# Data we need to retrieve.
# 1. Total number of votes cast = 369,711
# 2. A complete list of candidates who received votes = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
# 3. Total number of votes each candidate received = {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
# 4. Percentage of votes each candidate won = Charles Casper Stockham: received 23.0% of the vote. Diana DeGette: received 73.8% of the vote. Raymon Anthony Doane: received 3.1% of the vote.
# 5. The winner of the election based on popular vote = Diana DeGette: 73.8% (272,892)


# Assign a variable for the teamfile to load and the path. DIRECT PATH
file_to_load = 'resources/election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:
# To-do: perform analysis
    print(election_data)

# Add our dependencies
import csv
import os
# assign a variable to load a file from a direct path
file_to_load = 'resources/election_results.csv'
# assign a variable to save the file to a direct path.
file_to_save = 'analysis/election_analysis.txt'

# initialise a total vote counter 
total_votes = 0

# initialise candidate options
candidate_options = []

# declare empty dict for candidate: votes
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
    # To-do: read and analyse the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # print each row in the CSV file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1

        # print candidate name from each row
        candidate_name = row[2]

        # add the candidate name to the candidate list
        # if the candidate does not match any existing candidate..
        if candidate_name not in candidate_options:
            # add name to the list of candidates
            candidate_options.append(candidate_name)
            # start tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

# determine percentage of votes for each candidate by looping through the counts
# iterate through the candidate list
for candidate_name in candidate_votes:
    # retrieve vote count of the candidate
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # to print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

    # determine winning vote count and candidate
    # determine if votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # set the winning_candidate to the candidate's name
        winning_candidate = candidate_name

# print the winning candidate, vote count and percentage
winning_candidate_summary = (
    f'---------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'---------------------------\n')
print(winning_candidate_summary)
