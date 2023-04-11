from fastapi import FastAPI
from utils.personal import PersonalAgenda, Event

app = FastAPI()


@app.get('/')
def list_events():
    return PersonalAgenda.get_list()


@app.get('/mock')
def list_mock_events():
    return PersonalAgenda.get_list_mock()


@app.post('/create')
def create_event(event: Event):
    return PersonalAgenda.create_event(event)
