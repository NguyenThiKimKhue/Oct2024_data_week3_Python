# -*- coding: UTF-8 -*-
"""PyPoll Homework Kim Nguyen File."""

import csv
import os

# Define the path to the CSV file
file_path = os.path.join("PyPoll/Resources/election_data.csv")

# Initialize variables to track the election data and define lists and dictionaries to track candidate names and vote counts
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Open the CSV file and process it
with open(file_path) as election_data:
    # Read the CSV file
    reader = csv.DictReader(election_data)
    
    # Loop through each row in the CSV
    for row in reader:
        total_votes += 1  # Count total votes
        
        candidate = row["Candidate"]  # Get the candidate's name
        
        # If the candidate is not in the dictionary, add them
        if candidate not in candidates:
            candidates[candidate] = 0
        
        candidates[candidate] += 1  # Increment the candidate's vote count

# Prepare the output
output_lines = []
output_lines.append(f"Total Votes: {total_votes}\n")

# Print candidates and their vote counts
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100  # Calculate percentage of votes
    output_lines.append(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    # Check for the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the winner
output_lines.append(f"Winner: {winner}\n")

# Print to terminal
for line in output_lines:
    print(line.strip())

# Write the output to a text file
with open('election_analysis_Kim.txt', 'w') as output_file:
    output_file.writelines(output_lines)
