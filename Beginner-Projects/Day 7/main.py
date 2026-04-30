stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random

word_list = ["aardvark", "baboon", "camel"]
guess_word = random.choice(word_list)
underscores = ["_"] * len(guess_word)
life = 6
letter_list = list(guess_word)
print(stages[life])

while life > 0:
    print(f"\nWord to guess: {' '.join(underscores)}")
    guess = input("Guess a letter: ").lower()

    # 1. Check if they already guessed it (right or wrong)
    if guess in underscores:
        print(f"--> You already guessed '{guess}'. Try a different letter.")

        continue  # This jumps back to the start of the 'while' loop

    # 2. Check if the guess is correct
    if guess in letter_list:
        for index, letter in enumerate(letter_list):
            if letter == guess:
                underscores[index] = guess


        # 3. Check if they won
        if "_" not in underscores:
            print(stages[life])
            print(f"\nWord to guess: {' '.join(underscores)}")
            print("You win the game! 🎉")
            break

    else:
        # 4. Handle wrong guesses
        life -= 1
        print(stages[life])
        print(f"************************* {life}/6 Lives Left *************************")

if life == 0:
    print(stages[life])
    print(f"************************* It was {guess_word}. You lose! *************************")
