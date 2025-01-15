import random 

a=random.randint(1,100)

attempts=0

print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100. Try to guess it!")
# print("You have 10 attempts!!")

while attempts>=0:
    b=int(input("Enter your guess: "))
    attempts+=1
    
    if b < a:
        print("Too low! Try again.")
    elif b > a:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {a} in {attempts} attempts.")
        break

