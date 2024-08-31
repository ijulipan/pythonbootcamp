from art import logo
import random


#Welcome the player
print(logo)
print("Welcome to Guess the Number!")
print("I'm guessing a number between 1 and 100")
lives = 0

def main(lives):
# While loop to keep asking the player to guess until guessed correctly or run out of lives
    while lives is not 0:
        print(f"You have {lives} lives left")
        guess = int(input("Please guess a number: "))

        #Compare between the two numbers
        if guess > random_number:
            print("Too High")
            lives -= 1
        elif guess < random_number:
            print("Too low")
            lives -= 1
        else:
            lives = 0
        
        #Message to display to the user when they win or lose
        if lives == 0 and guess != random_number:
            print(f"You run out of lives. You lose!")
        elif lives == 0 and guess == random_number:
            print(f"You guessed correctly! The number was {random_number}. You win!")

#random number generator
random_number = random.randint(1,100)
print(f"Psst the number is {random_number}")

#Ask the player if they want it easy or hard
mode = input("Do you want to play the game in Easy or Hard mode? Type 'easy' or 'hard': ")
if mode == "easy":
    lives = 10
else:
    lives = 5

main(lives)
