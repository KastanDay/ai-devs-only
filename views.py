from fastapi import APIRouter
from models import Item

router = APIRouter()

@router.post('/items/')
def create_item(item: Item):
    return {'message': 'Item created'}

@router.get('/items/{item_id}')
def read_item(item_id: int):
    return {'message': 'Item read'}

@router.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'message': 'Item updated'}

@router.delete('/items/{item_id}')
def delete_item(item_id: int):
    return {'message': 'Item deleted'}