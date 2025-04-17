
from stats import (
    get_book_text,
    get_num_words,
    get_character_frequency,
    get_list_of_char
)

def main():

    path = "books/frankenstein.txt"
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    list = get_list_of_char(text)
    for i in list:
        print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")



main()