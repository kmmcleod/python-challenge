# Create file paths across operating systems
import os

# Module for reading CSV files
import csv

election_csv = os.path.join('Resources','election_data.csv')

candidates = []
num_votes = 0
vote_counts = []

# List files 
election_data = ['1', '2']

# Read CSV file
with open(election_csv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Skip header
    header=next(csvreader)

# Process the votes
    for line in csvreader:

        # Count the total number of votes
        num_votes = num_votes + 1

        # The candidate voted for
        candidate = line[2]

        # If the candidate has other votes then add to vote total
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        # Else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

    # Create variables
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    # Percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/num_votes*100
        percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
    winner = candidates[max_index]

# Round decimal

percentages = [round(i,2) for i in percentages]

# Print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# Name write file
output_file = election_csv[0:-4]

write_election_csv = f"{output_file}_results.txt"

# Open write file
filewriter = open(write_election_csv, mode = 'w')

# Print to write file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {num_votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

# Close file
filewriter.close()

    