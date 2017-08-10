import re
from pathlib import Path
from collections import Counter

TOP_COUNT = 10


def load_data(filepath):
    with open(filepath, 'r') as file:
        text_data = file.read()
    return text_data


def get_most_frequent_words(text_data):
    list_of_words = re.findall('[^\W_]+', text_data, re.UNICODE)

    return Counter(list_of_words).most_common(TOP_COUNT)


def is_txt_file(str_input):
    if not str_input:
        return False
    elif Path(str_input).is_file() and str_input.lower().endswith('.txt'):
        return True
    else:
        print('Please, verify the path and filename')
        return False

if __name__ == '__main__':
    path_to_file = None

    while not is_txt_file(path_to_file):
        path_to_file = input('Input the path and (or) filename of a text file: ')

    text_data_from_file = load_data(path_to_file).lower()

    top_ten_words = get_most_frequent_words(text_data_from_file)

    print('\n10 most frequent words in the file \'{}\':'.format(path_to_file))
    for word in top_ten_words:
        print('{}\t{}'.format(word[0], word[1]))
