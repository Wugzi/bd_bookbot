def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def get_unique_char_count(text: str) -> dict:
    char_count = {}
    for char in text:
        if str.lower(char) in char_count:
            char_count[str.lower(char)] += 1
        else:
            char_count[str.lower(char)] = 1
    return char_count

def sort_on(tuple: tuple) -> int:
    return tuple[1]

def chars_dict_to_sorted_list(char_count: dict) -> list:
    char_count_list = []
    for char in char_count:
        char_count_list.append((char, char_count[char]))
    return sorted(char_count_list, key=sort_on, reverse=True)
