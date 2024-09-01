import pandas

# Extract csv file content
data = pandas.read_csv("Projects\Project23\csv_handling\weather_data.csv")

# Convert to dictionary
data_dict = data.to_dict()


# Get data in Columns
data["condition"]
data.condition

# Get data in row
data[data.day == "Monday"]
data[data.temp == data.temp.max()]


# monday = data[data.day == "Monday"]
# fahrenheit = (monday.temp[0] * 9/5) + 32
# print(fahrenheit)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
# Save new dataframe to a csv file
new_data.to_csv("new_data.csv")




    


