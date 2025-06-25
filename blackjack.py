import random
import bjart
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)
your_hand=[]
def black():
    for i in range(2):
        a = random.randint(1, 11)
        your_hand.append(a)
    print(f"Your cards: {your_hand}, current score: {sum(your_hand)}")
    computer_hand=[]
    ch=random.randint(1,11)
    computer_hand.append(ch)
    print(f"Computer cards: {computer_hand}, current score: {sum(computer_hand)}")
    hitt = True
    while hitt:
     hit=input("Press 'Y' to get another hand, 'N' to quit").lower()

     if hit == 'y':
        your_hand.append(random.randint(1,11))
        print(f"Your cards: {your_hand}, current score: {sum(your_hand)}")
        print(f"computers first hand: {ch}")
        computer_hand.append(random.randint(1,11))
        if sum(your_hand) > 21:
            print("You lose😭")
            hitt=False
     else:
       if  sum(your_hand) < 17:
           print("you have to pick a card as your score is below 17")
           hitt=False
           print(f"YOU LOSE😭")
           break
       print(f"Your cards: {your_hand}, current score: {sum(your_hand)}")

       while not sum(computer_hand) > 17:
             computer_hand.append(random.randint(1, 11))

       print(f"Computer cards: {computer_hand}, current score: {sum(computer_hand)}")
       if sum(computer_hand) > 21:

             print("You win😁")
       elif sum(your_hand) > 21:

             print("You lose😭")
       elif sum(computer_hand) > sum(your_hand) and sum(computer_hand) <= 21:

             print("You Lose😭")
       elif sum(your_hand) > sum(computer_hand) and sum(your_hand) <= 21:


             print("You Win😁")
       elif sum(your_hand) == sum(computer_hand):
           print("DRAW🙃")
       hitt=False
b=True
while b:
    play=input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if play == 'y':
        black()
    elif play == 'n':
        b=False
