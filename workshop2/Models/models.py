from .clcrypto import hash_password
from datetime import datetime


class User:
    """
    Class for working with 'users' table
    """
    verbose = True  # table info prints

    def __init__(self, username="", password=""):
        self._id = -1
        self.username = username
        self._hashed_password = hash_password(password)

    def __str__(self):
        return f"user_id: {self.id} username: {self.username} hashed_password: {self.hashed_password}"

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, password):
        self._hashed_password = hash_password(password)

    def save_to_db(self, db):
        if self.id == -1:
            sql_query = f"""
            INSERT INTO users (username, hashed_password)
            VALUES
                ('{self.username}', '{self.hashed_password}')
            RETURNING user_id
            """
            self._id = db.execute_sql(sql_query)[0][0]
            if self.verbose:
                print(f"User '{self.username}' added to the database.")
        else:
            sql_query = f"""
            UPDATE users
            SET 
                username = '{self.username}',
                hashed_password = '{self.hashed_password}'
            WHERE user_id = {self.id}
            """
            db.execute_sql(sql_query)
            if self.verbose:
                print(f"User '{self.username}' successfully modified within the database.")

    @staticmethod
    def load_user_by_username(db, username):
        sql_query = f"""
            SELECT * 
            FROM users
            WHERE username = '{username}'
            """
        result = db.execute_sql(sql_query)
        if result:
            user = User(username=result[0][1])
            user._id = result[0][0]
            user._hashed_password = result[0][2]
            return user

    @staticmethod
    def load_user_by_id(db, user_id):
        sql_query = f"""
            SELECT * 
            FROM users
            WHERE user_id = {user_id}
            """
        result = db.execute_sql(sql_query)
        if result:
            user = User(username=result[0][1])
            user._id = result[0][0]
            user.hashed_password = result[0][2]
            return user

    @staticmethod
    def load_all_users(db):
        sql_query = f"""
        SELECT *
        FROM users
        """
        users = []
        results = db.execute_sql(sql_query)
        for result in results:
            user = User(username=result[1])
            user._id = result[0]
            user.hashed_password = result[2]
            users.append(user)
        return users

    def delete(self, db):
        sql_query = f"""
        DELETE FROM users
        WHERE user_id = {self._id}
        RETURNING user_id
        """
        result = db.execute_sql(sql_query)
        if result:
            self._id = -1
            if self.verbose:
                print(f"User with user_id {result[0][0]} deleted.")


class Message:
    """
    Class for working with 'messages' table
    """
    verbose = True  # table info prints

    def __init__(self, from_id, to_id, text="", creation_date=None):
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_date = creation_date

    def __str__(self):
        return (f"message_id: {self.id} from: {self.from_id} to: {self.to_id} "
                f"text: {self.text} created: {self.creation_date}")

    @property
    def id(self):
        return self._id

    def save_to_db(self, db):
        if self.id == -1:
            sql_query = f"""
            INSERT INTO messages (from_id, to_id, text)
            VALUES
                ({self.from_id}, {self.to_id}, '{self.text}')
            RETURNING message_id, creation_date
            """
            self._id, self.creation_date = db.execute_sql(sql_query)[0]
            if self.verbose:
                print(f"Message id {self.id} added to the database.")
        else:
            sql_query = f"""
            UPDATE messages
            SET 
                from_id = {self.from_id},
                to_id = {self.to_id},
                text = '{self.text}'
                creation_date = {datetime.today()}
            WHERE message_id = {self.id}
            """
            db.execute_sql(sql_query)
            if self.verbose:
                print(f"Message id {self.id} successfully modified within the database.")

    @staticmethod
    def load_all_messages(db):
        sql_query = f"""
        SELECT *
        FROM messages
        """
        messages = []
        results = db.execute_sql(sql_query)
        for result in results:
            message = Message(from_id=result[1], to_id=result[2])
            message._id = result[0]
            message.text = result[3]
            message.creation_date = result[4]
            messages.append(message)
        return messages
