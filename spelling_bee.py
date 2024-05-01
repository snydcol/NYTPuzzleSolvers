#usage: python3 -l <letters> -c <centerLetter>

def is_valid_word(word, letters, center_letter):
	'''Function to determine if a word is valid for the Spellingbee puzzle'''
	contains_special = False
	for letter in word:
		if letter == center_letter:
			contains_special = True
			continue
		if letter not in letters:
			return False
	return True and contains_special

def main():

	letters = input('Letters: ').lower().strip()
	center_letter = input('Center Letter: ').lower().strip()

	valid_words = []
	with open("twl06.txt", encoding="ascii") as file:
		for word in [l.lower().strip() for l in file if len(l) > 3]:
			if is_valid_word(word, letters, center_letter):
				#add word to word list
				valid_words.append(word)
	print(valid_words)


if __name__ == "__main__":
   main()
