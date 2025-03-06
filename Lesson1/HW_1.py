"""
Name:Duncan Staats
Date:3/6/25
Description: Unit 2 Homework 1 and 2
"""

class Restaurant():
    def __init__(self,restaurant_name: str, cuisine_type: str, number_served: int)-> None:
        """_summary_

        Args:
            restaurant_name (str): _description_
            cuisine_type (str): _description_
            number_served (int): _description_
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self)-> None:
        """_summary_
        """
        print(f"This type of resturant is {self.restaurant_name}, and the cuisine served here is {self.cuisine_type}")

    def open_restaurant(self)-> None:
        """_summary_
        """
        print(f"{self.restaurant_name} is open")

    def set_number_served(self)-> None:
        """_summary_
        """
        pass

    def increment_number_served(self)-> None:
        """_summary_
        """
        pass

class User():
    def __init__(self,first_name: str, last_name: str, age: int, sex: str, height: int, login_attempts:int)-> None:
        """_summary_

        Args:
            first_name (str): _description_
            last_name (str): _description_
            age (int): _description_
            sex (str): _description_
            height (int): _description_
            login_attempts (int): _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.height = height
        self.login_attempts = 0

    def describe_user(self)-> None:
        """_summary_
        """
        print(f"Your name is, {self.first_name} {self.last_name} and you are {self.age} years old and are a {self.sex}. Your height is {self.height} in inches.")

    def greet_user(self)-> None:
        """_summary_
        """
        print(f"Hello there {self.first_name} {self.last_name}. I hope you have been well and continue to be well.")

    def increment_login_attempts(self)-> None:
        """_summary_
        """
        pass

    def reset_login_attempts(self)-> None:
        """_summary_
        """
        pass


def main():
    restaurant_1 = Restaurant("Mama's Meatballs","Italian")
    restaurant_2 = Restaurant("Jonny's Wok","Chinese")
    restaurant_3 = Restaurant("Banjo's Classics","Southern American")

    user_1 = User("Duncan", "Staats", 18, "Male", 69)
    user_2 = User("Micheal", "Hawkins", 17, "Female", 60)
    user_3 = User("Hudson", "Sandler", 21, "Male", 80)

    print(f"The first restaurant name is {restaurant_1.restaurant_name}.")
    print(f"The first restaurant serves {restaurant_1.cuisine_type} food.")
    print()
    print(f"The second restaurant name is {restaurant_2.restaurant_name}.")
    print(f"The second restaurant serves {restaurant_2.cuisine_type} food.")
    print()
    print(f"The third restaurant name is {restaurant_2.restaurant_name}.")
    print(f"The third restaurant serves {restaurant_2.cuisine_type} food.")
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

if __name__ == '__main__':
    main()