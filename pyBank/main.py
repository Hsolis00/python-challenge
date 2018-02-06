import csv

# Declare lists to store CSV contents
bd1 = []
bd2 = []

# Iterate over each row of budget_data_1.csv and append the row as a list to bd1 list
with open('./python-challenge-master/budget_data_1.csv', 'r') as budgetOne:
    budgetOneReader = csv.reader(budgetOne)
    for row in budgetOneReader:
        bd1.append(row)

# Iterate over each row of budget_data_2.csv and append the row as a list to bd2 list
with open('./python-challenge-master/budget_data_2.csv', 'r') as budgetTwo:
    budgetTwoReader = csv.reader(budgetTwo)
    for row2 in budgetTwoReader:

with open('./python-challenge-master/budget_all.csv', 'w') as budgetAll:
    budgetAllWriter = csv.writer(budgetAll)
      for row in budgetAllWriter:
        #combined_row = []
        bd1.extend(bd2)
    #for budgetOne_row in bd1:
     #   combined_row = []
      #  combined_row.extend(budgetOne_row)
       # for budgetTwo_row in bd2:
        #    if budgetOne_row[0] != budgetOne_row[0]:
         #       combined_row.append(budgetTwo_row[1])
        #budgetAllWriter.writerow(row)

# Create reference for the CSV files
bd1 = "budget_data_1.csv"
bd2 = "budget_data_2.csv"

# Name the variables
total_months = 0
total_revenue = 0
revenue_change = 0
greatest_increase = 0
greatest_increase = 0

# Open and read csv
with open("budget_data_1.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter="," )

    next(csvreader, None)

    # Iterate through each row
    for row in csvreader:
        total_months +=  1
        total_revenue += int(row[1])

        print(row[0], row[1])

print(total_months)
print(total_revenue)
