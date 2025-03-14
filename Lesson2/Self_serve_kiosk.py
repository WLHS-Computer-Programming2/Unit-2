class Kiosk:
    """Creates a class called Kiosk
    """
    def __init__(self)->None:
        """sets the instances to a value of zero and empty dictionary
        """
        self.total_items = 0
        self.transaction_total = 0.0
        self.items = {}
        self.amount_paid = 0.0

    def add_item(self)->None:
        """Lets a user add an item and set the price of that item. Adds to the total items and transaction and items dictionary.
        """
        while True:
            item_name = input("Enter the item name (or type 'Done' to finish): ")
            item_name = item_name.title()
            if item_name == "Done":
                break
            while True:
                try:
                    price = float(input(f"Enter the price for {item_name}: "))
                    if price < 0:
                        print("Price cannot be negative. Please enter a positive price.")
                        continue
                    price = round(price, 2)
                    self.items[item_name] = price
                    self.total_items += 1
                    self.transaction_total += price
                    break
                except ValueError:
                    print("Invalid price. Please enter a number.")

    def get_total(self)->None:
        """Prints the total items and transaction.
        """
        print(f"Total items: {self.total_items}, Total cost: ${self.transaction_total:.2f}")

    def take_payment(self)->None:
        """Takes the user payment. If not enough, tells you its not and you have to add on to the amount that you put in to get to the total transaction.
        """
        while self.amount_paid < self.transaction_total:
            try:
                payment = float(input(f"This kiosk only accepts cash. You still owe ${self.transaction_total - self.amount_paid:.2f}. Enter payment amount: "))
                if payment < 0:
                    print("Payment cannot be negative. Please enter a positive amount.")
                    continue
                self.amount_paid += payment
                if self.amount_paid < self.transaction_total:
                    print(f"Not enough funds. You still owe ${self.transaction_total - self.amount_paid:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def give_change(self):
        """Gives you your change.
        """
        change = round(self.amount_paid - self.transaction_total, 2)
        if change > 0:
            print(f"Here is your change: ${change:.2f}")
        print("Transaction complete. Thank you for shopping!")

    def finalize_transaction(self):
        """Runs all the stuff related to the transaction.
        """
        self.get_total()
        self.take_payment()
        self.give_change()

def main():
    """Runs the class and how its suppose to run.
    """
    kiosk = Kiosk()
    kiosk.add_item()
    kiosk.finalize_transaction()

if __name__ == "__main__":
    main()