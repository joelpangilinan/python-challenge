import os
import csv

# set paths for input and output files
budget_csv = os.path.join("Resources", "budget_data.csv")
output_txt = os.path.join("analysis", "financial_results.txt")
#budget_csv = os.path.join("/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/python-challenge/PyBank/Resources", "budget_data.csv")
#output_txt = os.path.join("/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/python-challenge/PyBank/analysis", "financial_results.txt")
#budget_csv = os.path.join("\Resources", "budget_data.csv")
#output_txt = os.path.join("\analysis", "financial_results.txt")

# initialize variables
total_months = 0
net_total = 0
prev_profit = None
profit_changes = []
greatest_inc = {"date": "", "amount": 0}
greatest_dec = {"date": "", "amount": 0}

# read input file and iterate over rows
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # skip header row
    for row in csvreader:
        # update total months and net total
        total_months += 1
        net_total += int(row[1])

        # update profit changes and track greatest increase/decrease
        if prev_profit is not None:
            change = int(row[1]) - prev_profit
            profit_changes.append(change)
            if change > greatest_inc["amount"]:
                greatest_inc["date"] = row[0]
                greatest_inc["amount"] = change
            elif change < greatest_dec["amount"]:
                greatest_dec["date"] = row[0]
                greatest_dec["amount"] = change
        prev_profit = int(row[1])

# compute average change
if len(profit_changes) > 0:
    avg_change = sum(profit_changes) / len(profit_changes)
else:
    avg_change = 0

# write output to text file
with open(output_txt, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${avg_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_inc['date']} (${greatest_inc['amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_dec['date']} (${greatest_dec['amount']})\n")

# print output to console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc['date']} (${greatest_inc['amount']})")
print(f"Greatest Decrease in Profits: {greatest_dec['date']} (${greatest_dec['amount']})")
