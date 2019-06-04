import pyodbc
from config import GetDetails
import datetime as dt
import time

class SqlTable:
    def __init__(self):
        self.connection()

    def read(self):
        print("Read")
        cursor = self.conn.cursor()
        cursor.execute("select * from [python].[dbo].[instrument_table]")
        for row in cursor:
            print(f'row = {row}')
        print()


    def write(self, time,ask,bid):
        print("Create")
        cursor = self.conn.cursor()
        string = "insert into [python].[dbo].[instrument_table] (time, ask, bid) values('{time}',{ask}, {bid})".format(
            time=time, ask = ask, bid =bid)
        cursor.execute(string)
        self.conn.commit()


    def connection(self):
        connection = GetDetails()
        connection.get_sql_server_name()
        connection.get_sql_database()
        string = 'Driver={{SQL Server}};Server={e};Database={d};Trusted_Connection=yes;'.format(
            e=connection.sql_server_name, d=connection.sql_database)
        self.conn = pyodbc.connect(string)
        self.cursor = self.conn.cursor()
#
# if __name__ == '__main__':
#     while True:
#         test = SqlTable()
#         test.connection()
#         test.write()
#         time.sleep(1)


