from fastapi import FastAPI
from .rotas import select_all

app = FastAPI()

app.include_router(select_all.router, tags=["Realiza o select de todos os dados, salvos com o run_pipeline, do banco de dados."])


