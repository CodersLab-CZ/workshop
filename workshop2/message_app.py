import argparse
from Models import clcrypto
from Models.DatabaseProcessor import DatabaseProcessor
from Models.models import User, Message


class MessageApp:
    """
    Command line interface for messages table
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-u', '--username', help='username')
        self.parser.add_argument('-p', '--password', help='password (min 8 characters)')
        self.parser.add_argument('-t', '--to', help='recipient of a message')
        self.parser.add_argument('-s', '--send', help='message content')
        self.parser.add_argument('-l', '--list', help='list of all users', action='store_true')
        self.args = self.parser.parse_args()

    def process_args(self, db):
        if self.args.username and self.args.password and self.args.to and self.args.send:
            self.send_message(db)
        elif self.args.list:
            self.list_messages(db)
        else:
            self.parser.print_help()

    def send_message(self, db):
        user_from = User.load_user_by_username(db, username=self.args.username)
        if not user_from:
            raise ValueError(f"User {self.args.username} not found!")
        if not clcrypto.check_password(self.args.password, user_from.hashed_password):
            raise ValueError("Incorrect password!")
        user_to = User.load_user_by_username(db, username=self.args.to)
        if not user_to:
            raise ValueError(f"User {self.args.username} not found!")
        if len(self.args.send) > 255:
            raise ValueError("Message is too long (max. 255 characters)!")
        message = Message(user_from.id, user_to.id, self.args.send)
        message.save_to_db(db)

    @staticmethod
    def list_messages(db):
        messages = Message.load_all_messages(db)
        if messages:
            print("List of all messages:\n")
            for message in messages:
                print(message)
        else:
            print("No messages found.")


if __name__ == '__main__':
    try:
        db = DatabaseProcessor('workshop2_db', autoconnect=True)
        message_app = MessageApp()
        message_app.process_args(db)
        db.close_db()
    except ConnectionError as e:
        print(e)
    except ValueError as e:
        print(e)
