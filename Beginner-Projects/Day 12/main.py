import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Enter a valid type of difficulty!!")
    exit()

print(f"You have {attempts} attempts remaining to guess the number.")
guessing_number = random.randint(1, 100)  # Fixed: Includes 100, excludes 101

for i in range(1, attempts + 1):
    guess = int(input("Make a guess: "))
    
    if guess == guessing_number:
        print(f"You got it! The answer was {guess}")
        break  # Stops the game completely on a win
        
    elif guess > guessing_number:
        print("Too high!!")
    else:
        print("Too low!!")
        
    attempts_left = attempts - i
    if attempts_left > 0:
        print("Guess again")
        print(f"You have {attempts_left} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses. Refresh the page to run again.")
