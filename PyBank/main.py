# This script will analyze the financial record indicated on the Resources directory.  The file is budget_data.csv
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# Import the csv module
import os
import csv

# To determine the total number of months included in the dataset, you have to count the number of rows minus the header
# Read the financial record
filepath = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyBank", "Resources", "budget_data.csv")
read_csv = csv.reader(open(filepath))
number_of_months = len(list(read_csv))
print("Total Months: ", number_of_months - 1)