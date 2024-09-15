"""Odd Election driver.

Author: CS149 instructors
Version: 09/15/2024
"""
import odd_election

print("Welcome to the Dimmsdale Odd Elections!")
print("Here are the raw numbers for each candidate:")
print("Candidate\t\t\t\tNumber of Votes")
print("---------\t\t\t\t---------------")

# Candidates
cand1_name = "Chloe Carmichael"
cand2_name = "Timmy Turner"
cand3_name = "Denzel Crocker"
cand1_votes = 23
cand2_votes = 54
cand3_votes = 67
print(cand1_name + "\t\t\t\t" + str(cand1_votes))
print(cand2_name + "\t\t\t\t\t" + str(cand2_votes))
print(cand3_name + "\t\t\t\t\t" + str(cand3_votes))
print("---------\t\t\t\t---------------")


winnerPopVote = 5
winnerPopVote = odd_election.count_popular(cand1_votes, cand2_votes, cand3_votes)
print("Popular Vote Winner:", winnerPopVote)

winnerAbsMaj =  odd_election.count_majority(cand1_votes, cand2_votes, cand3_votes)
print("Absolute Majority Winner:", winnerAbsMaj)

winnerOdd =  odd_election.count_odd(cand1_votes, cand2_votes, cand3_votes)
print("Odd Winner:", winnerOdd)

winnerOdder =  odd_election.count_even_odder(cand1_votes, cand2_votes, cand3_votes)
print("Odder Winner:", winnerOdder)
