from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/users', methods=['POST'])
def create_user():
    name = request.json.get('name')
    email = request.json.get('email')
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return {'id': new_user.id}, 201

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return {'error': 'User not found'}, 404
    return {'name': user.name, 'email': user.email}

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user is None:
        return {'error': 'User not found'}, 404
    user.name = request.json.get('name', user.name)
    user.email = request.json.get('email', user.email)
    db.session.commit()
    return {'name': user.name, 'email': user.email}

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    db.create_all()
    app.run()