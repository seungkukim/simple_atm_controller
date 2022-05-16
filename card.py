from bank import Bank

class Card:
    def __init__(self, card_number: str, pin: str, bank: Bank):
        self.pin = pin
        self.card_number = card_number
        # Foreign key referencing bank
        self.bank = bank

    def __eq__(self, other):
        return self.card_number == other.card_number

    # Get foreign key
    def get_bank(self):
        return self.bank

    # Card Transaction
    def verify_pin(self, input_pin: str):
        return self.pin == input_pin
