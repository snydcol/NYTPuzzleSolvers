import math
import requests

#usage: python3 -l <letterList>

def load_todays_letters():
	"""Function sends an HTTP request to get current puzzle input"""
	response = requests.get('https://letterboxedsolverbe.web.app/fetchLetterBoxedSides')
	if response.status_code == 200:
		return response.json()['sides'].replace(" ","")
	else:
		return requests.HTTPError

def is_valid_word(word, letter_list):
	"""Function returns """
	prev_side = -1
	for letter in word:

		#Find the position of the current letter in letterList
		letter_position = letter_list.rfind(letter)

		#Splits letterList into 4 sections, representing the 4 sides
		letter_side = math.floor(letter_position/3)
		#Letter not found
		if letter_position == -1:
			return False
		#Letter was found in list but is on the same side as previous letter
		if letter_side == prev_side:
			return False
		
		prev_side = letter_side
	return True

def one_word_solutions(word_list, letter_list):
	"""Function returns all possible one word solutions to LetterBoxed."""
	valid_solutions =[]
	for word in word_list:
		if set(word) == set(letter_list):
			valid_solutions.append(word)
	return valid_solutions

def two_word_solutions(word_list, letter_list):
	"""Function returns all possible two word solutions to LetterBoxed."""
	valid_solutions =[]

	for word in word_list:
		matches = [w for w in word_list if w[0] == word[-1] and w!= word]
		for match in matches:
			if(set(word+match) == set(letter_list)):
				valid_solutions.append([word, match])
	return valid_solutions

def main():

	letter_list = load_todays_letters()

	letter_list = letter_list.strip().lower()
	valid_words = []

	#Open the file and add all valid words to list
	with open("words_alpha.txt", encoding="ascii") as file:
		for word in file:
			word = word.strip().lower()
			if is_valid_word(word, letter_list):
				valid_words.append(word)

	print("# of Possible words: ", len(valid_words))
	print(one_word_solutions(valid_words, letter_list))
	print(two_word_solutions(valid_words, letter_list))

if __name__ == "__main__":
   main()