import pyodbc

# Concept of 'Strong Params'
    # never ever trust user input
    # avoid sql injections
    # filter for sql conceptions

class ConnectMsS():
    def __init__(self,server,database,username,password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER= '+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def __filter_query(self, query): # Strong Params / Filter
        # doing some filtering for bad queries
        return self.cursor.execute(query)


    def sql_query(self, query):
        return self.__filter_query(query)

    def __sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone()

    def print_all_records_from_table(self,table):
        query_rows = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def avg_price_from_products(self):
        query_row = self.__filter_query("SELECT * FROM Products")
        prices = []
        while True:
            record = query_row.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        return (sum(prices)/len(prices))

    # CRUD:

    # Create 1 entry
        # Use INSERT
        # The Cursor cannot make transaction (go to documentation)
    # Read all entries
        # Fetch all records and return as a list of dictionaries
    # Read one entry
        # Fetch a specific record
        # Get one value using ID
    # Update 1 entry
        # The ID of the record to update
        # Update the specific record
            # The cursor cannot make transaction (go to documentation)
    # Destroy 1 entry
        # The ID of the specific record
        # Destroy the record
            # The cursor cannot make transaction (go to documentation)
