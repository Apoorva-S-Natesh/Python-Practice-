#import modules
import random
from hangman_words import word_list
from hangman_art import stages,logo
#import clear so that the console is clean every time
from replit import clear

#choose a random word from the list of words
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(logo)

#Create blanks
#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for _ in range(word_length):
    display += "_"
    
letter_repo=""
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in letter_repo:
        print(f"you have Already guessed this letter {guess}")
    
    #Check guessed letter
    #Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that             position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p",         "_", "_"].
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
            
    if guess not in chosen_word:
    #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter {guess} is not in the word and you lose a life")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
