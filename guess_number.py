# The computer chooses a number and then we have to guess it.

# import random to generate the number
import random

#create function
def guess(x):
    # create random number, between 1 and x
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Too high! Guess again.")
        elif guess < random_number:
            print("Too low! Guess again.")
        
    print(f"Congrats! You guessed correctly! The number is {random_number}!")

# Clarify the bounds set, have the computer guess between the bounds
def computer_guess(x):
   low = 1
   high = x
   guess = 0
   feedback = ''
   while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(h), too low(l), or correct(c)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
    
   print(f"Yay, I guessed your number {guess}!")
   


guess(20)
computer_guess(25)