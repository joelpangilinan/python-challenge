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


# Specify the financial record file
#filepath = "../Resources/budget_data.csv"
#filepath = os.path.join('..', 'Resources', 'budget_data.csv')
filepath = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyBank", "Resources", "budget_data.csv")

# To determine the total number of months included in the dataset, you have to count the number of rows minus the header
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    months = len(list(read_budget))
    number_of_months = months - 1
    #print(number_of_months)

# To determine the net total amount of "Profit/Losses" over the entire period, sum up the total the column "Profit/Losses" minus the header
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    net_total = 0
    # Exclude the header
    header = next(read_budget)
    for row in read_budget:
        net_total += int(row[1])
    #print("Total: ", net_total)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
total_months = number_of_months - 1
total_changes = net_total
average_change = float(net_total / total_months)
#print("Average Change: $", average_change)

# The greatest increase in profits (date and amount) over the entire period
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    # Exclude the header
    header = next(read_budget)
    profit = []
    for row in read_budget:
        profit.append(int(row[1]))
    
    values = [x for x in profit]
    max_profit = max(values)
    min_profit = min(values)
    #print(max_profit)
    #print(min_profit)

# Determine the date that matches the max value
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    # Exclude the header
    header = next(read_budget)
    for row in read_budget:
        if int(row[1]) == max_profit:
            max_date = (row[0])
            #print(max_date)

# Determine the date that matches the min value
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    # Exclude the header
    header = next(read_budget)
    for row in read_budget:
        if int(row[1]) == min_profit:
            min_date = (row[0])
            #print(min_date)

# Send the results to the analysis report file
print("Financial Analysis")
print("--------------------------------")
print("Total Months: ", number_of_months)
print("Total: $", net_total)
print("Average Change: $", average_change)
print("Greatest Increase in Profits: ", max_date, " ($", max_profit, ")")
print("Greatest Decrease in Profits: ", min_date, " ($", min_profit, ")")

# Write the results to a file in analysis folder
output_path = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyBank", "analysis", "analysis.txt")
with open(output_path, 'a') as textfile:
    textfile.write("Financial Analysis")
    textfile.write('\n')
    textfile.write("--------------------------------")
    textfile.write('\n')
    textfile.write("Total Months: ")
    textfile.write(str(number_of_months))
    textfile.write('\n')
    textfile.write("Total: $")
    textfile.write(str(net_total))
    textfile.write('\n')
    textfile.write("Average Change: $")
    textfile.write(str(average_change))
    textfile.write('\n')
    textfile.write("Greatest Increase in Profits: ")
    textfile.write(max_date)
    textfile.write(" ($")
    textfile.write(str(max_profit))
    textfile.write(")")
    textfile.write('\n')
    textfile.write("Greatest Decrease in Profits: ")
    textfile.write(min_date)
    textfile.write(" ($")
    textfile.write(str(min_profit))
    textfile.write(")")