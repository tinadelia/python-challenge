import os
import csv


months = []
profit_loss = []
change_list = []
avg=[]

Total = 0
Row_Number = 0
change_total = 0
change_average_total = 0

pybank_csv = os.path.join('Resources', 'budget_data.csv')

    
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)


    for row in csvreader:
        months.append(row[0])
        profit_loss.append(row[1])
        Total = Total + int(row[1])
        change = int(profit_loss[Row_Number]) - int(profit_loss[Row_Number - 1])
        avg.append(change)
        change_list.append(change)
        change_average_total += change
        Row_Number += 1

change_total = sum(change_list)

average_change = change_average_total / (len(avg) - 1)

import numpy as np
min_months = np.argmin(change_list) 
max_months = np.argmax(change_list) 


print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${Total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {(months[max_months])} (${str(max(change_list))})")
print(f"Greatest Decrease in Profits: {(months[min_months])} (${str(min(change_list))})")

output_file = os.path.join('Resources', 'output_folder', 'output.txt')

with open(output_file, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------------------\n")
    txt_file.write(f"Total Months: {len(months)}\n")
    txt_file.write(f"Total: ${Total}\n")
    txt_file.write(f"Average Change: ${round(average_change, 2)}\n")
    txt_file.write(f"Greatest Increase in Profits: {(months[max_months])} (${str(max(change_list))})\n")
    txt_file.write(f"Greatest Decrease in Profits: {(months[min_months])} (${str(min(change_list))})\n")