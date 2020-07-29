# Data we need to retrieve.
# 1. Total number of votes cast = 369,711
# 2. A complete list of candidates who received votes = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
# 3. Total number of votes each candidate received = {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
# 4. Percentage of votes each candidate won = Charles Casper Stockham: received 23.0% of the vote. Diana DeGette: received 73.8% of the vote. Raymon Anthony Doane: received 3.1% of the vote.
# 5. The winner of the election based on popular vote = Diana DeGette: 73.8% (272,892)

# Add our dependencies
import csv
import os
# assign a variable to load a file from an -indirect- path
# DIRECT PATH use, file_to_load = 'resources/election_results.csv'
file_to_load = os.path.join("resources", "election_results.csv")
# assign a variable to save the file to an -indirect- path.
# DIRECT PATH use, file_to_save = 'analysis/election_analysis.txt'
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialise a total vote counter 
total_votes = 0
# initialise candidate options list
candidate_options = []
# declare empty dict for candidate: votes
candidate_votes = {}
# track winning candidate, winning count tracker, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
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
            # and start tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's vote count
        candidate_votes[candidate_name] += 1

# save the results to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f'\n'
        f'Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')
    print(election_results, end="")

    # save the final vote count to the text file
    txt_file.write(election_results)

    # determine percentage of votes for each candidate by looping through the counts
    # iterate through the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count of the candidate
        votes = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # print each candidate's name, vote count, and percentage of votes
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results)
        # save candidate_results to the text file
        txt_file.write(candidate_results)

        # determine winning vote count, percentage, and candidate
        # if votes are greater than the winning count ..
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # set winning_count = votes and winning_percentage = vote_percentage
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

    # save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
