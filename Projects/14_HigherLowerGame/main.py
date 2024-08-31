from art import logo, vs
from game_data import data
import random

#select random celeb
def select_random_celeb():
    random_celeb = random.choice(data)
    return random_celeb

def main():
    game_is_on = True
    score = 0
    celeb_a = select_random_celeb()
    celeb_b = select_random_celeb()

    while game_is_on is True:
        #Celeb A details
        A_name = celeb_a['name']
        A_description = celeb_a['description']
        A_country = celeb_a['country']
        A_followers = celeb_a['follower_count']

        #Celeb B details
        B_name = celeb_b['name']
        B_description = celeb_b['description']
        B_country = celeb_b['country']
        B_followers = celeb_b['follower_count']


        #Game screen
        print(logo)
        print(f"Compare A: {A_name}, a {A_description}, from {A_country}")
        print(f"Pssst! Celeb A has {A_followers} Million followers")
        print(vs)
        print(f"Compare B: {B_name}, a {B_description}, from {B_country}")
        print(f"Pssst! Celeb A has {B_followers} Million followers")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        #Compare who has more followers
        if guess == "a":
            if A_followers > B_followers:
                score += 1
                print(f"You're right! Current Score: {score}")
                celeb_a = celeb_b
                celeb_b = select_random_celeb()
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                game_is_on = False
        elif guess == "b":
            if B_followers > A_followers:
                score += 1
                print(f"You're right! Current Score: {score}")
                celeb_b = celeb_a
                celeb_a = select_random_celeb()

            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                game_is_on = False
        
main()