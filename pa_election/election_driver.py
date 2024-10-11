"""Election driver.

Author: CS149 instructors
Version: 09/15/2024
"""
import election
import vote_file_processor

raw_ballot_file = ".\\data\\raw_ballot.csv"
electoral_data = ".\\data\\Electoral_College.json"

print("======Welcome to the JMU election simulator!======\n\n")
print("We will have 4 president candidates:")
print("Candidate Name\t\t\t\tCandidate ID")
print("---------------\t\t\t\t---------------")

# Candidates
candidates = {0: "Chloe Carmichael",
              1: "Timmy Turner",
              2: "Denzel Crocker",
              3: "Alexandra Bennett"}

for id in candidates:
    print(f"{candidates[id]:<15}\t\t\t\t{id:5}")


print("Here are the results of different election methods: ")


vote_counts = vote_file_processor.read_first_choice(raw_ballot_file)
winner = election.count_popular(vote_counts)
print(winner)
