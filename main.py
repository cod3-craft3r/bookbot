from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    # print(f"{sys.argv}")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    entire_book = get_book_text(filepath)
    word_count = get_num_words(entire_book)

    char_dict = get_char_count(entire_book)

    # print(f"{word_count} words found in the document")
    # print(f"{char_dict}")

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")

    sorted_dict = sort_dict(char_dict)

    for k,v in sorted_dict.items():
        if True == k.isalpha():
            print(f"{k}: {v}")

    print("============= END ===============")

main()
