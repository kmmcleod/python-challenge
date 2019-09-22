# Create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','budget_data.csv')

total_months=0
total_net=0
month_of_change=[]
net_change_list=[]
g_increase_value=0
g_increase_month=[]
g_decrease_value=0
g_decrease_month=[]

# Read CSV file
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Skip header
    header=next(csvreader)
    first_row=next(csvreader)

    # Intitialize variables
    
    total_months=total_months+1
    total_net=total_net+int(first_row[1])
    previous_net=int(first_row[1])
    previous_profit=int(first_row[1])
    previous_loss=int(first_row[1])

# Read through each row of data after the header
    for row in csvreader:
        total_months=total_months+1
        total_net=total_net+int(row[1])
        # Calculate net change
        net_change=int(row[1])-previous_net
        previous_net=int(row[1])
        net_change_list=net_change_list+[net_change]
        month_of_change=month_of_change+[row[0]]
        # Calculate greatest increase in profits
        profit_increase_change=int(row[1])-previous_profit
        previous_profit=int(row[1])
        if profit_increase_change > g_increase_value:
            g_increase_value = profit_increase_change
            g_increase_month = row[0]
        # Calculate greatest decrease in losses
        loss_decrease_change=int(row[1])-previous_loss
        previous_loss=int(row[1])
        if loss_decrease_change < g_decrease_value:
            g_decrease_value = loss_decrease_change
            g_decrease_month=row[0]
           
        average_net_change=sum(net_change_list)/len(net_change_list)

        
   

print("Financial Analysis")
print("--------------------")

print(f"Total Months: {total_months} ")

print(f"Net Total: ${total_net}")

print(f"Average change: ${average_net_change}")

print(f"Greatest increase in profits: {g_increase_month} (${g_increase_value})") 

print(f"Greatest decrease in profits: {g_decrease_month} (${g_decrease_value})")

