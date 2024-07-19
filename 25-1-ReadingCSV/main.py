# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("weather-data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperature = int(row[1])
            temperatures.append(temperature)

print(temperatures)
