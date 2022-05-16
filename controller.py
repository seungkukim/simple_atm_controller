from card import Card
from bank import Bank
from account import Account
from db import DB


class Controller:

    def __init__(self, db: DB):
        self.db = db

    # Card Related Functionalities
    def validate_card_num(self, card_num: str):
        my_card = self.db.select_card(card_num)
        if my_card is not None:
            return True
        else:
            return False

    def validate_card_pin(self, card_num: str, pin: str):
        my_card = self.db.select_card(card_num)
        if my_card is not None:
            return my_card.pin == pin
        else:
            return False

    # Account Related Functionalities
    def get_account(self, account_num: str):
        my_account = self.db.select_account(account_num)
        if my_account is not None:
            return my_account
        else:
            return False

    def get_balance(self, account_num):
        my_account = self.get_account(account_num)
        if my_account:
            return my_account.get_balance()

    def deposit(self, account_num: str, amount: int):
        my_account = self.get_account(account_num)
        if my_account:
            return my_account.deposit(amount)

    def withdraw(self, account_num: str, amount: int):
        my_account = self.get_account(account_num)
        if my_account:
            return my_account.deposit(amount)