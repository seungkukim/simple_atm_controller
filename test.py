import unittest

from card import Card
from bank import Bank
from account import Account
from db import DB
from controller import Controller

class TestAtm(unittest.TestCase):

    def setUp(self):
        self.db = DB()
        bank = Bank("bank of korea")
        card1 = Card("1111", "1234", bank)
        card2 = Card("2222", "1234", bank)
        account1 = Account("111-222", card1)
        account2 = Account("222-333", card1)
        account3 = Account("333-444", card2)
        account4 = Account("444-555", card2)

        self.db.insert_bank(bank)
        self.db.insert_card(card1)
        self.db.insert_card(card2)
        self.db.insert_account(account1)
        self.db.insert_account(account2)
        self.db.insert_account(account3)
        self.db.insert_account(account4)

        self.controller = Controller(self.db)

    def test_card_num(self):
        self.assertTrue(self.controller.validate_card_num("1111"))
        self.assertTrue(self.controller.validate_card_num("2222"))
        self.assertFalse(self.controller.validate_card_num("1234"))
        self.assertFalse(self.controller.validate_card_num("4321"))

    def test_card_pin(self):
        self.assertTrue(self.controller.validate_card_pin("1111", "1234"))
        self.assertTrue(self.controller.validate_card_pin("2222", "1234"))
        self.assertFalse(self.controller.validate_card_pin("1111", "1111"))

    def test_get_account(self):
        account1_test = Account("111-222", Card("1111", "1234", Bank("bank of korea")))
        account2_test = Account("333-444", Card("2222", "1234", Bank("bank of korea")))
        self.assertEqual(self.controller.get_account("111-222"), account1_test)
        self.assertEqual(self.controller.get_account("333-444"), account2_test)

    def test_transaction(self):
        self.assertTrue(self.controller.deposit("111-222", 123), 123)
        self.assertTrue(self.controller.withdraw("111-222", 23), 100)
        self.assertTrue(self.controller.withdraw("111-222", 100), 0)
        self.assertTrue(self.controller.get_balance("111-222"), 0)

if __name__ == "__main__":
    unittest.main()