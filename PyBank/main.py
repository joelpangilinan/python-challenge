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
#filepath = "../Resources/budget_data.csv"
#filepath = os.path.join('..', 'Resources', 'budget_data.csv')
filepath = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyBank", "Resources", "budget_data.csv")
read_csv = csv.reader(open(filepath))
number_of_months = len(list(read_csv))
print("Total Months: ", number_of_months - 1)

# To determine the net total amount of "Profit/Losses" over the entire period, sum up the total the column "Profit/Losses" minus the header
# Determine the number of rows
#filepath = "../Resources/budget_data.csv"
filepath = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyBank", "Resources", "budget_data.csv")

with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    net_total = 0
    # Exclude the header
    header = next(read_budget)
    for row in read_budget:
        #print(int(row[1]))
        net_total += int(row[1])
    print("Total: ", net_total)


