# Placeholder for MySQL database operations
def create():
    query = "INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2')"
    # Execute the query
    # db.execute(query)
    return 'Record created'

def read():
    query = "SELECT * FROM table_name"
    # Execute the query and fetch all records
    # records = db.execute(query).fetchall()
    return 'All records fetched'

# def update():
#     pass

# def delete():
#     pass