def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    # print(text.lower())
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
           
    print(char_dict)