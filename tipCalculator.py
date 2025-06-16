print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? !dont add '%'160 sign! "))
people = int(input("How many people to split the bill? "))
tip = tip/100
bill=bill+(bill*tip)
split_bill = (bill/people)
total = round(split_bill,2)
print(f"Each person should pay: ${total}" )
