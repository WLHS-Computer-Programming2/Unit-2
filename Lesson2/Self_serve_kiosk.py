class Kiosk:
    def __init__(self):
        self.total_items = 0
        self.transaction_total = 0.0
        self.items = {}
        self.amount_paid = 0.0

    def add_item(self):
        while True:
            item_name = input("Enter the item name (or type 'Done' to finish): ").title()
            if item_name == "Done":
                break
            while True:
                try:
                    price = float(input(f"Enter the price for {item_name}: "))
                    if price < 0:
                        print("Price cannot be negative. Please enter a valid price.")
                        continue
                    price = round(price, 2)
                    self.items[item_name] = price
                    self.total_items += 1
                    self.transaction_total += price
                    break
                except ValueError:
                    print("Invalid price. Please enter a numerical value.")

    def get_total(self):
        print(f"Total items: {self.total_items}, Total cost: ${self.transaction_total:.2f}")

    def take_payment(self):
        while self.amount_paid < self.transaction_total:
            try:
                payment = float(input(f"This kiosk only accepts cash. You still owe ${self.transaction_total - self.amount_paid:.2f}. Enter payment amount: "))
                if payment < 0:
                    print("Payment cannot be negative. Please enter a valid amount.")
                    continue
                self.amount_paid += payment
                if self.amount_paid < self.transaction_total:
                    print(f"Insufficient funds. You still owe ${self.transaction_total - self.amount_paid:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

    def give_change(self):
        change = round(self.amount_paid - self.transaction_total, 2)
        if change > 0:
            print(f"Here is your change: ${change:.2f}")
        print("Transaction complete. Thank you for shopping!")

    def finalize_transaction(self):
        self.get_total()
        self.take_payment()
        self.give_change()

def main():
    kiosk = Kiosk()
    kiosk.add_item()
    kiosk.finalize_transaction()

if __name__ == "__main__":
    main()