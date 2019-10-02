# Connecting SQL to Python using pyodbc :bread:

This is an example of us connecting to our SQL server, using python and pyodbc

We will look into:
- Cursor
- Rows
- Querying the db
- Using while loops for efficient data queries
- Transactions

## connection
    Connection objects manage connections to the database. 
    Each object manages a single ODBC connection (specifically a single HDBC).
    Connections are created through the module's connect() function

## .cursor()
    .cursor() returns a new Cursor object using the connection.
    The Cursor object represents a database cursor, which is typically used to manage the context of a fetch operation.

## .cursor().execute()
    Prepares and executes a SQL statement, returning the Cursor object itself. 

## .fetchall() vs .fetchone()
    .fetchall() returns a list of all the remaining rows in the query.
    .fetchone() Returns the next row in the query, or None when no more data is available.
 