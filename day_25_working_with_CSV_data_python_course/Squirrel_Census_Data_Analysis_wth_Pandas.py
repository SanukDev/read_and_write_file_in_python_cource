from typing import Dict
# Data analysis with pandas. We're analysing a file CSV with data of varius features of squirrels
import pandas
# Opening the file CSV with pandas
data_squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Picking up the data that we're going to analysis
fur_color = data_squirrel["Primary Fur Color"]
# Turned in a list
list_fur_color = fur_color.to_list()
gray = 0
black = 0
red = 0
# Cont the data  for analysis
for squirrel in list_fur_color:
    if squirrel == "Gray":
        gray += 1
    elif squirrel == "Black":
        black += 1
    elif squirrel == "Cinnamon":
        red += 1
# Creating the dictionary for Data Frame
color_squirrel = {
    "Colors":["Gray", "Red", "Black"],
    "Count":[gray, red, black]
}
# Making the Data Frame
df_squirrel = pandas.DataFrame(color_squirrel)

df_squirrel.to_csv("df_squirrel")