from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    items = {}

    def create(self):
        self.items[self.id] = self.name
        return {'message': 'Item created', 'item': self}

    @classmethod
    def read(cls, item_id):
        if item_id in cls.items:
            return {'message': 'Item read', 'item': {'id': item_id, 'name': cls.items[item_id]}}
        else:
            return {'message': 'Item not found'}

    def update(self):
        if self.id in self.items:
            self.items[self.id] = self.name
            return {'message': 'Item updated', 'item': self}
        else:
            return {'message': 'Item not found'}

    @classmethod
    def delete(cls, item_id):
        if item_id in cls.items:
            del cls.items[item_id]
            return {'message': 'Item deleted'}
        else:
            return {'message': 'Item not found'}