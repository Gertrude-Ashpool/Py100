import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240717.csv")

# columns = list(data.columns)
#
# for column in columns:
#     print(column)

# colors = data["Primary Fur Color"].value_counts()
# colors_dict = colors.to_dict()

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

colors_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_df = pandas.DataFrame(colors_dict)
new_df.to_csv("squirrel_colors.csv")
