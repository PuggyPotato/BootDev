def count_word(text: str) -> None:
    words = text.split()
    print(f"Found {len(words)} total words")

def count_char(text: str) -> dict[str, int]:
    count_dict = {}
    for val in text.lower():
        if val in count_dict:
            count_dict[val] += 1
        else:
            count_dict[val] = 1
    return count_dict

