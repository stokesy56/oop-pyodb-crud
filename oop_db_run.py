from oop_db_connection import *
from products_class import *

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_nw = ConnectMsS(server,database,username,password)
# print(db_nw)
# print(db_nw.conn_nwdb)
#
# print(db_nw.cursor.execute("SELECT * FROM Products").fetchone())
# print(db_nw.cursor.execute("SELECT * FROM Products").fetchone().UnitPrice)
#
# print(db_nw.sql_query("SELECT * FROM Products").fetchone())
#
#print(db_nw.avg_price_from_products())

product1 = Products(server,database,username,password)

print(product1)