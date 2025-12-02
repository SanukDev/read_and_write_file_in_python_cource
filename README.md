CSV Data Processing & Squirrel Fur Color Analysis


This repository contains two small Python scripts demonstrating how to process CSV files using both the built-in csv module and the powerful pandas library.
Contents


 Reading CSV Files Using Standard Python (csv module)
File: weather_reader.py (or whatever the file is named on your repo)
This script shows how to read a CSV file using Python's built-in csv library.
It reads temperature data from weather_data.csv, skips the header, and stores all temperature values into a list.


Squirrel Fur Color Analysis with Pandas


File: squirrel_analysis.py (or similar)
This script analyzes the 2018 Central Park Squirrel Census dataset and counts how many squirrels have each primary fur color.
It generates a new CSV file containing a summary of the results.


 Core Features:

 
Reads a CSV file using pandas.read_csv()
Extracts and counts values from the "Primary Fur Color" column
Supports Gray, Black, and Cinnamon fur types
Outputs a clean summary CSV
