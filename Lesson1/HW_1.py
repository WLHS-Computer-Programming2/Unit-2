"""
Name:Duncan Staats
Date:3/6/25
Description: Unit 2 Homework 1 and 2
"""

class Restaurant():
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        """Creates a new restaurant object

        Args:
            restaurant_name (str): name of resturant
            cuisine_type (str): name of cuisine
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 


    def describe_restaurant(self)-> None:
        """Prints a description of the restaurant
        """
        print(f"This type of resturant is {self.restaurant_name}, and the cuisine served here is {self.cuisine_type}")

    def open_restaurant(self)-> None:
        """Prints that the resturant is open
        """
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number: int)-> None:
        """Sets the number of serverd customers at the restaurant
        """
        if number > 0:
            self.number_served += number
        else:
            print("Number served must be positive.")

    def increment_number_served(self, number: int)-> None:
        """Adds on the amount served with given amount
        """
        if number > 0:
            self.number_served += number
        else:
            print("Increment must be positive.")

class User():
    def __init__(self,first_name: str, last_name: str, age: int, sex: str, height: int, login_attempts:int = 0)-> None:
        """creates a new user object

        Args:
            first_name (str): first name of person
            last_name (str): last name of person
            age (int): age of person
            sex (str): birth sex of person
            height (int): height in inches of person
            login_attempts (int): login attemps of person, default 0
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.height = height
        self.login_attempts = login_attempts

    def describe_user(self)-> None:
        """Prints a description of the person
        """
        print(f"Your name is, {self.first_name} {self.last_name} and you are {self.age} years old and are a {self.sex}. Your height is {self.height} in inches.")

    def greet_user(self)-> None:
        """Prints a greating
        """
        print(f"Hello there {self.first_name} {self.last_name}. I hope you have been well and continue to be well.")

    def increment_login_attempts(self)-> None:
        """Adds 1 to the total amount of login attemps
        """
        self.login_attempts += 1

    def reset_login_attempts(self)-> None:
        """Resets the login attemps to zero
        """
        self.login_attempts = 0

def main():    
    restaurant_1 = Restaurant("Mama's Meatballs","Italian")
    restaurant_2 = Restaurant("Jonny's Wok","Chinese")
    restaurant_3 = Restaurant("Banjo's Classics","Southern American")

    user_1 = User("Duncan", "Staats", 18, "Male", 69)
    user_2 = User("Micheal", "Hawkins", 17, "Female", 60)
    user_3 = User("Hudson", "Sandler", 21, "Male", 80)

    restaurant_1.set_number_served(20)
    restaurant_2.set_number_served(40)
    restaurant_3.set_number_served(38)

    restaurant_1.increment_number_served(10)
    restaurant_2.increment_number_served(15)
    restaurant_3.increment_number_served(30)

    print(f"{restaurant_1.restaurant_name} has served {restaurant_1.number_served} customers.")
    print(f"{restaurant_2.restaurant_name} has served {restaurant_2.number_served} customers.")
    print(f"{restaurant_3.restaurant_name} has served {restaurant_3.number_served} customers.")
    print()
    print(f"The first restaurant name is {restaurant_1.restaurant_name}.")
    print(f"The first restaurant serves {restaurant_1.cuisine_type} food.")
    print()
    print(f"The second restaurant name is {restaurant_2.restaurant_name}.")
    print(f"The second restaurant serves {restaurant_2.cuisine_type} food.")
    print()
    print(f"The third restaurant name is {restaurant_3.restaurant_name}.")
    print(f"The third restaurant serves {restaurant_3.cuisine_type} food.")
    print()
    restaurant_1.describe_restaurant()
    restaurant_1.open_restaurant()
    print()
    restaurant_2.describe_restaurant()
    restaurant_2.open_restaurant()
    print()
    restaurant_3.describe_restaurant()
    restaurant_3.open_restaurant()
    print()
    user_1.describe_user()
    user_1.greet_user()
    print()
    user_2.describe_user()
    user_2.greet_user()
    print()
    user_3.describe_user()
    user_3.greet_user()
    print()
    print("Testing User login attempts:")
    print()
    user_1.increment_login_attempts()
    user_1.increment_login_attempts()
    user_1.increment_login_attempts()
    print(f"{user_1.first_name}'s login attempts: {user_1.login_attempts}")
    user_1.reset_login_attempts()
    print(f"{user_1.first_name}'s login attempts after reset: {user_1.login_attempts}")
    print()
    user_2.increment_login_attempts()
    user_2.increment_login_attempts()
    print(f"{user_2.first_name}'s login attempts: {user_2.login_attempts}")
    user_2.reset_login_attempts()
    print(f"{user_2.first_name}'s login attempts after reset: {user_2.login_attempts}")
    print()
    user_3.increment_login_attempts()
    user_3.increment_login_attempts()
    user_3.increment_login_attempts()
    user_3.increment_login_attempts()
    print(f"{user_3.first_name}'s login attempts: {user_3.login_attempts}")
    user_3.reset_login_attempts()
    print(f"{user_3.first_name}'s login attempts after reset: {user_3.login_attempts}")

if __name__ == '__main__':
    main() 