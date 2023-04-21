import os
import csv

#pull CSV
budget_data_path =os.path.join('..', 'Pybank', 'budget_data.csv')

with open(budget_data_path) as budget_data:
    reader = csv.reader(budget_data, delimiter = ',')
    header= next(reader)

    #csv lists
    months = []
    profit_loss = []
    change = []

    for row in reader:
       months.append(row[0])
       profit_loss.append(int(row[1]))
    for i in range(len(profit_loss)-1):
        change.append(profit_loss[i+1]-profit_loss[i])

increase = max(change)
decrease = min(change)

monthincrease = change.index(max(change))+1
monthdecrease = change.index(min(change))+1

print("Financial Analysis")
print(" ")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: {round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {months[monthincrease]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {months[monthdecrease]} (${(str(decrease))})")