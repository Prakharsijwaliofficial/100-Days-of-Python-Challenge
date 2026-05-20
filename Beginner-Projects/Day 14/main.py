import random
import game_data
import art

print(art.logo)
score = 0
game_should_continue = True

# Get the first random person for position A
person_a = random.choice(game_data.data)

while game_should_continue:
    # Get a random person for position B
    person_b = random.choice(game_data.data)

    # Make sure Person A and Person B are not the exact same person
    while person_a == person_b:
        person_b = random.choice(game_data.data)

    # Print the comparison
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

    # Get user guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts
    a_follower_count = person_a["follower_count"]
    b_follower_count = person_b["follower_count"]

    # Check if user is correct
    if a_follower_count > b_follower_count:
        correct_answer = "a"
    else:
        correct_answer = "b"

    # Handle the game outcome
    if guess == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}.\n")

        # The winner becomes the next Person A
        if correct_answer == "b":
            person_a = person_b
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
