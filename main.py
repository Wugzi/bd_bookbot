import stats
import sys

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
    
def print_book_report(path_to_file: str, word_count: int, char_count: list) -> str:
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char, count in char_count:
        if str.isalpha(char):
            print(f"{char}: {count}")
    print(f"============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    book_text = get_book_text(book_file)
    print_book_report(book_file, stats.get_word_count(book_text), stats.chars_dict_to_sorted_list(stats.get_unique_char_count(book_text)))

main()