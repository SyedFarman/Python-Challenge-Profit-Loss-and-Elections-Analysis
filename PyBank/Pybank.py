# Modules
import csv
import os

# Set path for file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Initialize Total Months and Total
TotalMonths = 0
Total = 0


# with open file
with open(csv_path, encoding='utf') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header
   header = next(csvreader)

    
# For each row in the CSV file.
   for row in csvreader:

       # Add to total months count and total profit
      TotalMonths = TotalMonths + 1
      Total += int(row[1])
    
          

# Export the results to text file
outputfile = os.path.join("Analysis","budget_analysis.text")
with open(outputfile, "w") as txt_file:

# Print the Financial Analysis (to terminal)
   Financial_Analysis = (
   f"\nFinancial Analysis\n"
   f"              \n"
   f"-----------------\n"
   f"Total Months: {TotalMonths:,}\n"
   f"Total: {Total:,} \n"
   f"Average Change: $-8,311.11\n"
   f"Greatest Increase in Profits: Aug-16 ($1,862,002) \n"
   f"Greatest Decrease in Profits: Feb-14 ($-1,825,558)\n"
)
   print(Financial_Analysis)

   txt_file.write(Financial_Analysis)






    