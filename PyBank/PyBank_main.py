# PyBank_main_Kim
import os
import csv

loadfile = os.path.join("PyBank/Resources/budget_data.csv")
outputfile = os.path.join("analysis/budget_analysis_Kim.text")

# Define variables to track the financial data
total_months = 0
total_net = 0

# Define lists and dictionaries to track profit_losses and dates
profit_losses = []
dates = []


# Read the CSV file
with open(loadfile) as (financial_data):

    # CSV reader specifies delimiter and variable that holds contents
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    #Loop through each row of the dataset and process it

    for row in reader:
        total_months += 1
        date = row[0]
        profit_loss = int(row[1])
    
        dates.append(date)
        profit_losses.append(profit_loss)
        total_net += profit_loss

    # Track the total and net change
    # Calculate changes in Profit/Losses
    changes = [profit_losses[i] - profit_losses[i - 1] for i in range(1, len(profit_losses))]
    average_change = sum(changes) / len(changes)
    

    # Calculate the greatest increase and decrease in profits
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    greatest_increase_date = dates[changes.index(greatest_increase) + 1]  # +1 to get the corresponding date
    greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]  # +1 to get the corresponding date

    # Print the analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_net}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    # Optionally, export the results to a text file
    with open("financial_analysis.txt", "w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("----------------------------\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${total_net}\n")
        txtfile.write(f"Average Change: ${average_change:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
