import art
import random
import game_data
a=random.choice(game_data.data)
b=random.choice(game_data.data)
while b == a:
    b = random.choice(game_data.data)
ac=a['name'] + " "+a['description']+ " " +a['country']
cb=b['name'] + " "+b['description']+ " " +b['country']
def highlow(a, b, ca, cb):
 score=0
 play=True
 while play:
  print(art.logo)
  print(f"Compare A: {ca}")
  print(art.vs)
  print(f"Against B: {cb}")
  answer = input("Who has more followers?A/B ").upper()
  if answer == "A":
    if a['follower_count'] > b['follower_count']:
        score+=1
        print(f"\n" * 20)

        print(f"You're Right!")
        a=b
        b=random.choice(game_data.data)
        ca = a['name'] + " " + a['description'] + " " + a['country']
        cb = b['name'] + " " + b['description'] + " " + b['country']
        print(f"your score is {score}")
    elif a['follower_count'] < b['follower_count']:
        print(f"\n"*20)
        print(art.logo)
        print(f"You're Wrong!")
        print("your score is",score)
        play=False
  elif answer == "B":
    if b['follower_count'] > a['follower_count']:
      score += 1
      print(f"\n" * 20)
      
      print(f"You're Right!")
      a= b
      b = random.choice(game_data.data)
      ca = a['name'] + " " + a['description'] + " " + a['country']
      cb = b['name'] + " " + b['description'] + " " + b['country']
      print(f"your score is {score}")
    elif b['follower_count'] < a['follower_count']:
      print(f"\n"*20)
      print(art.logo)
      print(f"You're Wrong!")
      print("your score is",score)
      play=False
  else:
      print(f"\n"*20)
      print(art.logo)
      print(f"You're Wrong!")
      print("your score is",score)
      play=False
playagain=True
while playagain:
 highlow(a,b,ac,cb)
 ask=input("Would you like to play again? (y/n): ").lower()
 if ask == "n":
     playagain=False
