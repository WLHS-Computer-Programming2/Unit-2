def main():
    cat_name = "Diamond"
    # cat_name[0] = "d" strings are immutable, cannot assign a character
    # cat_name = "d"+cat_name[1:]
    # print(cat_name)
    list_of_numbers = "1323489734"
    num_evens = 0
    # non-pythonic way
    for i in range(len(list_of_numbers)):
        if int(list_of_numbers[i]) % 2 == 0:
            num_evens += 1
    print(num_evens)
    num_evens = 0
    # pythonic way
    for number in list_of_numbers:
        if int(number) % 2 == 0:
            num_evens += 1
    print(num_evens)

    # printing every other item
    for i in range(0,len(list_of_numbers),2):
        print(num_evens)

    # write a function called vowel_counter that will 
    # go through an arbitrary string parameter and 
    # count how many vowels (AEIOU or aeiou) are in it
    # This count will be returned, not printed

if __name__ == "__main__":
    main()
