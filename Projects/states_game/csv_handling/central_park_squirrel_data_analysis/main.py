import pandas

squirrel_data = pandas.read_csv("Projects\Project23\csv_handling\central_park_squirrel_data_analysis\Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# # Count how many squirrels are which color
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(f"Gray: {gray_squirrels_count}, Cinnamon: {cinnamon_squirrels_count}, Black: {black_squirrels_count}")

# Create a new dictionary
squirrel_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# Create a new pandas datafram & extract to new csv file
new_data = pandas.DataFrame(squirrel_count)
new_data.to_csv("Projects\Project23\csv_handling\central_park_squirrel_data_analysis\squirrel_count.csv")