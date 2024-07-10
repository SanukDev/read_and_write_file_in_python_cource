
# Reading with pandas
import pandas

data_csv = pandas.read_csv("weather_data.csv")
print(data_csv["temp"])
