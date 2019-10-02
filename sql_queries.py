import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER= '+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = conn_nwdb.cursor()

#query1
print('Question 1')
rows = cursor.execute("SELECT * FROM Orders").fetchall()
print(len(rows),'\n')

#query2
print('Question 2')
rows = cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro'").fetchall()
print(len(rows),'\n')

#query3
print('Question 3')
    rows = cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro' OR ShipCity = 'Reims'").fetchall()
for row in rows:
    print(row)

