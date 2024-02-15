def vowel_counter(string:str)->int:
    """Return the number of vowels in a string
    Parameter
    ---------
    string:str the input string
    
    Return
    -------
    int: number of vowels"""

def main():
    assert count_vowels("") == 0
    assert count_vowels("Rhythm") == 0
    assert count_vowels("aeiouAEIOU") == 10
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python!@# is awesome.") == 4
    assert count_vowels("HeLLo WoRLd") == 3


if __name__ == "__main__":
    main()