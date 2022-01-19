import psycopg2

connection = psycopg2.connect(
                host="localhost",
                database="db-demos",
                user="postgres",
                password="1234")

cursor = connection.cursor()
cursor.execute('SELECT * FROM Humans')
print(cursor)
connection.close()

