from card import Card

class Account:
    def __init__(self, account_num: str, card: Card):
        self.balance = 0
        self.account_num = account_num
        # foreign key referencing card
        self.card = card

    def __eq__(self, other):
        return self.account_num == other.account_num

    # Get foreign key
    def get_card(self):
        return self.card

    # Account Transaction
    def get_balance(self):
        return self.balance

    def withdraw(self, amount: int):
        if self.balance < amount:
            return False
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount: int):
        self.balance = self.balance + amount
        return self.balance
