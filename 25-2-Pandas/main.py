import pandas
#
# data = pandas.read_csv("weather-data.csv")
#
# monday = data[data.day == "Monday"]
# monday_celsius = int(monday.temp)
# monday_temp_f = (monday_celsius * 9 / 5) + 32
#
# print(monday_temp_f)

# create a dataframe of scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 65, 67]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
