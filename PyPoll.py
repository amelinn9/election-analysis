# Data we need to retrieve.
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Assign a variable for the file to load and the path. DIRECT PATH
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

# open the election results and read the file
with open(file_to_load) as election_data:

    # To-do: read and analyse the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read and print the header row
    headers = next(file_reader)
    print(headers)

    # print each row in the CSV file excluding headers
    for row in file_reader:
        print(row)



# ------------------------------------------------------------------------------------------------------------------    
    # print the file object
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = 'analysis/election_analysis.txt'
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement, open the file as a text file
#with open(file_to_save, "w") as txt_file:
    # write three counties to the file
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")


    