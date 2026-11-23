def count_word(text: str) -> int:
    words = text.split()
    return len(words)

def count_char(text: str) -> dict[str, int]:
    count_dict = {}
    for val in text.lower():
        if val in count_dict:
            count_dict[val] += 1
        else:
            count_dict[val] = 1
    return count_dict

def sort_on(t: tuple[str, int]) -> int:
    return t[1]

def chars_dict_to_sorted_list(d: dict[str, int]) -> list[tuple[str, int]]:
    temp_list = list()
    for key in d:
        temp_list.append((key, d[key]))

    sorted_list = sorted(temp_list, reverse=True, key=sort_on)
    return sorted_list

