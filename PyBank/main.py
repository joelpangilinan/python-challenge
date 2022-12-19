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
    
# To determine the net total amount of "Profit/Losses" over the entire period, sum up the total the column "Profit/Losses" minus the header
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    net_total = 0
    # Exclude the header
    header = next(read_budget)
    for row in read_budget:
        net_total += int(row[1])
    
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
total_months = number_of_months - 1
total_changes = net_total
average_change = "%.2f" %(float(net_total / total_months)) # Format the result to limit the number of decimal places to two


# The greatest increase and decrease in profits (date and amount) over the entire period
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    # Exclude the header
    header = next(read_budget)
    profit = []
    for row in read_budget:
        profit.append(int(row[1]))
    
    values = [x for x in profit]
    max_profit = max(values)        # Get the greatest increase in profit
    min_profit = min(values)        # Get the greatest decrease in profit

# Determine the date that matches the max_profit
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    # Exclude the header
    header = next(read_budget)
    for row in read_budget:
        if int(row[1]) == max_profit:
            max_date = (row[0])
            

# Determine the date that matches the min_profit
with open(filepath) as budget_file:
    read_budget = csv.reader(budget_file, delimiter=',')
    # Exclude the header
    header = next(read_budget)
    for row in read_budget:
        if int(row[1]) == min_profit:
            min_date = (row[0])
            

# Output the results to the terminal
print(f"Financial Analysis\n")
print(f"--------------------------------\n")
print(f"Total Months: {str(number_of_months)}\n")
print(f"Total: ${str(net_total)}\n")
print(f"Average Change: ${str(average_change)}\n")
print(f"Greatest Increase in Profits: {max_date} (${str(max_profit)})\n")
print(f"Greatest Decrease in Profits: {min_date} (${str(min_profit)})")

# Write the results to the financial_results.txt under the analysis folder
output_path = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyBank", "analysis", "financial_results.txt")
with open(output_path, 'a') as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"--------------------------------\n")
    textfile.write(f"Total Months: {str(number_of_months)}\n")
    textfile.write(f"Total: ${str(net_total)}\n")
    textfile.write(f"Average Change: ${str(average_change)}\n")
    textfile.write(f"Greatest Increase in Profits: {max_date} (${str(max_profit)})\n")
    textfile.write(f"Greatest Decrease in Profits: {min_date} (${str(min_profit)})")
