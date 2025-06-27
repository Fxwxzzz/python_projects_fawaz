import random
from gnart import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_number = random.randint(1, 100)
diff=input("enter a difficulty level 'EASY'/'HARD' : ").lower()
guess_chance=0
if diff == 'easy':
    guess_chance = 10
elif diff == 'hard':
    guess_chance = 5
else:
     print("invalid difficulty level")
     exit()
def guess(guess_chance):
 for guess in range(guess_chance):
    print(f"you have {guess_chance} guesses")
    guess_chance-=1
    g = int(input(f"Guess the number between 1 and 100: "))
    if g == chosen_number:
        print(f"You guessed the number in {guess} guesses.YOU WIN!")
        break
    elif g < chosen_number-10:
        print("Your guess is too low.")
    elif g > chosen_number+10:
        print("Your guess is too high.")
    elif g<chosen_number:
        print("Your guess is too close.")
    elif g>chosen_number:
        print("Your guess is too close.")
    if guess_chance == 0:
        print(f"You Lose!. {chosen_number} is the correct number")
play=True
while play:
      guess(guess_chance)
      play_again=input("Do you want to play again? (y/n): ").lower()
      if play_again == 'n':
          play=False
      if play_again == 'y':
          print("\n"*20)
          print(logo)
          print("Welcome to the Number Guessing Game!")
          print("I'm thinking of a number between 1 and 100.")
          chosen_number = random.randint(1, 100)
          diff = input("enter a difficulty level 'EASY'/'HARD' : ").lower()
          guess_chance = 0
          if diff == 'easy':
              guess_chance = 10
          elif diff == 'hard':
              guess_chance = 5
          else:
              print("invalid difficulty level")
              exit()
