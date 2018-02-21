import os
import csv

print("Financial Analysis")
print("-----------------------------------------------")

# Path to collect data from the Resources folder 



##	The total number of months included in the dataset


budgetData1CSV = os.path.join('Resources','budget_data_1.csv')
numberOfMonths = 0
totalRevenue = 0
avgRevenueChange = 0

with open(budgetData1CSV, 'r') as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	next(csvReader, None)
	for row in csvReader:
		numberOfMonths += 1
		totalRevenue = totalRevenue + int(row[1])
	print("Total Months : " + str(numberOfMonths))
	print("Total Revenue : $" +str(totalRevenue))




##  The total amount of revenue gained over the entire period

##  The average change in revenue between months over the entire period

##  The greatest increase in revenue (date and amount) over the entire period

##  The greatest decrease in revenue (date and amount) over the entire period

##budgetWorkbook = ["1","2"]

##for budgetCheck in budgetWorkbook:
''''newbudgetCSV = os.path.join('..', 'output', 'WWE-Data-' + budgetWorkbook + '.csv')
totalRevenue = []
avgRevenueChange = []
greatestRevenueIncrease =[]
greatestRevenueDescrease = []'''