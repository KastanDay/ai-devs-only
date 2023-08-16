from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

# Placeholder for MySQL database operations
# def db_operations():
#     pass