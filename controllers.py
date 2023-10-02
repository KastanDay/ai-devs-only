items = {}

def create_item(item):
    items[item.id] = item.name
    return {'message': 'Item created', 'item': item}

def read_item(item_id):
    if item_id in items:
        return {'message': 'Item read', 'item': {'id': item_id, 'name': items[item_id]}}
    else:
        return {'message': 'Item not found'}

def update_item(item_id, item):
    if item_id in items:
        items[item_id] = item.name
        return {'message': 'Item updated', 'item': item}
    else:
        return {'message': 'Item not found'}

def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return {'message': 'Item deleted'}
    else:
        return {'message': 'Item not found'}