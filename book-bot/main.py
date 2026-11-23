def get_book_text(fp: str) -> None: 
    with open(fp) as f:
        print(f.read())

def main():
    get_book_text("./books/frankenstein.txt")

main()