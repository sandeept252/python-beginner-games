# guess_the_number_0.0.3.py
# Guess the Number Game v. 0.0.3 by Sandeept
print("\nGuess the Number by Sandeept".upper())
print("=" * 40)

while True:
    # 1. Generate a random number between a given range (a to b)
    from random import randint

    first_num = 1
    last_num = 20
    number = randint(first_num, last_num)
    
    try:
        print(f"\nI have a number between {first_num} and {last_num} in my memory. Can you guess it?")
        # 2. Set the maximum number of chances
        number_of_chances = 5
        number_of_tries = 1
    
        # 3. Ask the user to guess a number between a and b until the number of chances becomes 0.
        while number_of_chances > 0:
        
            print(f"\nYou have {number_of_chances} chances left!\n")
            guess = int(input("Take take a guess: "))
        
            if (guess < first_num) or (guess > last_num):
                print("\nPlease enter a number between 1 and 20!")
                continue
        
            if guess > number:
                print("\nYou guessed too high!")
            
            if guess < number:
                print("\nYou guessed too low!")
            
            if guess == number:
                print(f"\nWow! You guessed it in {number_of_tries} tries!\n".upper())
                break
        
            number_of_chances -= 1
            number_of_tries += 1
        
            print("." * 25)
        
        if guess != number:
            print(f"\nSorry, I won ! The number in my memory is: {number}".upper())
        
        print("-" * 40)    
        rerun_choice = input("\nDo you want to play again? (Y/N): ").upper()
        
        if rerun_choice == "N":
            print("\nThank you for playing! See you again!\n")
            break
    
    except ValueError as e:
        print(f"\nError: {e}")
        print("-" * 40)