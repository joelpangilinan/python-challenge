import os
import csv

# Path to the election data file
election_data_path = os.path.join("Resources", "election_data.csv")

# Initialize variables to store the analysis results
total_votes = 0
candidates = {}
winner = ""

# Read the election data file
with open(election_data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    next(csvreader)
    # Loop through the data rows
    for row in csvreader:
        # Increment the total number of votes
        total_votes += 1
        # Get the candidate name from the row
        candidate = row[2]
        # If this is the first vote for this candidate, add them to the dictionary
        if candidate not in candidates:
            candidates[candidate] = 0
        # Increment the vote count for this candidate
        candidates[candidate] += 1

# Analyze the vote counts for each candidate
candidate_results = []
for candidate, votes in candidates.items():
    # Calculate the percentage of votes this candidate won
    vote_percentage = round((votes / total_votes) * 100, 3)
    # Add this candidate's results to the list
    candidate_results.append((candidate, vote_percentage, votes))
    # Check if this candidate has the most votes so far
    if winner == "" or votes > candidates[winner]:
        winner = candidate

# Print the analysis results to the console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate_result in candidate_results:
    print(f"{candidate_result[0]}: {candidate_result[1]}% ({candidate_result[2]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the analysis results to a text file
output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate_result in candidate_results:
        txtfile.write(f"{candidate_result[0]}: {candidate_result[1]}% ({candidate_result[2]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
