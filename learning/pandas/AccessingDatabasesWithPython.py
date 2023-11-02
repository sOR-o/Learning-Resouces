from dbmodule import connect, close

# Create a database connection using the custom module
connection = connect('my_database.db', 'your_username', 'your_password')

# Create a cursor object
cursor = connection.cursor()

# Run queries
cursor.execute('SELECT * FROM my_table')
results = cursor.fetchall()

# Free resources
cursor.close()
connection.close()

