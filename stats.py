def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_charaters(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
           
    return char_dict

def get_charaters_list(char_dict):
    dict_list = []
    for char, num in char_dict.items():
        dict_list.append({'char': char, 'num': num})

    def get_num(dictionary):
        return dictionary['num']

    dict_list.sort(key=get_num, reverse=True)
    return dict_list
