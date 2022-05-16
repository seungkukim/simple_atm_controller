from card import Card
from bank import Bank
from account import Account

class DB:
    def __init__(self):
        self.bank_table = list()
        self.card_table = list()
        self.account_table = list()

    # Insert operation
    def insert_bank(self, bank: Bank):
        self.bank_table.append(bank)
        return

    def insert_card(self, card: Card):
        self.card_table.append(card)
        return

    def insert_account(self, account: Account):
        self.account_table.append(account)
        return

    # Select operation
    def select_card(self, card_number: str):
        for c in self.card_table:
            if c.card_number == card_number:
                return c
        return None

    def select_account(self, account_num: str):
        for a in self.account_table:
            if a.account_num == account_num:
                return a
        return None

    def select_bank(self, name: str):
        for b in self.bank_table:
            if b.name == name:
                return b
        return None
