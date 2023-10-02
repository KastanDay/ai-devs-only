from flask import Flask
from views import router as views_router
from controllers import create_item, read_item, update_item, delete_item

app = Flask(__name__)
app.register_blueprint(views_router)

from fastapi.middleware.wsgi import WSGIMiddleware
from views import router as fastapi_router

app = Flask(__name__)
app.wsgi_app = WSGIMiddleware(fastapi_router)

if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    app.run()