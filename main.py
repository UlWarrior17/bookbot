from stats import get_num_words, char_count


def main():
    path = "books/frankenstein.txt"
    result = get_book_text(path)

    num_words = get_num_words(result)
    print(f"Found {num_words} total words")
    char_count(result)
    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

      

main()
