import csv 
import os

budget_data_input = os.path.join("..", "Desktop", "budget_data.csv")
budget_data_output = os.path.join("..", "Desktop", "budget_output.csv")

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]
total_net = 0 

with open(budget_data_input) as financial_data:
    reader = csv.reader(financial_data)


    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader: 

        total_months = total_months + 1
        total_net = total_net + int(row[1])
    
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list +[net_change]
        month_of_change = month_of_change + [row[0]]
    
        if net_change > greatest_increase[1]: 
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
    
        if net_change < greatest_decrease[1]: 
            greatest_decrease[0] = row[0]
            greatest_decrease[1] =net_change
        
net_monthly_avg = sum(net_change_list) / len(net_change_list)

Output = ( f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(Output)

with open(budget_data_output, "w") as txt_file: 
    txt_file.write(Output)