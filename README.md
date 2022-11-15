# Python-Challenge-Profit-Loss-and-Elections-Analysis
Python Challenge: PyBank-Profit &amp; Loss Analysis and PyPoll-Elections Analysis

# Profit And Loss Analysis
## Project Overview

In the project we are analysig financial records of the company,for the given period.
 
## Summary

After analysing the financials of the company, we can say that in last 86 months company has a profit of 22M, and has average change per month is -8,311.11, and we saw a greatest jump in the month of Aug-16 with 1.86M and lost change per month in Feb-14 with -1.82M

![Financial Analysis](https://user-images.githubusercontent.com/24644072/201807589-a0555a3b-7068-4548-9b48-3c5bd81aef0d.PNG)

![](Images/Financial Analysis.png)

***1.a)‘Set path for file.***
```
csv_path = os.path.join('Resources', 'budget_data.csv')
```
***b)‘# # Initialize Total Months and Total Profit and other***
```
totalmonths= 0
totalprofitloss=0
avgprofitlosses=0
maxincrease=["",0]
maxdecrease=["",0]
lastmonthprofit=0
netprofitlosseslist=[]
```
  

***2.a)' with open file.***
```
with open(csv_path, encoding='utf') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
 ```
  ***b)' # Read the header.***
   ```
header = next(csvreader)
 ```

***c)‘# For each row in the CSV file..***
 ```
 for row in csvreader:
 ```
***d)‘ # Add to total months count and total profit ..***
 ```
    totalmonths += 1
    lastmonthprofit = int(firstdatarow[1])
    totalprofitloss += int(firstdatarow[1])
 ```
***e)‘ # Add the count of the total months ..***
 ```
    	totalmonths += 1
        totalprofitloss+=int(row[1])

        netprofitlosses= int(row[1])-lastmonthprofit
        lastmonthprofit=int (row[1])
        netprofitlosseslist+=[netprofitlosses]
 ```
***f)‘ # Finding value of Max & Min profit/Loss***
 ```
    	 if netprofitlosses> maxincrease[1]:
           maxincrease[1]=netprofitlosses
           maxincrease[0]=row[0]
        elif netprofitlosses < maxdecrease[1]:
           maxdecrease[1] = netprofitlosses
           maxdecrease[0] = row[0]
 ```
***g)‘ # Find Average of profit and loss***
 ```
    	 avgprofitlosses= totalprofitloss/totalmonths
   	 avgprofitlosses= sum(netprofitlosseslist)/len(netprofitlosseslist)
 ```
***3.a)‘Export the results to text file.***
 ```
outputfile = os.path.join("Analysis","budget_analysis.text")
with open(outputfile, "w") as txt_file:

 ```
***b)‘ # Print the Financial Analysis (to terminal)***
 ```
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
 ```


 # Election Analysis
## Project Overview

In the project we are analysig Election results of the small town.
 
## Summary

There were total 369,711 votes had been cast, and the Winner is Diana DeGette who received 73% votes that is equal to 272,892
![Election Result](https://user-images.githubusercontent.com/24644072/201807626-9375d6b6-8f7c-463a-8685-70cb5e0cbd39.PNG)

![](Images/Election Result.png)

***1.a)‘Set path for file.***
```
election_csv = os.path.join("Resources","election_data.csv")
```
***b)‘# Initialize a total vote counter,Candidate Options and candidate votes.***
```
total_votes = 0
candidate_options = []
candidate_votes = {}
```
***c)‘# Track the winning candidate, vote count and percentage.***
```
winning_candidate = ""
winning_count = 0
winning_percentage = 0
```  

***2.a)' Read the csv and convert it into a list of dictionaries.***
```
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
 ```
  ***b)' # Read the header.***
   ```
header = next(csvreader)
 ```

***c)‘# For each row in the CSV file..***
 ```
 for row in csvreader:
 ```
***d)‘ # Add to the total vote count & candidate name.***
 ```
       total_votes = total_votes + 1
       candidate_name = row[2]
 ```
***e)‘ #If the candidate does not match any existing candidate add it to candidate list .***
 ```
       if candidate_name not in candidate_options:
           candidate_options.append(candidate_name)
           candidate_votes[candidate_name] = 0
           candidate_votes[candidate_name] += 1
 ```

***3.a)' Export the final candidate vote count to the text file..***
```
for candidate_name in candidate_votes:
       
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
 ```
  ***b)' # Print each candidate's voter count and percentage to the terminal.***
   ```
        print(candidate_results)
        #  Export the candidate results to text file.
        txt_file.write(candidate_results)
```
  ***c)' # Determine winning vote count, winning percentage, and candidate.***
   ```      
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```

***4)‘Export the results to text file.***
 ```
outputfile = os.path.join("Analysis","election_analysis.text")    

with open(outputfile, "w") as txt_file:

 ```

