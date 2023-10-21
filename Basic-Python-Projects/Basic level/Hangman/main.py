import random
import Art
import Hangman_words

while True:
	print(Art.logo,"\n\n")

	display = []
	word_chosen = random.choice(Hangman_words.word_list)
	word_length = len(word_chosen)
	for j in range(word_length):
		display.append("_")

	count = 0
	tries = 0
	while True:
		present = 0
		print("\n",display)
		guess = input("\nGuess a letter: ").lower()
		for i in range(word_length):
			if word_chosen[i]==guess:
				display[i]=guess
				count+=1
				present = 1
		if present == 0:
			tries-=1
			if tries>=-6:
				print(Art.stages[tries])
				print(guess,"is not in word, use different letter\n")
				if 7+tries!=1:
					print("You have",7+tries,"tries left!\n")
				else:
					print("You have 1 try left\n")
			else:
				print(Art.stages[tries],"\n\nYou Lose!\nThe correct word was",word_chosen,"!\n\n")
				break
		else:
			if count==word_length:
				print("You Won!")
				break
	choice=input("Want to play again? yes or no? ")
	if choice=="yes":
		continue
	else:
		break