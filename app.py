from fastapi import FastAPI
import db_operations

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.post('/create')
def create():
    return db_operations.create()

@app.get('/read')
def read():
    return db_operations.read()

@app.put('/update')
def update():
    return db_operations.update()

@app.delete('/delete')
def delete():
    return db_operations.delete()