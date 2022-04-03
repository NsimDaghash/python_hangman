import os

global MAX_TRIES
global num_of_tries
global old_letters_guessed

# HANGMAN_PHOTOS : a global dict that hold the stages of the game
HANGMAN_PHOTOS = {
	# the initial stage at the begining of the game
	0: """
	x------x

	""",
	# first stage :the hang pillar
	1: """
	x------x
	|
	|
	|
	|
	|
	-
	""",
	# second stage : head
	2: """
	x------x
	|      |
	|      O
	|
	|
	|
	-
	""",
	# third stage : head and torso
	3: """
	x------x
	|      |
	|      O
	|      |
	|
	|
	-
	""",
	# fourth stage : head, torso, and both arms
	4: """

	x------x
	|      |
	|      O
	|     /|\\
	|
	|
	-
	""",
	# fifth stage : head, torso, both arms, and one leg
	5: """
	x------x
	|      |
	|      O
	|     /|\\
	|     /
	|
	-
	""",
	# sixth stage : head, torso, both arms, and both legs
	6: """
	x------x
	|      |
	|      O
	|     /|\\
	|     / \\
	|
	-
	"""
}
#  ------------- end of dict ------------------


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""
	This function update the list of the guessted letters, if the returned
	value from the check_valid_input function is true otherwise it will print
	the guessed letters list .
	:param letter_guessed: the later that the player is trying to guess
	:type letter_guessed: string(text letter)
	:param old_letters_guessed: All the letters the player has guessted
	:type old_letters_guessed: list
	:return:true if the lettter in the word / false if not in the word
	:rtype:  boolian type
	"""
	if check_valid_input(letter_guessed, old_letters_guessed):
		old_letters_guessed.append(letter_guessed)
		return(True)
	else:
		os.system('COLOR b4')   # print list color white on red background
		print("\n X")
		guessed = "-> ".join(old_letters_guessed)
		print("-> ".join(sorted(old_letters_guessed)))
		return(False)
#  ------------- end of try_update_letter_guessed function ------------------


def check_valid_input(letter_guessed, old_letters_guessed):
	"""
	This function check if the input is a single English alphabet letter
	and if it wasn't guessed earlier.
	:param letter_guessed: the later that the player is trying to guess
	:type letter_guessed: string(text letter)
	:param old_letters_guessed: All the letters the player has guessted
	:type old_letters_guessed: list
	:return: true/ false
	:rtype:  boolian type
	"""
	bol = letter_guessed in old_letters_guessed   # bol: boolian variable
	if not bol:
		if(len(letter_guessed) == 1) and letter_guessed.isalpha():
			return True
		else:
			return False
	else:
		return False
#  ------------- end of check_valid_input function ------------------


def open_screen(MAX_TRIES):
	"""
	Show the logo of the game and print the maximum wrong guesses that
	can be done
	:param MAX_TRIES:maximum wrong guesses that can be done
	:type MAX_TRIES :int
	:return: none """
	print("""
	 _    _
	| |  | |
	| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
	|  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
	| |  | | (_| | | | | (_| | | | | | | (_| | | | |
	|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
			     __/ |
			    |___/
			    
		      by : Nasim Daghash
				""")
	print(MAX_TRIES)
#  ------------- end of open_screen function ------------------


def check_win(secret_word, old_letters_guessed):
	"""
	This function get the word that the player need to guess and the
	letters that he guessed , the function check if all the letters in
	the secret word guessed correctly the function will return true , else
	it will return false .
	:param secret_word: the word that the player need to guess
	:type secret_word: string
	:param old_letters_guessed: the letters that the player have guessed
	:type old_letters_guessed: list
	:return: true if the player guessed the whole word ,or false if he didn't
	:return type: boolian type
	"""
	winner = True
	for letter in secret_word:
		if letter not in old_letters_guessed:
			winner = False
	return winner
#  ------------- end of check_win function ------------------


def choose_word(file_path, index):
	"""
	This function will get a text file location, and an integer representing the
	location of a particular word in the file, and return chosen word ,with
	minimum two letters, if the index bigger than the content of the file When
	the count reaches the end of the file, it will continue in circle, until it
	reaches the index and choose the word .
	:param file_path: path of the file from which the word will be selected.
	:type file_path: string
	:param index:the location of the word in the file
	:type index: int
	:return: the word that the player should guess
	:rtype: string
	"""
	chosen_word = ""
	new_index = 0
	with open(file_path) as words:
		words = words.read()
		
	words = words.split(' ')
	#print(len(words))                  # ***********"

	if len(words) == 1 and check_legal_word(chosen_word):    # one word file
		chosen_word = words[0] 		     # it will be the choosen word
		
		
	if index > len(words):               # out of range 
		new_index = (index % len(words)) - 1
		chosen_word = words[new_index]
		while (len(chosen_word)) < 2 or not check_legal_word(chosen_word):
			new_index -= 1
			chosen_word = words[new_index]	
	else:									# in the range
		chosen_word = words[index - 1]
		while (len(chosen_word)) < 2 or not check_legal_word(chosen_word):
			index -= 1
			chosen_word = words[index - 1]

	return chosen_word
#  ------------- end of choose_word function ------------------


def check_legal_word(chosen_word):
	"""
	check if all letters of the word is alphabetcal
	:param chosen_word : the word that the player need to guess
	:type chosen_word : string
	:return : true/false
	:rtype: boolian
	"""
	for letter in chosen_word:
		if not letter.isalpha():
			return False
	return True
#  ------------- end of check_legal_word function ------------------


def show_hidden_word(secret_word, old_letters_guessed):
	"""
	The function return list of guessed letters and _ for non guessed
	:param secret_word: the word that the player need to guess
	:type secret_word: string
	:param old_letters_guessed: the letters that the player have guessed
	:type old_letters_guessed: list
	:return:word_display
	:rtype:list
	"""
	word_display = []
	for letter in secret_word:
		if letter not in old_letters_guessed:
			word_display.append("_ ")
		else:
			word_display.append(letter)
	return " ".join(word_display)
#  ------------- end of show_hidden_word function ------------------


def letter_check(letter_guessed, secret_word):
	"""
	check if the letter within the secret word
	:param letter_guessed: the later that the player is trying to guess
	:type letter_guessed: string(text letter)
	:param secret_word: the word that the player need to guess
	:type secret_word: string
	:return: True if the letter un the word or false if its not
	:rtype : boolian
	"""
	for letter in letter_guessed:
		if letter in secret_word:
			print("\n Very Good \n")
			os.system('COLOR 1F')	# white script on blue background	
			return True
		else:
			print("\n wrong letter , try another letter \n")
			os.system('COLOR F4')   # red script on white background  
			return False
#  ------------- end of letter_check function ------------------


def not_empty_file(file_path):
	"""
	this function check if the file is empty
	:param file_path:the path of the file to choose a secretword from it
	:type file_path :string
	:return : false if the file is empty / true if its not empty
	:rtype: boolian
	"""
	with open(file_path) as words:
		words = words.read()
	words = words.split(' ')
	if len(words) == 1:
		if words[0] == '':
			return False
	else:
		return True
#  ------------- end of not_empty_file function ------------------


def hangman(MAX_TRIES, secret_word, old_letters_guessed, num_of_tries):
	"""
	This function try to guess the secret word ,it will end if the player
	guess the secret word or get out of tries( 6 different wrong letters )
	:param MAX_TRIES:maximum wrong guesses that can be done
	:type MAX_TRIES :int
	:param secret_word: the word that the player need to guess
	:type secret_word: string
	:param old_letters_guessed: the letters that the player have guessed
	:type old_letters_guessed: list
	:param num_of_tries:how many time wrong letter guessed
	:type num_of_tries : int
	:return: none
	"""
	while MAX_TRIES > 0:
		print(HANGMAN_PHOTOS[int(num_of_tries)])
		print(show_hidden_word(secret_word, old_letters_guessed))
		letter_guessed = input("\n enter a letter :").lower()
		if try_update_letter_guessed(letter_guessed, old_letters_guessed):
			if not letter_check(letter_guessed, secret_word):
				MAX_TRIES -= 1
				num_of_tries += 1
			if check_win(secret_word, old_letters_guessed):
				os.system('COLOR 2f')
				print("\n The word is :", secret_word)
				print("\n You Win ")
				break
		print("\n you have ", num_of_tries, " incorret guesses of 6 ")
		if MAX_TRIES == 0:
			os.system('COLOR 4f')
			print(HANGMAN_PHOTOS[int(num_of_tries)])
			print("\n Lose\n\n")
			print(" The word is :", secret_word)
#  ------------- end of hangman function ------------------


def main():

	MAX_TRIES = 6
	num_of_tries = 0
	old_letters_guessed = []
	answer = "y"
	while answer == "y":
		os.system('COLOR 07')    # white script on black background
		open_screen(MAX_TRIES)
		file_path = input("enter the location of the text file :")
		if not os.path.isfile(file_path):        # if the file not found
			print("The file does not exist ! ! ! ")
			continue
		if not not_empty_file(file_path):			# if it's an empty file
			print("This file is empty ! ! ! ")
			continue
		index = input("enter the word index :")
		if index.isnumeric():				# check if it's a number
			index = int(index)
			secret_word = choose_word(file_path, index)
			secret_word = secret_word.lower()
			hangman(MAX_TRIES, secret_word, old_letters_guessed, num_of_tries)
		else:
			print("Not a valid index ")
		answer = input("\n for new game press :y\n to quit press :n\n").lower()

		while answer != "y":  # if the player choose another letter
			if answer == 'n':
				break
			print(" wrong letter!")
			answer = input(" to start a new game press y , to quit press n")
			answer.lower()
		os.system("cls")  # clear screen to start new game
		MAX_TRIES = 6     # reset MAX_TRIES to 6
		num_of_tries = 0  # reset number of tries to 0
		old_letters_guessed = []  # reset the list of the guessed words
	os.system('COLOR 07')         # white script on black background

if __name__ == "__main__":
	main()
