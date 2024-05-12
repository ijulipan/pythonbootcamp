#Import and print the logo from art.py
from art import logo
print(logo)
print("Welcome to the secret auction program.\n")

database = {}
bidders = True

def highest_bidder(bidding_record):
    bid_value = 0
    for person in bidding_record:
        if bidding_record[person] > bid_value:
            bid_value = bidding_record[person]
            winner = person
    print(f"The highest bid is {winner} with a value of RM{bid_value}!")

while bidders is True:
    name = input("Who is bidding?: ")
    bid = int(input("How much are you bidding?: RM"))
    database[name] = bid
    more_bidders = input("Is there more bidders? Type 'yes' or 'no'\n")
    if more_bidders == "yes":
        bidders = True
    else:
        bidders = False
        highest_bidder(bidding_record=database)

