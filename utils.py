import sys
import random

def read_file(filename):
    dictionary = {}
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            parts = line.strip().split(' : ')
            if len(parts) == 2:
                hiragana, definition = parts
                dictionary[hiragana] = definition
    return dictionary

def print_dictionary(dictionary):
    for word, definition in dictionary.items():
        print(f"{word} : {definition}")
    return


def print_home():
    print("\n")
    print("--------------------------------------------------------")
    print("                                                        ")
    print("               JP-Learner 日本語                         ")
    print("                                                        ")
    print("                made by @lettu3                         ")
    print("                   -q : quit                            ")
    print("--------------------------------------------------------")
    print("\n")
    return


def print_success():
    print("---------------------------------------------------------")
    print("/             おつかれさまでした!                        /")
    print("---------------------------------------------------------")

def get_word(dictionary):
    word = random.choice(list(dictionary.keys()))
    definition = dictionary[word]
    return word, definition

