import json
from user import User
from account import Account
from message import Message

class Auth:
    def __init__(self):
        self.message = Message()

    def login(self, username, password):
        with open('db.json', 'r') as file:
            users = json.load(file)['users']

        for user in users:
            if user['name'] == username:
                if user['password'] == password:
                    accounts = {}
                    for account in user['accounts']:
                        accounts[account['accountNumber']] = Account(account['balance'])
                    return User(user['name'], accounts)
                else:
                    self.message.print("name or password not found")
            else:
                self.message.print("name or password not found")
            
        return None
