class Kiosk():
    def __init__(self,transaction_total: int = 0, total_items: int = 0,)-> None:
        self.total_items = total_items
        self.transaction_total = transaction_total
        self.item_name = None
        self.price = None
        self.t_p = None

    def getTotal(self)-> None:
        print(f"Your total transaction cost: ${self.transaction_total}. The amount of items selected is: {self.total_items}")
        # use transaction total and total items and print, calculate and display the totals of the two.

    def addItem(self)-> None:
        while True:
            self.item_name = input("Enter in your selected item. If done with checkout, enter in -> (Done): ")
            self.item_name = self.item_name.title()
            if self.item_name == "Done":
                print("You will now be transfered to the payment method.")
                break
            else:
                self.total_items += 1
                continue 
        self.price = input(float("Enter in the associated price of the item."))
        self.price = round(self.price,2)
        self.transaction_total += self.price

        #add price to total transcation.
        #Take the item and store it in a dictionary. Add to total items
        #add an interactive input/str that makes the user 
        #either add and item or be done and exit to the payment area

    def takePayment(self)-> None:
        while True:
            self.t_p = input(float("This Kiosk only takes cash. How much will you be paying with today: "))
            if self.t_p < self.transaction_total:
                print("Please enter in an amount that equals or exceeds the total transaction amount.")
                continue
            else:
                break

        # check it they are using cash and take thier payment, it payment isn't enough or 
        #equal to the total transaction, ask for more cash.

    def giveChange(self)-> int:
        if self.t_p > self.transaction_total:
            change = self.t_p - self.transaction_total
            print(f"Here is your change of ${change}.")
            return change
        else:
            print(f"The amount seleceted meets the required payment amount: {self.transaction_total}")
        #if payment went over the required amount then give change, calculate from takepayment and totalt transaction

    def finializeTransaction(self)-> str:
        print(f"Your total amount of items {self.total_items}, the cost of all those items is {self.transaction_total}.")
        check = input("Are you done with your purchase today(Answer with Yes or No): ")
        check = check.title()
        if check == "Yes":
            return "Yes"
        if check == "No":
            print("What would you like to add.") # loop back to addItems
        #print Total the items and cost, trigger the take payment method, check done

def main():
    while True:
        addItem()
        takePayment()
        giveChange()
        finializeTransaction() # loop back it they decide that they aren't done with their purchases
    getTotal()

    # go through all the methods in the class and run them through the main function. One user, like a check out stand. 

if __name__ == '__main__':
    main()
