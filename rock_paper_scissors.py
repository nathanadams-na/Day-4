import random
#from random import choice
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_choice = int(input("Please type 0 for Rock, 1 for Paper or 2 for Scissors \t"))
if user_choice > 2 or user_choice < 0:
    print("Invalid input.")
else:
    r_p_s = [rock, paper, scissors]
    #computer_choice = random.randint(0, 2)
    computer_choice = random.choice(r_p_s)
    user_rps = r_p_s[user_choice]
    print(user_rps)
    print("The computer chose:")
    print(computer_choice)
    if user_rps == computer_choice:
        print("It was a tie!")
    elif user_rps == rock:
        if computer_choice == scissors:
            print("You Win!")
        else:
            print("You Lose!")
    elif user_rps == paper:
        if computer_choice == rock:
            print("You Win!")
        else:
            print("You Lose!")
    else:
        if computer_choice == paper:
            print("You Win!")
        else:
            print("You Lose!")