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
choices = [rock, paper, scissors]
inp=int(input("enter 0 for rock, 1 for paper, 2 for scissors: "))
if inp==0:
    print("YOU CHOSE ROCK")
    print(rock)
    comp_choice=random.choice(choices)
    if comp_choice==choices[inp]:
        print("COMP CHOSE ROCK")
        print(rock)
        print("DRAW")
    elif comp_choice==choices[1]:
        print("COMP CHOSE PAPER")
        print(paper)
        print("YOU LOSE")
    elif comp_choice==choices[2]:
        print("COMP CHOSE SCISSORS")
        print(scissors)
        print("YOU WIN")
elif inp==1:
    print("YOU CHOSE PAPER")
    print(paper)
    comp_choice=random.choice(choices)
    if comp_choice==choices[inp]:
        print("COMP CHOSE PAPER")
        print(paper)
        print("DRAW")
    elif comp_choice==choices[0]:
        print("COMP CHOSE ROCK")
        print(rock)
        print("YOU WIN")
    elif comp_choice==choices[2]:
        print("COMP CHOSE SCISSORS")
        print(scissors)
        print("YOU LOSE")
elif inp==2:
    print("YOU CHOSE SCISSORS")
    print(scissors)
    comp_choice=random.choice(choices)
    if comp_choice==choices[inp]:
        print("COMP CHOSE SCISSORS")
        print(scissors)
        print("DRAW")
    elif comp_choice==choices[0]:
        print("COMP CHOSE ROCK")
        print(rock)
        print("YOU LOSE")
    elif comp_choice==choices[1]:
        print("COMP CHOSE PAPER")
        print(paper)
        print("YOU WIN")
else:
    print("YOU LOST CAUSE YOU CANT EVEN PICK A NUMBER I ASKED YOU TO PICK.BRUH!!")
        print(r'''    
                     _____
                   (((\\\\\\
                    )_ \\\\|
                   / \\\\|\\/
                  \\\\( ), &
                   \\) (  ((
                    |` \\\\ ))) _
                    |   \\` __|  `
                    |  , \\ ` ,    \\
                    | \\  ,\\      , \\
                    '  \\/  \\_ \\/    \\
                    `_,`-._   `      \\
                   /       `-. _ \\    `
                  /   ,\`.               \\
            ===  /   '== =\`.            | ====
                /    |   === `  /      /=========
               /     |         /     ,
              /______|        /    ,  ========
         __-'    | =  ===    /   ,=======
        '   -  --           (   
                             \\   \\
                              \\   `
                               \\    `
                                \\     `
                                 \\_____ \\
                                  /  `
                                _/  /
                               '--
                                ''')

