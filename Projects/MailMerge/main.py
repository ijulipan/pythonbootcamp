
PLACEHOLDER = "[name]"

with open("Projects/MailMerge/Input/Names/invited_names.txt", mode="r") as names:
    # To retrieve the names and put them in a list
    name_list = names.readlines()
    #print(name_list)

with open("Projects/MailMerge/Input/Letters/starting_letter.txt") as letter_file:
    # To read the file and store it as a string in a variable
    letter_contents = letter_file.read()
    for name in name_list:
        # Replace the [name] placeholder with the names in the list of names
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        # Writes a new txt file for each name 
        with open(f"Projects/MailMerge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

            
   


