import json
from user import User
from account import Account
from message import Message
import time

class Auth:
    def __init__(self):
        self.message = Message()

    def login(self, username, password):
        with open('db.json', 'r') as file:
            users = json.load(file)['users']

        for user in users:
            if user['name'] == username and user['password'] == password:
                accounts = self.get_accounts(user["accounts"])
                return User(user['name'], accounts)
            else:
                self.message.print("name or password not found")
            
        return None

    def get_accounts(self, allAccounts):
        returnAccounts = {}
        for account in  allAccounts:
            accountNumber = account['accountNumber']
            balance = account['balance']
            
            returnAccounts[accountNumber] = Account(balance)
        return returnAccounts