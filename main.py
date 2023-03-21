from fastapi import FastAPI
from utils.mock import Mock

app = FastAPI()


@app.get('/')
def list_atividades():
    return Mock.get_list()
