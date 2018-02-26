
##	The total number of months included in the dataset
##  The total amount of revenue gained over the entire period
	


##  The average change in revenue between months over the entire period

		
		

##  The greatest increase in revenue (date and amount) over the entire period

##  The greatest decrease in revenue (date and amount) over the entire period

import os
import csv

print("Financial Analysis")
print("-----------------------------------------------")

# Path to collect data from the Resources folder 




budgetData1CSV = os.path.join('Resources','budget_data_1.csv')
newbudgetData1CSV = os.path.join('output', 'newdata1' + '.csv')
numberOfMonths = 0
totalRevenue = 0
avgChange = 0
nextMonth = 0
currentMonth = 0
row2 = 1
revenueList = []

with open(budgetData1CSV, 'r') as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	next(csvReader, None)
	for row in csvReader:
		numberOfMonths += 1
		totalRevenue = totalRevenue + int(row[1])
		currentMonth = int(row[1])
		for row2 in csvReader:
			nextMonth = int(row2[1])
			avgChange = nextMonth-currentMonth
			revenueList.append(avgChange)
			break
		
	totalAvgChange = avgChange/numberOfMonths
	print("Average change : " + str(totalAvgChange))
	print("Total Months : " + str(numberOfMonths))
	print("Total Revenue : $" +str(totalRevenue))

cleanCSV = zip("Average change : " + str(totalAvgChange),
	"Total Months : " + str(numberOfMonths),
	"Total Revenue : $" +str(totalRevenue))

with open(newbudgetData1CSV, 'w', newline="") as csvFile:
	csvWriter = csv.writer(csvFile, delimiter=',')
	csvWriter.writerows(cleanCSV)

budgetData1CSV = os.path.join('Resources','budget_data_2.csv')
newbudgetData1CSV = os.path.join('output', 'newdata2' + '.csv')
numberOfMonths = 0
totalRevenue = 0
avgChange = 0
nextMonth = 0
currentMonth = 0
row2 = 1
revenueList = []

print("Financial Analysis")
print("-----------------------------------------------")


with open(budgetData1CSV, 'r') as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',')
	next(csvReader, None)
	for row in csvReader:
		numberOfMonths += 1
		totalRevenue = totalRevenue + int(row[1])
		currentMonth = int(row[1])
		for row2 in csvReader:
			nextMonth = int(row2[1])
			avgChange = nextMonth-currentMonth
			revenueList.append(avgChange)
			break
		
	totalAvgChange = avgChange/numberOfMonths
	print("Average change : " + str(totalAvgChange))
	print("Total Months : " + str(numberOfMonths))
	print("Total Revenue : $" +str(totalRevenue))

cleanCSV = zip("Average change : " + str(totalAvgChange),
	"Total Months : " + str(numberOfMonths),
	"Total Revenue : $" +str(totalRevenue))

with open(newbudgetData1CSV, 'w', newline="") as csvFile:
	csvWriter = csv.writer(csvFile, delimiter=',')
	csvWriter.writerows(cleanCSV)