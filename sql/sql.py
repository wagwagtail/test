import pyodbc
from config import GetDetails
import datetime as dt
import time


def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from [python].[dbo].[price_table]")
    for row in cursor:
        print(f'row = {row}')
    print()


def write(conn):
    print("Create")
    cursor = conn.cursor()
    string = "insert into [python].[dbo].[price_table] (time, ask, bid) values('{now}',130.3, 130.2)".format(
        now=dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    cursor.execute(string)
    conn.commit()


if __name__ == "__main__":
    connection = GetDetails()
    connection.get_sql_server_name()
    connection.get_sql_database()
    string = 'Driver={{SQL Server}};Server={e};Database={d};Trusted_Connection=yes;'.format(
        e=connection.sql_server_name, d=connection.sql_database)

    conn = pyodbc.connect(string)

    cursor = conn.cursor()
    while True:
        write(conn)
        time.sleep(1)
