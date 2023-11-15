# build a schema using pydantic
from pydantic import BaseModel
from fastapi import FastAPI, Form, Depends

class KitBase(BaseModel):
    nome_instrumento: str

class KitCreate(KitBase):
    pass

class Kit(KitBase):
    id: int
    class Config:
        orm_mode = True


class CirurgiaBase(BaseModel):
    CRM_Medico: int
    CPF_Paciente: int
    Sala_Hospital: int
    Tipo_Cirurgia: str


class CirurgiaCreate(CirurgiaBase):
    pass

class Cirurgia(CirurgiaBase):
    id: int
    Kit_id: int
    
    class Config:
        orm_mode = True
