from fastapi import FastAPI
from .db import get_data

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/data')
def read_data():
    return get_data()