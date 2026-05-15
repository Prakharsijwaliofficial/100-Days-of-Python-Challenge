import art

print(art.logo)

dict1 = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dict1[name] = bid

    other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if other == "no":
        break
    else:
        # This "clears" the screen for the next bidder
        print("\n" * 100)

highest_bid = 0
winner = ""

# Loop through the dictionary to find the highest value
for name in dict1:
    bid_amount = dict1[name]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = name

print(f"The winner is {winner} with a bid of ${highest_bid}")
