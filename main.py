from datetime import date
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def list_atividades():
    return [
        {'name': 'estudar', 'endDate': date.today(), 'description': 'Estudar para o TCC'}
    ]