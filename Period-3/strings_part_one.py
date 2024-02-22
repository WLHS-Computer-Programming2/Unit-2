<<<<<<< HEAD
'''
Name: Mr. Smith
Date: 2/13/2024
Class: Period 3
Description: Covering f-strings, functions with default parameters,
string indexing, string slicing, as well as if __name__
'''


def main():
    print("Hello Mr. Smith")

print("Hi")

if __name__ == '__main__':
=======
'''
Name: Mr. Smith
Date: 2/13/2024
Class: Period 3
Description: Covering f-strings, functions with default parameters,
string indexing, string slicing, as well as if __name__
'''

def slicing_demo(name):
    # suppose name = M  r  .       S  m  i  t  h
    #                0  1  2   3   4  5  6  7  8
    #               -9  -8 -7 -6  -5 -4 -3 -2 -1
    # reverse a string
    # [start:stop:step]
    # starts at start and go up to but not including stop
    # if start or stop is blank, it means include the beginning
    # and end chars
    print(name[ : :-1])
    print(name[ : : 1])
    print(name[ : : 2])

    # Smith
    # Starts at 4, goes through the end
    print(name[4:])

    # last character
    print(name[-1])
    print(name[len(name)-1])

    # Practice in CodeHS with Sandwich Sandwiches
    # in Indexing and 
    # If You're Not First, You're Last
    # and replace a letter, both parts, in Slicing

# more functions

def salutations(name:str,title:str="boring",rank:str="the first")->None:
    print(f"Hello {name} the {title} {rank}")

def main():
    name = "Mr. Smith"
    #slicing_demo(name)
    salutations(name,"mad")

if __name__ == '__main__':
>>>>>>> 787e6d570c479a9f42ba4c3da84d9b27cad7dfc6
    main()