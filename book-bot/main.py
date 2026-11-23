from stats import count_word
from stats import count_char
from stats import chars_dict_to_sorted_list

def get_book_text(fp: str) -> str: 
    with open(fp) as f:
        return f.read()

def main():
    path = "./books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = count_word(book_text)
    sorted_list = chars_dict_to_sorted_list(count_char(book_text))
    print_report(path, word_count, sorted_list)

def print_report(path: str, word_count: int, sorted_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for val in sorted_list:
        if val[0].isalpha():
            print(f"{val[0]}: {val[1]}")
    print("============= END ===============")

    
main()