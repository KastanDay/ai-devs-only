import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='yourusername',
  password='yourpassword',
  database='mydatabase'
)

def get_data():
  mycursor = mydb.cursor()
  mycursor.execute('SELECT * FROM tablename')
  myresult = mycursor.fetchall()
  return myresult