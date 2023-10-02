from fastapi import APIRouter
from models import Item

router = APIRouter()

from controllers import create_item as create_item_controller, read_item as read_item_controller, update_item as update_item_controller, delete_item as delete_item_controller

@router.post('/items/')
def create_item(item: Item):
    return create_item_controller(item)

@router.get('/items/{item_id}')
def read_item(item_id: int):
    return read_item_controller(item_id)

@router.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return update_item_controller(item_id, item)

@router.delete('/items/{item_id}')
def delete_item(item_id: int):
    return delete_item_controller(item_id)