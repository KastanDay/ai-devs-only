from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://user:password@localhost/dbname')
metadata = MetaData()

# Define your tables here