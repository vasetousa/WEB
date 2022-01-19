import pyodbc

server = 'localhost'
database = 'SoftUni'
username = 'SA'
password = 'docker21@'

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = connection.cursor()
print ('Reading data from table:')
print()
tsql = "SELECT * FROM Employees WHERE EmployeeId between 10 and 20;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        # print (str(row[0]) + " " + str(row[1]))
        print('-->  ', end=''), print(*row)
        row = cursor.fetchone()