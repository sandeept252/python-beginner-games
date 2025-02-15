# guess_the_number.py: Python program for the guessing game

# Generate a random integer between a range of numbers
from random import randint
number = randint(1, 100)

print("Guess the number".upper())
print("=" * 40)

player_name = input("What's your name: ")

print(f"\nHi, {player_name}. I am thinking of a number 1 and 100. Can you guess it?")

# Ask the user to enter an integer within the range for n number of times
number_of_guess = 10
chances_taken = 1

while number_of_guess >= 0:
    print(f"\nYou have {number_of_guess} guesses left!")
    
    guess = int(input("Take a guess: "))
    
    if guess > number:
        print("\nYour guess is high.")
        
    if guess < number:
        print("\nYour guess is low.")
    
    if guess == number:
        print(f"\n Wow! You did it in chance no. {chances_taken}\n")
        break
    
    number_of_guess = number_of_guess - 1
    chances_taken = chances_taken + 1

# if the number is incorrect, continue the loop until it reaches n

# if the number is correct, exit the program
