from art import logo

print(logo)

winner ={}
highest_bid = 0
def auction(name,bid):
   global highest_bid
   winner[name] = bid
   for key in winner:
       if winner[key]>highest_bid:

           highest_bid = winner[key]


winner_name = ""




go=True
while go:
 name = input("What is your name? ").lower()
 bid = int(input("What is your bid? $"))
 REPEAT=input("there is another bidder? Y/N").lower()
 print("\n" * 20)
 auction(name,bid)
 if REPEAT == "n" or REPEAT == "no":
     go=False
     for key, value in winner.items():
         if value == highest_bid:
             winner_name = key
print(f"The winner is {winner_name} with a bid of ${highest_bid}")
