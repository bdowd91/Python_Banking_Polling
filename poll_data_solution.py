# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:52:07 2019

@author: Brendan Dowd
"""

import os
import csv

poll_data_input = os.path.join("..", "Desktop", "poll_data.csv")
poll_data_output = os.path.join("..", "Desktop", "poll_data_output.py")

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(poll_data_input) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)
    for row in reader: 
            print(".", end=""), 
            total_votes = total_votes + 1
            candidate_name = row[2]
            if candidate_name not in candidate_options: 
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
            
with open(file_to_output, "w") as txt_file: 
    election_results = (
            f"\n\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n")
    print(election_results, end="")
    
    txt_file.write(election_results)
    
    for candidate in candidate_votes: 
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        if (votes > winning_count): 
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f"{candidate}: {vote_percentage:.df}% ({votes})\n"
        print(voter_output, ends="")
        
        txt_file.write(voter_output)
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)
        