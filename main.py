from stats import get_num_words, get_num_charaters, get_charaters_list


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_count_dict = get_num_charaters(text)
    char_count_list = get_charaters_list(char_count_dict)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char_dict in char_count_list:
        if char_dict['char'].isalpha():
            print(f'{char_dict['char']}: {char_dict['num']}')
    print('============= END ===============')

    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

      

main()
