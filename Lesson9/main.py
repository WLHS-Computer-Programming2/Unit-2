class BankAccount:
    __num_transaction = 0
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def get_num_transaction(self):
        return BankAccount.__num_transaction
    
    def set_balance(self,amount):
        if amount > self.__balance:
            self.__balance = amount
            BankAccount.__num_transaction += 1
    
my_account = BankAccount("Brandon", 1234,50)
print(my_account.get_balance())
print(my_account.get_num_transaction())
my_account.set_balance(100)
print(my_account.get_balance())
print(my_account.get_num_transaction())