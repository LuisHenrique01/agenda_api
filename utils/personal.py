from datetime import date
from typing import Optional
from uuid import uuid4, UUID

from pydantic import BaseModel


class Event(BaseModel):

    id: Optional[UUID] = uuid4()
    name: str
    description: str
    endDate: Optional[date] = date.today()


class PersonalAgenda:

    PersonalAgenda: list[Event] = []
    mock: list[Event] = [
        Event.construct(id=uuid4(), name='estudar', endDate=date.today(), description='Estudar para o TCC')
        ]

    @classmethod
    def get_list(cls):
        return cls.PersonalAgenda

    @classmethod
    def create_event(cls, event: Event | dict) -> dict:
        if isinstance(event, dict):
            cls.PersonalAgenda.append(Event.construct(**event))
        else:
            cls.PersonalAgenda.append(event)
        return cls.PersonalAgenda[-1]

    @classmethod
    def get_list_mock(cls) -> list[dict]:
        return cls.mock
