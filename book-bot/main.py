from stats import count_word
from stats import count_char
from stats import chars_dict_to_sorted_list

def get_book_text(fp: str) -> str: 
    with open(fp) as f:
        return f.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    count_word(book_text)
    sorted_list = chars_dict_to_sorted_list(count_char(book_text))
    print(sorted_list)

main()