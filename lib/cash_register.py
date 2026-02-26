#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        # Initialize attributes
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # -------------------------
    # Add Item
    # -------------------------
    def add_item(self, title, price, quantity=1):
        # Increase total
        self.total += price * quantity

        # Add items to list (include multiples)
        for _ in range(quantity):
            self.items.append(title)

        # Store transaction for possible void
        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    # -------------------------
    # Apply Discount
    # -------------------------
    def apply_discount(self):
        # If no discount
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply percentage discount
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Remove decimals if whole number
        if self.total.is_integer():
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    # -------------------------
    # Void Last Transaction
    # -------------------------
    def void_last_transaction(self):
        # If no transaction
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Get last transaction
        last = self.previous_transactions.pop()

        # Subtract from total
        self.total -= last["price"] * last["quantity"]

        # Remove items from items list
        for _ in range(last["quantity"]):
            self.items.pop()