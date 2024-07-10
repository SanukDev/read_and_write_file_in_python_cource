
# Standard mode read files csv
import csv
with open("weather_data.csv", mode="r") as data_csv:
    temp = []
    lines_file = csv.reader(data_csv)
    for row in lines_file:
        if row[1] != "temp":
            temp.append(row[1])
            print(temp)


