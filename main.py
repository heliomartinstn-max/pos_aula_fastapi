from enum import Enum

from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field

def common_api_token(api_token: str):
    if api_token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido")
    return {"api_token": api_token}

app = FastAPI(
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
 dependencies=[Depends(common_api_token)]
)

API_TOKEN="123"



@app.get("/teste")
def hello_world():
    return {"mensagem": " Hello World"}

# Passando o número 1 e 2 na URL http://127.0.0.1:8000/soma/5/5
@app.get("/soma/v1/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição http://127.0.0.1:8000/soma_formato2?numero1=5&numero2=5
@app.post("/soma/v2")
def soma_formato2(numero1: int, numero2: int, api_token: str):
    total = numero1 + numero2
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição http://127.0.0.1:8000/soma_formato3

class Numeros(BaseModel):
    numero1: int
    numero2: int
    
 
class Resultado(BaseModel):
    resultado: int




@app.post("/soma/v3", 
          response_model= Resultado, 
          summary="Soma de dois números", 
          description="Essa rota recebe dois números e retorna a soma deles",
          tags=["Operações Matematicas"],
          )
def soma_formato3(numeros: Numeros):

    if numeros.API_TOKEN != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token de autenticação inválido")
    if numeros.numero1 < 0 or numeros.numero2 < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Os números devem ser positivos")
    
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}



class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"



@app.post("/operacao_matematica", tags=["Operações Matematicas"])
def operacao_matematica(numeros: Numeros, operacao: TipoOperacao):
    if operacao == TipoOperacao.soma:
        resultado = numeros.numero1 + numeros.numero2
    elif operacao == TipoOperacao.subtracao:
        resultado = numeros.numero1 - numeros.numero2
    elif operacao == TipoOperacao.multiplicacao:
        resultado = numeros.numero1 * numeros.numero2
    elif operacao == TipoOperacao.divisao:
        resultado = numeros.numero1 / numeros.numero2
    return {"resultado": resultado}