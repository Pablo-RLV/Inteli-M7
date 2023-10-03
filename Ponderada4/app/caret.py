from datetime import datetime, timedelta
from typing import Annotated, Union
from fastapi import Depends, FastAPI, HTTPException, status, Request, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from dotenv import load_dotenv
from pydantic import create_model
from pycaret.classification import load_model, predict_model
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse
import pandas as pd
import matplotlib.pyplot as plt
import uvicorn
import psycopg2
import os

load_dotenv()

url = "postgresql://user:password@postgres:5432/database"
filename = './static/img/grafico.png'

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

model = load_model("caret")
input_model = create_model("pycaret_input", **{'Gender': 1, 'Age': 63, 'Anual_Income': 48})
output_model = create_model("pycaret_output", prediction='Comum')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

users = {
    os.environ.get("USER"): {
        "username": os.environ.get("USERNAME"),
        "hashed_password": os.environ.get("PASSWORD"),
        "disabled": False,
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class User(BaseModel):
    username: str
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(users, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/user", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

@app.get("/")
async def exibir_formulario(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/home")
async def read_root(request: Request):
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM predictions ORDER BY id DESC LIMIT 1")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    if len(result) > 0:
        prediction = result[0][1]
    else:
        prediction = ""
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction})

@app.get("/graph")
async def graph():
    try: 
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM predictions")
        banco = cursor.fetchall()
        df = pd.DataFrame(banco, columns=['id', 'prediction'])
        df = df['prediction'].value_counts()
        df.plot(kind='bar', color="black")
        if os.path.exists(filename):
            os.remove(filename)
        plt.savefig(filename)
        print("gráfico criado")
        plt.close()
        cursor.close()
        connection.close()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao se conectar ao banco de dados:", e)
    return FileResponse(filename)

@app.post("/predict")
async def process_form_data(age: int = Form(...), anual_income: int = Form(...), inlineRadioOptions: int = Form(...)):
    data = {"Gender": inlineRadioOptions, "Age": age, "Anual_Income": anual_income}
    data = pd.DataFrame([data])
    predictions = predict_model(model, data=data)
    result = predictions["prediction_label"].iloc[0]
    try:
        connection = psycopg2.connect(url)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO predictions (prediction) VALUES ('" + result + "')")
        connection.commit()
        print("Inserido no banco de dados")
        cursor.close()
        connection.close()
    except psycopg2.Error as e:
        print("Ocorreu um erro ao se conectar ao banco de dados:", e)
    return RedirectResponse(url="/home", status_code=302)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
