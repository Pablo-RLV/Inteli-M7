import os
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse

app = FastAPI()
url = "postgresql://user:password@postgres:5432/database"
filename = './static/img/grafico.png'

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index(request: Request):
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


@app.get("/predict")
async def graph(prediction: str = "oi"):
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO predictions (prediction) VALUES ('" + prediction + "')")
    connection.commit()
    cursor.execute("SELECT * FROM predictions")
    banco = cursor.fetchall()
    df = pd.DataFrame(banco, columns=['id', 'prediction'])
    df = df['prediction'].value_counts()
    df.plot(kind='bar', color="black")
    if os.path.exists(filename):
        os.remove(filename)
    plt.savefig(filename)
    plt.close()
    cursor.close()
    connection.close()
    return RedirectResponse(url="/") , FileResponse(filename)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)