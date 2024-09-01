### List comprehension
## Example of using list comprehension
# FORMAT: new_list = [new_item for new_item in list]
numbers = [1, 2, 3, 4]
new_numbers = [n + 1 for n in numbers]

# Can also use list comprehension on strings to get a list of letters in the string
name = "Izzul"
new_list = [letter for letter in name]

double_list = [number * 2 for number in range(1, 5)]


## Conditional list comprehension
# FORMAT: new_list = [new_item for new_item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [n.upper() for n in names if len(n) < 5]
print(short_names)




