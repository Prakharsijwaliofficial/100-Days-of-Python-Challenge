import art
import random

want = input("Do you want to play a game BlackJack? Type 'y' or 'n': ")
if want == "n":
    exit()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while want == "y":
    # User starting card generator code
    user_card_1 = random.choice(cards)
    user_card_2 = random.choice(cards)
    user_card_list = [user_card_1, user_card_2]
    user_current_score = sum(user_card_list)

    # Computer card generator code
    computer_card_1 = random.choice(cards)
    computer_card_2 = random.choice(cards)
    computer_card_list = [computer_card_1, computer_card_2]
    computer_current_score = sum(computer_card_list)

    # Computer dealer AI rule: draws cards until total score is 17 or higher
    while computer_current_score < 17:
        computer_card_3 = random.choice(cards)
        computer_card_list.append(computer_card_3)
        computer_current_score += computer_card_3

    print(art.logo)
    print(f"\tYour cards: {user_card_list}, current score: {user_current_score}")
    print(f"\tComputer's first card: {computer_card_1}")

    # Set up a flag to control the card hitting loop cleanly
    player_drawing = True
    
    while player_drawing:
        want1 = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if want1 == "y":
            user_card_want = random.choice(cards)
            user_card_list.append(user_card_want)
            user_current_score += user_card_want
            
            # Ace handling: if player busts and has an 11, turn it into a 1
            if user_current_score > 21 and 11 in user_card_list:
                ace_position = user_card_list.index(11)
                user_card_list[ace_position] = 1
                user_current_score = sum(user_card_list) # Recalculate score

            if user_current_score > 21:
                print(f"\tYour final hand: {user_card_list}, final score: {user_current_score}")
                print(f"\tComputer's first card: [{computer_card_1}], final score: {computer_card_1}")
                print("You went over. You lose 😤")
                player_drawing = False  # End the hitting turn
            else:
                print(f"\tYour cards: {user_card_list}, current_score: {user_current_score}")
                print(f"\tComputer's first card: {computer_card_1}")
                
        elif want1 == "n":
            player_drawing = False

    # Check game outcomes only after drawing has completely finished
    if user_current_score <= 21:
        print(f"Your final hand: {user_card_list}, final score: {user_current_score}")
        print(f"Computer's final hand: {computer_card_list}, final score: {computer_current_score}")
        
        if computer_current_score > 21:
            print("Opponent went over. You win 😁")
        elif user_current_score > computer_current_score:
            print("You win 😃")
        elif user_current_score < computer_current_score:
            print("You lose 😤")
        else:
            print("Its a Draw 🙃")

    # Ask the user if they want to restart the match loop
    want = input("Do you want to play a game BlackJack? Type 'y' or 'n': ")
