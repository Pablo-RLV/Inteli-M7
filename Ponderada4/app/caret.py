from pydantic import create_model
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse
import pandas as pd
import matplotlib.pyplot as plt
import uvicorn
import psycopg2
import os

url = "postgresql://user:password@postgres:5432/database"
filename = './static/img/grafico.png'

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

model = load_model("caret")
input_model = create_model("pycaret_input", **{'Gender': 1, 'Age': 63, 'Anual_Income': 48})
output_model = create_model("pycaret_output", prediction='Comum')

@app.get("/")
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
        cursor.execute("SELECT * FROM predictions")
        banco = cursor.fetchall()
        df = pd.DataFrame(banco, columns=['id', 'prediction'])
        df = df['prediction'].value_counts()
        df.plot(kind='bar', color="black")
        if os.path.exists(filename):
            os.remove(filename)
            print("gráfico removido")
        plt.savefig(filename)
        plt.close()
        cursor.close()
        connection.close()
        print("Inserido no banco de dados")
    except psycopg2.Error as e:
        print("Ocorreu um erro ao se conectar ao banco de dados:", e)
    return FileResponse(filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
