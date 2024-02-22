def vowel_counter(string:str)->int:
    """Return the number of vowels in a string
    Parameter
    ---------
    string:str the input string
    
    Return
    -------
    int: number of vowels"""
    vowels = 'aeiou'
    vowel_count = 0
    for char in string.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    # assert vowel_counter("") == 0
    # assert vowel_counter("Rhythm") == 0
    # assert vowel_counter("aeiouAEIOU") == 10
    # assert vowel_counter("Hello World") == 3
    # assert vowel_counter("Python!@# is awesome.") == 6
    # assert vowel_counter("HELLo WoRLd") == 3
    # print("All tests passed!")

    cat_name = "Diamond"
    cat_name.lower()
    print(cat_name) # stays Diamond
    cat_name = cat_name.lower()
    print(cat_name) # it is now lowercase

    # common string methods
    new_cat = "applejack"
    print(new_cat.capitalize()) #Applejack
    print(new_cat.center(20,"-")) # -----applejack------
    print(new_cat.count("p")) # 2
    print(new_cat.find("jack")) # 5, can be used for chars
    print(new_cat.replace("apple","cracker")) #crackerjack
    new_cat = new_cat.capitalize() # Applejack
    print(new_cat.swapcase()) #aPPLEJACK
    new_cat = "     Applejack                 "
    new_cat = new_cat.strip() # Applejack
    print(new_cat.upper())
    print(new_cat.lower())
    user_input = "5a"
    print(user_input.isalnum())
    print(user_input.isalpha())
    print(user_input.isdigit())


if __name__ == "__main__":
    main()