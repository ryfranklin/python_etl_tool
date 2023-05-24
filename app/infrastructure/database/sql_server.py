import pyodbc
from flask import g
from dotenv import load_dotenv
import os

load_dotenv()


class SqlServerConnection:
    def __init__(self):
        self.server = os.environ.get("SERVER")
        self.database = os.environ.get("DATABASE")
        self.username = os.environ.get("USERNAME")
        self.password = os.environ.get("PASSWORD")
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = pyodbc.connect(
                '''
                Driver={ODBC DRIVER 17 for SQL server};
                SERVER=%s;
                DATABASE=%s;
                UID=%s;
                PWD=%s;
                TrustServerCertificate=yes;
                Encrypt=yes;
                ''' % (self.server,
                       self.database,
                       self.username,
                       self.password), fast_executemany=True
            )
        return g.db

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_db(self):
        if 'db' not in g:
            g.db = self.connect()
            return g.db
        
    def close_db(e=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()
