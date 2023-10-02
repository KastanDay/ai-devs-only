from models import Item

def create_item(item):
    item = Item(**item)
    return item.create()

def read_item(item_id):
    return Item.read(item_id)

def update_item(item_id, item):
    item = Item(**item)
    return item.update()

def delete_item(item_id):
    return Item.delete(item_id)