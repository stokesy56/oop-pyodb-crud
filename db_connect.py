import pyodbc
# In this file we'll make our connection

# Parameters/variables for connection
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER= '+server+';DATABASE='+database+';UID='+username+';PWD='+password)


print(conn_nwdb)

# Create a cursor
cursor = conn_nwdb.cursor() #allows us to execute read only queries on the databse

# using .execute() on cursor
cursor.execute("SELECT * FROM Customers")

#Fetch rows from cursor
#.fetchone()
row = cursor.fetchone()
print(row)

row = cursor.fetchone() # it maintains state
print(row.ContactName)

row = cursor.fetchone() # it maintains state
print(row.ContactName)

# .fetchall()
rows = cursor.execute("SELECT * FROM Customers").fetchall() #don't normally use as could overload computer
#print(rows)
print(type(rows)) #if this is a list, then:

# Fetch some data using for loop
rows = cursor.execute("SELECT * FROM Products").fetchall()
#we can iterate
#for record in rows:
    #print(type(record))
    #print(record.UnitPrice) #we can acces the column of a specific record

# However, this is dangerous
# Because we can clog our machine with too much data
    # can use while loop to be more efficient

rows = cursor.execute("SELECT * FROM Products")

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)


