import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

# Initialize a total vote counter,Candidate Options and candidate votes.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # Read the header
    header = next(csvreader)

    # For each row in the CSV file.
    for row in csvreader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to candidate list       
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
# Export the results to text file.
outputfile = os.path.join("Analysis","election_analysis.text")    

with open(outputfile, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        )
    print(election_results, end="")

    txt_file.write(election_results)
  
    # Export the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Export the candidate results to text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
                
        f"-------------------------\n")
    print(winning_candidate)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate)
