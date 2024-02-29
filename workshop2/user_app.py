import argparse
from Models import clcrypto
from Models.DatabaseProcessor import DatabaseProcessor, errors
from Models.models import User


class UserApp:
    """
    Command line interface for users table
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-u', '--username', help='username')
        self.parser.add_argument('-p', '--password', help='password (min 8 characters)')
        self.parser.add_argument('-n', '--new_pass', help='new password (min 8 characters)')
        self.parser.add_argument('-e', '--edit', help='edit a user', action='store_true')
        self.parser.add_argument('-l', '--list', help='list of all users', action='store_true')
        self.parser.add_argument('-d', '--delete', help='delete a user', action='store_true')
        self.args = self.parser.parse_args()

    def process_args(self, db):
        if self.args.username and self.args.password and self.args.edit and self.args.new_pass:
            self.edit_password(db)
        elif self.args.username and self.args.password and self.args.delete:
            self.delete_user(db)
        elif self.args.username and self.args.password:
            self.create_user(db)
        elif self.args.list:
            self.list_users(db)
        else:
            self.parser.print_help()

    def create_user(self, db):
        if len(self.args.password) < 8:
            raise ValueError("Password should have at least 8 characters!")
        try:
            user = User(username=self.args.username, password=self.args.password)
            user.save_to_db(db)
        except errors.UniqueViolation:
            print(f"User {self.args.username} already exists!")

    def edit_password(self, db):
        user = User.load_user_by_username(db, username=self.args.username)
        if not user:
            raise ValueError(f"User '{self.args.username}' not found!")
        if not clcrypto.check_password(self.args.password, user.hashed_password):
            raise ValueError("Incorrect password!")
        if len(self.args.new_pass) < 8:
            raise ValueError("New password should have at least 8 characters!")
        user.hashed_password = self.args.new_pass  # is hashed inside User class
        user.save_to_db(db)

    def delete_user(self, db):
        user = User.load_user_by_username(db, username=self.args.username)
        if not user:
            raise ValueError(f"User {self.args.username} not found!")
        if not clcrypto.check_password(self.args.password, user.hashed_password):
            raise ValueError("Incorrect password!")
        user.delete(db)

    @staticmethod
    def list_users(db):
        users = User.load_all_users(db)
        if users:
            print("List of all users:\n")
            for user in users:
                print(user)
        else:
            print("No users found.")


if __name__ == '__main__':
    try:
        db = DatabaseProcessor('workshop2_db', autoconnect=True)
        user_app = UserApp()
        user_app.process_args(db)
        db.close_db()
    except ConnectionError as e:
        print(e)
    except ValueError as e:
        print(e)
