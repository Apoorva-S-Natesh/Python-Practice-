" " "The game Rock paper scissors is played with computer.The player gives their choice in terms of 0,1,2 for rock paper and scissors. The computer then makes its choice and the winner is declared " " "
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#take input from player and store it as player's option  
#randomize the computer option
#compare the player option and computer option and declare the winner.
#The ASCII art is stored as list to make it easrir to print and comapre.
game_gif=[rock,paper,scissors]
#converting player choice to integer.
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors: "))
print(game_gif[player_choice])
#randint() function is used to randomise the computer choice.
computer_choice=random.randint(0,2)
#using the computer choice as index for prnting the gif.
print("Computer Choice " + game_gif[computer_choice])

#conditions which needs to be satisfied for winning or losing
if player_choice >= 3 or player_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif player_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and player_choice == 2:
  print("You lose")
  # when computer is 2(rock),player choice is 1(paper) | computer choice is 1(paper) and player choice is 0(rock)
elif computer_choice > player__choice:
  print("You lose")
elif player_choice > computer_choice:
  print("You win!")
elif computer_choice == player_choice:
  print("It's a draw")
