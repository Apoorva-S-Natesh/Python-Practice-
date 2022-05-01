#welcome message
print("Welcome to the Love Calculator!")

#get 2 names
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#first convert the names to lower case using lower() function 
name1.lower()
name2.lower()

#count each of the alphabet T,R,U,E if they are present in either of the names using count() function
combined=name1 + name2

t=combined.count("t")
r=combined.count("r")
u=combined.count("u")
e=combined.count("e")

total_true=t+r+u+e

l=combined.count("l")
o=combined.count("o")
v=combined.count("v")


total_love=l + o + v + e

#concatenate the two sum numbers by converting them to string
score=int(str(total_true)+str(total_love))

#check for the scores to which condition they fall under
if (score<10) or (score>90) :
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>=40) and (score<=50) :
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
