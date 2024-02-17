def vowel_counter(string:str)->int:
    """Counts the number of vowels, aeiou, in
    a given string. Case insensitive
    
    Parameter
    ---------
    string:str input string to count vowels in
    
    Return
    ------
    int: number of vowels
    """
    vowel_count = 0
    for letter in string:
        if letter.lower() in "aeiou":
            vowel_count += 1
    return vowel_count

def main():
    # cat_name = "Diamond"
    # # cat_name[0] = "d" strings are immutable, cannot assign a character
    # # cat_name = "d"+cat_name[1:]
    # # print(cat_name)
    # list_of_numbers = "1323489734"
    # num_evens = 0
    # # non-pythonic way
    # for i in range(len(list_of_numbers)):
    #     if int(list_of_numbers[i]) % 2 == 0:
    #         num_evens += 1
    # print(num_evens)
    # num_evens = 0
    # # pythonic way
    # for number in list_of_numbers:
    #     if int(number) % 2 == 0:
    #         num_evens += 1
    # print(num_evens)

    # # printing every other item
    # for i in range(0,len(list_of_numbers),2):
    #     print(num_evens)

    # write a function called vowel_counter that will 
    # go through an arbitrary string parameter and 
    # count how many vowels (AEIOU or aeiou) are in it
    # This count will be returned, not printed
    # try:
    #     assert vowel_counter("") == 0
    #     assert vowel_counter("Rhythm") == 0
    #     assert vowel_counter("AEIOUaeiou") == 10
    # except AssertionError:
    #     print("Test failed")
    cat_name = "Diamond"
    cat_sentence = f"{cat_name} is one of six foster kittens."
    print(cat_sentence.upper())
    print(cat_sentence.title())
    print(cat_sentence.capitalize())
    print(cat_name.center(31,"*"))
    print(cat_sentence.count("o"))
    print(cat_sentence.count("foster"))
    cat_sentence = cat_sentence.replace("six","seven")
    print(cat_sentence)
    sentence = "The grey cat is in a grey box."
    sentence = sentence.replace("grey","orange",1)
    print(sentence)
    cat_name = "        Applejack                     "
    cat_name = cat_name.strip()
    print(cat_name)
    user_input = "5a-"
    print(user_input.isdigit())
    print(user_input.isalpha())
    print(user_input.isalnum())
    

    


if __name__ == "__main__":
    main()
