from oop_db_connection import *

class Products(ConnectMsS):

    def read_all_entries(self):
        query_rows = self.__filter_query(f"SELECT * FROM Products")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def read_one_entry(self, *id):
        query = self.__filter_query(f"SELECT * FROM Products WHERE ProductID = '{id}'")
        return query.fetchone()

    def update_one_entry(self,column,entry,id):
        query = self.__filter_query(f"UPDATE Products SET {column} = '{entry}' WHERE ProductID = '{id}'")
