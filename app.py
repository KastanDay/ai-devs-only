from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from models import User
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

limiter = Limiter(app, key_func=get_remote_address, default_limits=['200 per day', '50 per hour'])

db = SQLAlchemy(app)

@app.route('/', methods=['POST'])
@limiter.limit('10/minute')
def webhook():
    data = request.get_json()
    print('Received data:', data)
    return 'Success', 200

if __name__ == '__main__':
    db.create_all()
    app.run(port=5000)