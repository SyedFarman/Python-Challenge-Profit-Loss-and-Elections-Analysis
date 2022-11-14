# Python-Challenge-Profit-Loss-and-Elections-Analysis
Python Challenge: PyBank-Profit &amp; Loss Analysis and PyPoll-Elections Analysis

# Profit And Loss Analysis
## Project Overview

In the project we are analysig financial records of the company,for the given period.
 
## Summary

After analysing the financials of the company, we can say that in last 86 months company has a profit of 22M, and has average change per month is -8,311.11, and we saw a greatest jump in the month of Aug-16 with 1.86M and lost change per month in Feb-14 with -1.82M

![Financial Analysis](https://user-images.githubusercontent.com/24644072/201574573-11016b2b-bae6-468c-8363-aadddfa0ef28.PNG)

!(Images/Financial Analysis.png)

***1.a)‘Set path for file.***
```
csv_path = os.path.join('Resources', 'budget_data.csv')
```
***b)‘# Initialize Total Months and Total.***
```
TotalMonths = 0
Total = 0
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
      TotalMonths = TotalMonths + 1
      Total += int(row[1])
 ```

***3)‘Export the results to text file.***
 ```
outputfile = os.path.join("Analysis","budget_analysis.text")
with open(outputfile, "w") as txt_file:

 ```

 # Election Analysis
## Project Overview

In the project we are analysig Election results of the small town.
 
## Summary

There were total 369,711 votes had been cast, and the Winner is Diana DeGette who received 73% votes that is equal to 272,892

![Election Result](https://user-images.githubusercontent.com/24644072/201574629-2bcc7046-7cbe-4c19-89ec-7a13f09b3b2d.PNG)
!(Images/Election Result.png)

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

