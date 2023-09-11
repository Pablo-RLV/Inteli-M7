import pandas as pd
from pydantic import create_model
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

model = load_model("caret")

input_model = create_model("pycaret_input", **{'Gender': 1, 'Age': 63, 'Anual_Income': 48})
output_model = create_model("pycaret_output", prediction='Comum')

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def process_form_data(request: Request, age: int = Form(...), anual_income: int = Form(...), inlineRadioOptions: int = Form(...)):
    data = {"Gender": inlineRadioOptions, "Age": age, "Anual_Income": anual_income}
    data = pd.DataFrame([data])
    predictions = predict_model(model, data=data)
    return templates.TemplateResponse("index.html", {"request":request, "prediction": predictions["prediction_label"].iloc[0]})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
