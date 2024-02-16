def main():
    cat_name = "Diamond"
    # cat_name[0] = "d" strings are immutable, cannot assign a character
    # cat_name = "d"+cat_name[1:]
    # print(cat_name)
    list_of_numbers = "1323489734"
    num_evens = 0
    # non-pythonic way
    for i in range(0,len(list_of_numbers),2):
        print(list_of_numbers[i])
    num_evens = 0
    # pythonic way
    for number in list_of_numbers:
        if int(number) % 2 == 0:
            num_evens += 1
    print(num_evens)


if __name__ == "__main__":
    main()
