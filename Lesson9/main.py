class BankAccount:
    __num_transactions = 0 # class variable

    def __init__(self,name,number,balance):
        self.name = name
        self._number = number # please don't change
        self.__balance = balance # hidden, can't change
    
    # getter method
    def get_balance(self):
        return f"${self.__balance:.2f}"
    
    def get_num_transactions():
        return BankAccount.__num_transactions

    # setter method

    def set_balance(self,amount):
        if amount>self.__balance:
            self.__balance = amount
            BankAccount.__num_transactions += 1

my_account = BankAccount("Brandon",1234,50)
my_account._number = 12345
print(my_account.get_balance())
print(BankAccount.get_num_transactions())
my_account.set_balance(100)
print(my_account.get_balance())
print(BankAccount.get_num_transactions())
