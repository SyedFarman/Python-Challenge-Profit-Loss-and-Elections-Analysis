# Modules
import csv
import os

# Set path for file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Initialize Total Months and Total Profit and other
totalmonths= 0
totalprofitloss=0
avgprofitlosses=0
maxincrease=["",0]
maxdecrease=["",0]
lastmonthprofit=0
netprofitlosseslist=[]

# with open file
with open(csv_path, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header
    header = next(csvreader)
 
    #read the first row
    firstdatarow= next(csvreader)

    # Add to total months count and total profit
    totalmonths += 1
    lastmonthprofit = int(firstdatarow[1])
    totalprofitloss += int(firstdatarow[1])

    # For each row in the CSV file
    for row in csvreader:
        # Add the count of the total months
        totalmonths += 1
        totalprofitloss+=int(row[1])

        netprofitlosses= int(row[1])-lastmonthprofit
        lastmonthprofit=int (row[1])
        netprofitlosseslist+=[netprofitlosses]

        # Finding value of Max & Min profit/Loss
        if netprofitlosses> maxincrease[1]:
           maxincrease[1]=netprofitlosses
           maxincrease[0]=row[0]
        elif netprofitlosses < maxdecrease[1]:
           maxdecrease[1] = netprofitlosses
           maxdecrease[0] = row[0]

    # Find Average of profit and loss 
    avgprofitlosses= totalprofitloss/totalmonths
    avgprofitlosses= sum(netprofitlosseslist)/len(netprofitlosseslist)
    
    # Export the results to text file
    outputfile = os.path.join("Analysis","budget_analysis.text")
    with open(outputfile, "w") as txt_file:

    # Print the Financial Analysis (to terminal)
        Financial_Analysis =(
    f"Financial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {totalmonths }\n"
    f"Total: ${totalprofitloss:,}\n"
    f"Average Change: ${avgprofitlosses:,.2f}\n"
    f"Greatest Increase in Profits: {maxincrease[0]} (${maxincrease[1]:,})\n"
    f"Greatest Decrease in Profits: {maxdecrease[0]} (${maxdecrease[1]:,})\n"
    )
        print(Financial_Analysis)
        txt_file.write(Financial_Analysis)






    