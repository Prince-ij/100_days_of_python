# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     i = 0
#     for row in data:
#         if i != 0:
#             temperatures.append(int(row[1]))
#         i += 1

# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# max_temp = data["temp"].max()

# print(data[data.temp == max_temp])

# data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")

# fur_color = data["Primary Fur Color"]
# grey = len(data[fur_color == 'Gray'])
# red = len(data[fur_color == 'Cinnamon'])
# black = len(data[fur_color == 'Black'])

# fur_color_dict = {
#     "Fur Colors": ['Red', "Grey", "Black"],
#     "Count": [red, grey, black]
# }

# new_data = pandas.DataFrame(fur_color_dict)
# new_data.to_csv("fur_count.csv")




