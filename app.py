from flask import Flask
from views import router as views_router
from controllers import create_item, read_item, update_item, delete_item

app = Flask(__name__)
app.register_blueprint(views_router)

@app.route('/items/', methods=['POST'])
def create_item_route(item):
    return create_item(item)

@app.route('/items/<int:item_id>', methods=['GET'])
def read_item_route(item_id):
    return read_item(item_id)

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item_route(item_id, item):
    return update_item(item_id, item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item_route(item_id):
    return delete_item(item_id)

if __name__ == '__main__':
    app.run()