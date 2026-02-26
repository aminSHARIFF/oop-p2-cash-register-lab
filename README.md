# Cash Register OOP Lab

## Overview

This project implements a `CashRegister` class in Python to simulate the basic functionality of an e-commerce cash register.

The register allows:
- Adding items
- Tracking total price
- Applying percentage discounts
- Voiding the last transaction

All functionality is tested using pytest.

---

## Features

### Attributes
- `discount` – percentage discount applied to total
- `total` – running total of all items
- `items` – list of items added (includes duplicates if quantity > 1)
- `previous_transactions` – stores transaction history for void functionality

---

### Methods

#### add_item(title, price, quantity=1)
- Adds item(s) to the register
- Updates total
- Stores transaction history

#### apply_discount()
- Applies percentage discount to total
- Prints updated total
- Prints error if no discount exists

#### void_last_transaction()
- Removes the last transaction
- Updates total and items list
- Prints error if no transactions exist

---

## Running Tests

To run tests locally:
