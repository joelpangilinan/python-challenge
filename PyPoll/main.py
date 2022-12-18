# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Import the modules
import os
import csv

# Specify the file where you will calculate the results
ballot_file_path = os.path.join("C:/Users/Joel/Documents/UC-Berkeley-Boot-Camp/Weekly-assignments/module3/Starter_Code/Instructions/python-challenge/PyPoll", "Resources", "election_data.csv")

# The total number of votes cast
with open(ballot_file_path) as ballot_file:
    read_ballot_file = csv.reader(ballot_file, delimiter=',')
    total_number_of_votes_cast = len(list(read_ballot_file)) - 1
    print("Total votes cast: ", total_number_of_votes_cast)

# A complete list of candidates who received votes
with open(ballot_file_path) as ballot_file:
    read_ballot_file = csv.reader(ballot_file, delimiter=',')
    # Exclude the header
    header = next(read_ballot_file)
    candidate_list = []
    for row in read_ballot_file:
        candidate_list.append(row[2])
        candidates = sorted(list(set(candidate_list)))
    print(candidates)

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
    print("Total votes for Charles: ", total_votes_cast_for_charles)
    print("Total votes for Diana: ", total_votes_cast_for_diana)
    print("Total votes for Raymon: ", total_votes_cast_for_raymon)
    
# The percentage of votes each candidate won
percent_vote_for_charles = "{:.3%}".format(total_votes_cast_for_charles/total_number_of_votes_cast)
percent_vote_for_diana = "{:.3%}".format(total_votes_cast_for_diana/total_number_of_votes_cast)
percent_vote_for_raymon = "{:.3%}".format(total_votes_cast_for_raymon/total_number_of_votes_cast)
print("Percentage votes for charles: ", percent_vote_for_charles)
print("Percentage votes for diana: ", percent_vote_for_diana)
print("Percentage votes for raymon: ", percent_vote_for_raymon)

# The winner of the election based on popular vote
winner_dict = {}
winner_dict[candidates[0]] = total_votes_cast_for_charles
winner_dict[candidates[1]] = total_votes_cast_for_diana
winner_dict[candidates[2]] = total_votes_cast_for_raymon
winning_candidate = max(zip(winner_dict.values(), winner_dict.keys()))[1]
print(winning_candidate)

#Election Results
#  -------------------------
#  Total Votes: 369711
#  -------------------------
#  Charles Casper Stockham: 23.049% (85213)
#  Diana DeGette: 73.812% (272892)
#  Raymon Anthony Doane: 3.139% (11606)
#  -------------------------
#  Winner: Diana DeGette
#  -------------------------

# Print the results
print('Election Results')
print('---------------------------------')
print('Total Votes: ', total_number_of_votes_cast)
print('---------------------------------')
print(candidates[0], ': ', percent_vote_for_charles, ' (', total_votes_cast_for_charles, ')')
print(candidates[1], ': ', percent_vote_for_diana, ' (', total_votes_cast_for_diana, ')')
print(candidates[2], ': ', percent_vote_for_raymon, ' (', total_votes_cast_for_raymon, ')')
print('---------------------------------')
print('Winner: ', winning_candidate)
print('---------------------------------')