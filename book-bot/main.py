from stats import count_word
from stats import count_char

def get_book_text(fp: str) -> str: 
    with open(fp) as f:
        return f.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    count_word(book_text)
    for key, val in count_char(book_text).items():
        print(f"'{key}': {val}")

main()