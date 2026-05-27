from fastapi import FastAPI

app = FastAPI(app = FastAPI(
 title="Aula",
 summary="API desenvolvida durante a aula de Construção de APIs para IA",
 version="0.1",
 terms_of_service="http://example.com/terms/",
 contact={
 "name": "Hélio Martins T Neto",
 "url": "http://github.com/rogerior/",
 "email": "rogerior@ufg.br",
 },
 license_info={
 "name": "Apache 2.0",
 "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
 },
))

@app.get("/teste")
def hello_world():
    return {"mensagem": " Hello World"}

# Passando o número 1 e 2 na URL http://127.0.0.1:8000/soma/5/5
@app.get("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição http://127.0.0.1:8000/soma_formato2?numero1=5&numero2=5
@app.post("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição http://127.0.0.1:8000/soma_formato3
from pydantic import BaseModel
class Numeros(BaseModel):
    numero1: int
    numero2: int
 
class Resultado(BaseModel):
    resultado: int

@app.post("/soma_formato3", response_model= Resultado)
def soma_formato3(numeros: Numeros):
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}