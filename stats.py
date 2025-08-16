def get_num_words(entire_book):
    # entire_book = get_book_text(filepath)

    word_list = entire_book.split()
    return len(word_list)

def get_char_count(entire_book):
    # word_list = entire_book.split()
    big_dict = {}

    for char in entire_book:
        char = char.lower()
        if char in big_dict:
            big_dict[char] += 1
        else:
            big_dict[char] = 1
    return big_dict

def sort_dict(big_dict):
    sorted_items = sorted(big_dict.items(), reverse=True, key=lambda x: x[1])
    sorted_dict = dict(sorted_items)

    return sorted_dict

