import string
import math
from django.core.paginator import Paginator

from .settings import BASE_DIR


def delete_punctuation(text_file):
    """Delete punctuation in text."""
    for char in string.punctuation:
        text_file = text_file.replace(char, '')
    return text_file


def split_text(text_file):
    """Convert text_file to set,
    
    and to list. 
    """
    return list(set(text_file.split()))


def processing_file(files):
    """Processing file."""
    text_file = ''
    rslt_dict = {}

    with open(f'{BASE_DIR}/{files}', "r") as file:
        text_file = file.read()

    text_file = delete_punctuation(text_file)
    test_words = split_text(text_file)
    count_words_of_file = len(text_file.split())

    for i in range(0, 51):
        try:
            tf = text_file.count(test_words[i]) / count_words_of_file
            idf = math.log10(1)
            rslt_dict[test_words[i]] = [float(f'{tf:.2f}'), idf]
        except IndexError:
            print(f'Получилось вывести только {i+1} слов.')
            return rslt_dict
    return rslt_dict
