"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
WORDS = []


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    data = read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            find_anagrams(s)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        data = []
        for line in f:
            data.append(line.replace('\n', ''))
    return data


def find_anagrams(s):
    """
    :param s: str
    :return:
    """

    lst = list(s)
    helper(lst, [], len(s))


def helper(lst, current_lst, ans_len):
    target = ''.join(lst)
    data = read_dictionary()
    if len(current_lst) == ans_len:
        word = ''.join(current_lst)
        if word in data:
            if word not in WORDS:
                if sorted(target) == sorted(word):
                    print('Searching...')
                    print('Found: ' + word)
                    WORDS.append(word)
    else:
        for ele in lst:
            # Choose
            current_lst.append(ele)
            # Explore
            helper(lst, current_lst, ans_len)
            # Un-choose
            current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str, the vocabulary we are gomung to search
    :return: boolean, return whether the dic has the word starts from sub_s
    """
    for word in dic:
        if word.startswith(sub_s):
            return True



if __name__ == '__main__':
    main()
