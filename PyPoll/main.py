# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Import the modules
import os
import csv

# Specify the file where you will base your calculation
ballot_file_path = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyPoll", "Resources", "election_data.csv")

# The total number of votes cast
with open(ballot_file_path) as ballot_file:
    read_ballot_file = csv.reader(ballot_file, delimiter=',')
    total_number_of_votes_cast = len(list(read_ballot_file)) - 1    # Subtracted by 1 to remove the header from the count
    
# A complete list of candidates who received votes
with open(ballot_file_path) as ballot_file:
    read_ballot_file = csv.reader(ballot_file, delimiter=',')
    # Exclude the header
    header = next(read_ballot_file)
    candidate_list = []
    for row in read_ballot_file:
        candidate_list.append(row[2])
    candidates = sorted(list(set(candidate_list)))  # Sorted the unique values from the candidate_list so that the list won't change in order of values everytime the script is run
    
# The total number of votes each candidate won
with open(ballot_file_path) as ballot_file:
    read_ballot_file = csv.reader(ballot_file, delimiter=',')
    # Exclude the header
    header = next(read_ballot_file)
    # Put a holder on the number of votes for each candidate
    votes_for_charles = []
    votes_for_diana = []
    votes_for_raymon = []
    for row in read_ballot_file:
        if row[2] == "Charles Casper Stockham":
            votes_for_charles.append(row[0])
        if row[2] == "Diana DeGette":
            votes_for_diana.append(row[0])        
        if row[2] == "Raymon Anthony Doane":
            votes_for_raymon.append(row[0])
    # Count the number of votes for each candidate
    total_votes_cast_for_charles = len(votes_for_charles)
    total_votes_cast_for_diana = len(votes_for_diana)
    total_votes_cast_for_raymon = len(votes_for_raymon)
   
# The percentage of votes each candidate won and format the results are percentage with 3 decimal places
percent_vote_for_charles = "{:.3%}".format(total_votes_cast_for_charles/total_number_of_votes_cast)
percent_vote_for_diana = "{:.3%}".format(total_votes_cast_for_diana/total_number_of_votes_cast)
percent_vote_for_raymon = "{:.3%}".format(total_votes_cast_for_raymon/total_number_of_votes_cast)

# The winner of the election based on popular vote
winner_dict = {}
winner_dict[candidates[0]] = total_votes_cast_for_charles
winner_dict[candidates[1]] = total_votes_cast_for_diana
winner_dict[candidates[2]] = total_votes_cast_for_raymon
winning_candidate = max(zip(winner_dict.values(), winner_dict.keys()))[1]   # Determine the largest vote count from dictionary

# Print the results to the terminal
print(f"Election Results")
print(f"---------------------------------")
print(f"Total Votes: ", total_number_of_votes_cast)
print(f"---------------------------------")
print(f"{candidates[0]}: {percent_vote_for_charles} ({total_votes_cast_for_charles})")
print(f"{candidates[1]}: {percent_vote_for_diana} ({total_votes_cast_for_diana})")
print(f"{candidates[2]}: {percent_vote_for_raymon} ({total_votes_cast_for_raymon})")
print(f"---------------------------------")
print(f"Winner: {winning_candidate}")
print(f"---------------------------------")

# Write the results to election_results.txt in analysis folder
output_path = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyPoll", "analysis", "election_results.txt")
with open(output_path, 'a') as textfile:
    textfile.write(f"Election Results")
    textfile.write(f"\n---------------------------------")
    textfile.write(f"\nTotal Votes: ")
    textfile.write(f"{total_number_of_votes_cast}")
    textfile.write(f"\n---------------------------------\n")
    textfile.write(f"{candidates[0]}: {percent_vote_for_charles} ({total_votes_cast_for_charles})\n")
    textfile.write(f"{candidates[0]}: {percent_vote_for_diana} ({total_votes_cast_for_diana})\n")
    textfile.write(f"{candidates[0]}: {percent_vote_for_raymon} ({total_votes_cast_for_raymon})\n")
    textfile.write(f"---------------------------------\n")
    textfile.write(f"Winner: {winning_candidate}\n")
    textfile.write(f"---------------------------------")