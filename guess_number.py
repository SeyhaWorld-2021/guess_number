import random
import math

print("Welcome to Guess Number\n")
input("Press enter to continues\n")

print("Select your difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("-"*30)
mode = input("Enter choice (1/2/3):")


if mode == "1":
    low = 1
    high = 50
    max_attempts = 10

elif mode == "2":
    low = 1
    high = 100
    max_attempts = 5
    R = 7

elif mode == "3":
    low = 1
    high = 200
    max_attempts = 3
    R = 5

else:
    print("Invalid choice → default MEDIUM")
    low = 1
    high = 100
    max_attempts = 5
    R = 7

number = random.randint(low, high)
secret = number
attempts = 0

def hints(secret, R, min_val, max_val):
    low = max(min_val, secret - R)
    high = min(max_val, secret + R)
    return low, high

while attempts < max_attempts:
    

    print(f"hints: {hints(secret, R, low, high)}")
    guess = int(input(f"Guess the number from ({low} to {high}): "))
    print("-"*30)
    attempts += 1
    
    if guess == number:
        print("You guessed the right number")
        break
    
    else:
        print("You guessed the wrong number")
        
        R = max(1, R - 1)
        
        if attempts < max_attempts:
            remaining_attempts = max_attempts - attempts
            print(f"{remaining_attempts} attempt(s) left.")
            print("-"*30)
        
        else:
            print("Too many attempt!!")

print("-"*30)

print(f"The answer is {number}")