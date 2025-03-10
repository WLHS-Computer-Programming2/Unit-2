class Kiosk():
    transaction_total = 0
    total_items = 0

    def __init__(self,item_name: str)-> None:
        self.item_name = item_name

    def getTotal(self)-> None:
        pass # use transaction total and total items and print/calculate the totals of the two.

    def addItem(self)-> None:
        while True:
            item_name = input("Enter in your selected item. If done with checkout, enter in -> (Done): ")
            item_name = item_name.title()
            if item_name == "Done":
                print("You will now be transfered to the payment method.")
                break
            else:
                total_items += 1
                continue 
        price = input(float("Enter in the associated price of the item."))
        price = round(price,2)
        transaction_total += price

        #add price to total transcation.
        #Take the item and store it in a dictionary. Add to total items
        #add an interactive input/str that makes the user 
        #either add and item or be done and exit to the payment area

    def takePayment(self)-> None:
        while True:
            t_p = input(float("This Kiosk only takes cash. How much will you be paying with today: "))
            if t_p < transaction_total:
                print("Please enter in an amount that equals or exceeds the total transaction amount.")
                continue
            else:
                break

        # check it they are using cash and take thier payment, it payment isn't enough or 
        #equal to the total transaction, ask for more cash.

    def giveChange(self)-> None:
        if t_p > transaction_total:
            change = t_p - transaction_total
        else:
            pass
        #if payment went over the required amount then give change, calculate from takepayment and totalt transaction

    def finializeTransaction(self)-> None:
        print(f"Your total amount of items {total_items}, the cost of all those items is {transaction_total}.")
        check = input("Are you done with your purchase today(Answer with Yes or No): ")
        check = check.title()
        if check == "Yes":
            pass
        if check == "No":
            print(What would you like to add.) # loop back to addItems
        #print Total the items and cost, trigger the take payment method, check done

def main():
    pass

if __name__ == '__main__':
    main()
