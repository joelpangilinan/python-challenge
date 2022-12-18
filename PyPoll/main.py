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
percent_vote_for_charles = (float(total_votes_cast_for_charles) / float(total_number_of_votes_cast)) * 100
percent_vote_for_diana = (float(total_votes_cast_for_diana) / float(total_number_of_votes_cast)) * 100
percent_vote_for_raymon = (float(total_votes_cast_for_raymon) / float(total_number_of_votes_cast)) * 100
print("Percentage votes for charles: ", percent_vote_for_charles)
print("Percentage votes for diana: ", percent_vote_for_diana)
print("Percentage votes for raymon: ", percent_vote_for_raymon)








#with open(filepath) as budget_file:
#    read_budget = csv.reader(budget_file, delimiter=',')
    # Exclude the header
#    header = next(read_budget)
#    profit = []
#    for row in read_budget:
#        profit.append(int(row[1]))
    
#    values = [x for x in profit]
#    max_profit = max(values)
#    min_profit = min(values)
    #print(max_profit)
    #print(min_profit)
    