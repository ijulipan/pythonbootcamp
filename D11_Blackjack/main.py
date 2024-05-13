from art import logo
import random

#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Function to deal a random card
def deal_card():
    return random.choice(cards)

#Function to calculate the total score of a hand
def calculate_score(card_deck):
    total = sum(card_deck)
    if sum(card_deck) == 21 and len(card_deck) == 2:
        return 0
    if 11 in card_deck and sum(card_deck) > 21:
        card_deck.remove(11)
        card_deck.append(1)
    return total

#Function to compare the player's score and computer's score
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "it's a draw!"
    elif computer_score == 0 or user_score > 21:
        return "You lose!"
    elif user_score == 0 or computer_score > 21:
        return "You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You Lose!"

#Main program function
def play_game():

    print(logo)
    user_cards = []
    computer_cards = []

    for starting_card in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"User cards: {user_cards}")
    print(f"Computer cards: {computer_cards}")

    is_game_on = True

    #While loop to let the player play
    while is_game_on:
        user_total = calculate_score(user_cards)
        computer_total = calculate_score(computer_cards)

        print(f"User's total: {user_total}")
        print(f"Computer's total: {computer_total}")

        if user_total == 0 or computer_total == 0 or user_total > 21:
            is_game_on = False
        else:
            continue_drawing = input("Do you want to draw another card? Type 'yes' to draw another type 'no' to stop drawing: ")
            if continue_drawing == "yes":
                user_cards.append(deal_card())
            else:
                is_game_on = False

    #While loop to let the computer play
    while computer_total != 0 and computer_total < 17:
        computer_cards.append(deal_card())
        computer_total = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} and total: {user_total}")
    print(f"Computer's final hand: {computer_cards} and total: {computer_total}")
    print(compare(user_score=user_total, computer_score=computer_total))

#While loop to initialise and keep restarting the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
