from fastapi import FastAPI

app = FastAPI()

from .database import engine, metadata
from sqlalchemy import select, insert, update, delete
from fastapi import HTTPException

@app.get('/items')
def read_items():
    with engine.connect() as connection:
        result = connection.execute(select('*').select_from('items'))
        return result.fetchall()

@app.post('/items')
def create_item(item):
    with engine.connect() as connection:
        result = connection.execute(insert('items').values(item))
        return {'id': result.inserted_primary_key[0]}

@app.put('/items/{item_id}')
def update_item(item_id, item):
    with engine.connect() as connection:
        result = connection.execute(update('items').where('id = :id').values(item), id=item_id)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail='Item not found')
        return {'id': item_id}

@app.delete('/items/{item_id}')
def delete_item(item_id):
    with engine.connect() as connection:
        result = connection.execute(delete('items').where('id = :id'), id=item_id)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail='Item not found')
        return {'id': item_id}