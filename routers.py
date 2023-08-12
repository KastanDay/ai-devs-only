from fastapi import APIRouter
from models import User

router = APIRouter()

@router.post('/users/')
def create_user(user: User):
    return {'message': 'User created'}