from psycopg2 import connect, errors
from dotenv import load_dotenv
from os import getenv


class DatabaseProcessor:
    """
    Class for working with the database
    """
    def __init__(self, dbname, autoconnect=True):
        self.dbname = dbname
        load_dotenv()
        self.username = getenv('DB_USER')
        self.__password = getenv('DB_PASSWORD')
        self.host = getenv('DB_HOST')
        self.port = getenv('DB_PORT')
        self.cnx = None
        self.cursor = None
        if autoconnect:
            self.connect_to_db(self.dbname)

    def connect_to_db(self, dbname, verbose=True):
        default_db = 'postgres'
        try:
            self.cnx = connect(database=dbname, user=self.username, password=self.__password,
                               host=self.host, port=self.port)
            self.cnx.autocommit = True
            self.cursor = self.cnx.cursor()
            if verbose:
                print(f"Successfully connected to '{dbname}' database.")
        except errors.OperationalError:
            print(f"Cannot connect to '{dbname}' database. HINT: Maybe it doesn't exist yet?")
            print(f"Connecting to default postgresql database ('{default_db}').")
            self.connect_to_db(default_db)

    def execute_sql(self, sql_query, verbose=False):
        if not self.cnx:
            raise ConnectionError("Not connected to any database!")
        if verbose:
            print(sql_query)
        try:
            self.cursor.execute(sql_query)
            return self.cursor.fetchall()

        # handling exceptions
        except errors.ProgrammingError as err:  # catch nothing to fetch ('nothing to return' queries)
            if "no results to fetch" in str(err).lower():
                return []
            else:
                raise
        except errors.Error as err:  # catch invalid sql query, re-raise all other exceptions
            if "syntax error" in str(err).lower():
                print("Invalid SQL query:")
                print(sql_query)
            else:
                raise

    def close_db(self, verbose=True):
        self.cursor.close()
        self.cnx.close()
        self.cnx = None
        self.cursor = None
        if verbose:
            print(f"Database '{self.dbname}' closed.")
