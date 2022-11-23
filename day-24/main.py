# with open("day-24\weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("day-24\weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#          temperature.append(int(row[1]))
    
#     print(temperature)

import pandas

data = pandas.read_csv("day-24/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# data_dict = data.to_dict()

# temp = data[data.day == "Monday"]
# print(temp.condition)

grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

print(grey)
print(red)
print(black)

data_dict = {
    "Fur Color": ["Gray" , "Cinnamon", "Black"],
    "Count": [grey, red , black]
}

#convert this to DateFrame

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
