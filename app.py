from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print('Received data:', data)
    return 'Success', 200

if __name__ == '__main__':
    db.create_all()
    app.run(port=5000)