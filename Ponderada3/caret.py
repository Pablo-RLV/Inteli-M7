# Importações das bibliotecas necessárias
import pandas as pd  # Para manipulação de dados tabulares
from pydantic import create_model  # Para criar modelos Pydantic
from pycaret.classification import load_model, predict_model  # Para carregar e usar modelos de classificação com o PyCaret
from fastapi import FastAPI, Request, Form  # Para criar a aplicação web FastAPI e lidar com formulários
from fastapi.templating import Jinja2Templates  # Para renderização de templates HTML
from fastapi.staticfiles import StaticFiles  # Para servir arquivos estáticos
import uvicorn  # Para executar o servidor ASGI

# Inicialização do aplicativo FastAPI
app = FastAPI()

# Configuração para usar templates Jinja2
templates = Jinja2Templates(directory="templates")

# Montagem de arquivos estáticos para uso na aplicação
app.mount("/static", StaticFiles(directory="static"), name="static")

# Carregar um modelo de classificação treinado anteriormente (do arquivo "caret")
model = load_model("caret")

# Definir um modelo Pydantic para a estrutura dos dados de entrada
input_model = create_model("pycaret_input", **{'Gender': 1, 'Age': 63, 'Anual_Income': 48})

# Definir um modelo Pydantic para a estrutura dos dados de saída
output_model = create_model("pycaret_output", prediction='Comum')

# Rota raiz ("/") que renderiza a página "index.html" usando Jinja2
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Rota "/predict" para processar dados enviados pelo usuário via formulário
@app.post("/predict")
async def process_form_data(request: Request, age: int = Form(...), anual_income: int = Form(...), inlineRadioOptions: int = Form(...)):
    # Coleta os dados do formulário e cria um DataFrame pandas com eles
    data = {"Gender": inlineRadioOptions, "Age": age, "Anual_Income": anual_income}
    data = pd.DataFrame([data])

    # Faz previsões com base nos dados usando o modelo carregado anteriormente
    predictions = predict_model(model, data=data)

    # Retorna o resultado da previsão para ser exibido na página "index.html"
    return templates.TemplateResponse("index.html", {"request": request, "prediction": predictions["prediction_label"].iloc[0]})

# Executar a aplicação usando o servidor Uvicorn na porta 8000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
