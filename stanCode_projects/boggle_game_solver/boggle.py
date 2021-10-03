"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

boggle_dic = {}
dic = []
words = []


def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	read_dictionary()
	get_boggle()
	found_words()
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			vocab = line[:line.find('\n')]
			dic.append(vocab)
		# print(dic)


def get_boggle():
	"""
	get the str from user
	"""
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		if len(row) != 7:
			print('Illegal format')
		else:
			if row[0].isalpha() and row[2].isalpha() and row[4].isalpha() and row[6].isalpha() \
					and row[1] == ' ' and row[3] == ' ' and row[5] == ' ':
				pass
			else:
				print('Illegal format')
				return False
		boggle_dic[i] = row.lower().split(' ')
		# print(boggle_dic[i])


def found_words():
	for i in range(len(boggle_dic)):
		for j in range(boggle_dic[i]):
			words.append(i, j)
			# found_words_helper()
	if words in boggle_dic:
		return words

# def found_words_helper():



def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if len(sub_s) == 2:
		if sub_s[0:2] in dic:
			for vocab in dic[sub_s[0:2]]:
				if vocab.startswith(sub_s):
					return True
			return False
	else:
		if sub_s[0:3] in dic:
			for vocab in dic[sub_s[0:3]]:
				if vocab.startswith(sub_s):
					return True
			return False


if __name__ == '__main__':
	main()
