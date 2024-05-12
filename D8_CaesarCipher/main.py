alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function of the caesar cipher program called
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  shift_amount = shift_amount % 26 # Used to retrieve the remainder of the shift_amount should the user inputs a shift_amount greater than 26 (alphabets)
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Run once when starting the program 
from art import logo
print(logo) 

# While loop to keep running the program by asking user if they want to continue
game_is_on = True
while game_is_on is True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  continue_game = input("Do you want to continue? type 'yes' or 'no':\n").lower()
  if continue_game == "yes":
    game_is_on = True
  else:
    game_is_on = False
    
