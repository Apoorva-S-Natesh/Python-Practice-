# Who is going to pay the bill at a restaurant like a Russian Roulette
# Without using choice() method
# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")

#splitting the string to a list using split()
names = names_string.split(", ")

#Find the ength of string using len()
people=len(names)

#Randomly finding the person who should pay the bill using randint().The last item in th list will be at an index 1 less that length of the list
bill_paid=names[random.randint(0,people-1)]
print(f"{bill_paid} is going to pay for the meal today!")
