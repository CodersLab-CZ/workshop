from Models.DatabaseProcessor import DatabaseProcessor, errors

CREATE_USERS_TABLE = """
                     CREATE TABLE users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(255) UNIQUE,
                        hashed_password VARCHAR(80)
                        )                   
                     """
CREATE_MESSAGES_TABLE = """
                        CREATE TABLE messages (
                           message_id SERIAL PRIMARY KEY,                           
                           from_id INTEGER,
                           to_id INTEGER,
                           text TEXT,
                           creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                           FOREIGN KEY (from_id) REFERENCES users(user_id) ON DELETE CASCADE,
                           FOREIGN KEY (to_id) REFERENCES users(user_id) ON DELETE CASCADE
                           )
                        """


def create_db(db, autoconnect=True, verbose=True):
    create_db_query = f"""
                      CREATE DATABASE {db.dbname}
                      """
    try:
        db.execute_sql(create_db_query)
        if verbose:
            print(f"Database '{db.dbname}' created.")
        if autoconnect:
            db.connect_to_db(db.dbname)
    except errors.DuplicateDatabase:
        print(f"Database '{db.dbname}' already exists!")


def create_table(db, table_name, create_table_query, verbose=True):
    try:
        db.execute_sql(create_table_query)
        if verbose:
            print(f"Table '{table_name}' created.")
    except errors.DuplicateTable:
        print(f"Table '{table_name}' already exists!")


try:
    db = DatabaseProcessor('workshop2_db', autoconnect=True)
    create_db(db)
    create_table(db, 'users', CREATE_USERS_TABLE)
    create_table(db, 'messages', CREATE_MESSAGES_TABLE)
    db.close_db()
except ConnectionError as e:
    print(e)
