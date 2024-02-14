'''
Name: Mr. Smith
Date: 2/14/2024
Class: Period 8
Description: Covering f-strings, functions with default parameters,           f       
string indexing, string slicing, as well as if __name__
'''

def slicing_demo(string):
    # access last character
    print(string[-1])
    print(string[len(string)-1])
    # slicing
    # string[start : stop : step], stop is not included
    print(string[0:3]) # step not specified means default 1
    print(string[4:9]) # Method 1 to get Smith
    print(string[4:])  # Method 2 to get Smith - if stop blank, 
    #                    goes through end of string
    print(string[0:len(string):2]) # every other letter starting at M
    print(string[ : :2]) # every other letter starting at M
    print(string[]) # get Smith using negative indices

def main():
    # name = M  r  .     S  m  i  t  h
    #        0  1  2  3  4  5  6  7  8
    #       -9 -8 -7 -6 -5 -4 -3 -2 -1
    name = "Mr. Smith"
    slicing_demo(name)

if __name__ == "__main__":
    main()
