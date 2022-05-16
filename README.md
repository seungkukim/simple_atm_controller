# simple_atm_controller

### Structure of Application

## Data Entity
There are 3 classes Bank, Card, and Account. These classes act as an abstraction of the real world ATM model.
Each class represent each relation with member variable corresponding to attributes of a relation.

- Bank
  - Stores the name of a bank
  
- Card
  - Stores the card_number, pin, and bank (foreign key referencing bank)
  - Supports retrieving foreign key by get_bank()
  - Stored procedure verify_pin is supported verify_pin(input_pin)
  
- Account
  - Stores the account_num, balance and card (foreign key referencing card)
  - Supports retrieving foreign key by get_card()
  - Stored procedure get_balance(), withdraw(amount), deposit(amount) are used as transaction with ATM.
  
  
## Controller
Acts as an interface between the user and actual database
Uses functionality of the 3 data entities plus some other logic
to serve the functionality of an ATM.

- Supports functionality of verifying card number and card pin
- Supports getting account by account number
- Supports atm transaction between account and user


## DB
DB class (db.py) has 3 list has it's member variable.
It's member variable represent a separate relation in a database.
Each list stores banks, cards, and accounts in bank_table, card_table and account_table respectively.

Since an abstraction of a database is used normal CRUD capabilities are not implemented.
Hence, there are member functions that implement simple insert and select capabilities.
More, sql capabilities can be implemented here, or a real database can be connected
instead of using member variables as storage.

### Install Application
Clone code from the github repo and run the code by changing the directory to simple_atm_controller

```code
git clone https://github.com/seungkukim/simple_atm_controller.git

cd simple_atm_controller
```

### Test Application
Unit test is conducted with `unittest` framework with
the test code located in test.py

To run tests, cd into simple_atm_controller directory and run 

```code
python3 test.py
```
