names_string = input("Please give me everybody's names, seperated by a comma.\t")
names_list = names_string.split(",")
import random

maximum = len(names_list) - 1
random_number = random.randint(0,maximum)
bill_payer = names_list[random_number]
print(f"{bill_payer} is paying the bill")
