"""Election driver.

Author: CS149 instructors
Version: 09/15/2024
"""
import election
import vote_file_processor

raw_ballot_file = "data/raw_ballot.csv"
electoral_file = "data/Electoral_College.json"

print("======Welcome to DukeVote: JMU Election Simulator======\n\n")
print("We will have 4 president candidates:")
print("Candidate Name\tCandidate ID")
print("---------------\t---------------")

# Candidates
candidates = {0: "Chloe Carmichael",
              1: "Timmy Turner",
              2: "Denzel Crocker",
              3: "Alexandra Bennett"}
print("Chloe Carmichael      ", 0)
print("Timmy Turner          ", 1)
print("Denzel Crocker        ", 2)
print("Alexandra Bennett     ", 3)


print("\n\n")
print("==Here are the results of different election methods:==")
print("-------------------------------------------------------")
print("Election method\t\t\tWinner name")
print("--------------------\t\t---------------------------")
vote_counts = vote_file_processor.read_first_choice(raw_ballot_file)
winner_popular = election.count_popular(vote_counts)
if winner_popular >= 0:
    print(f"Count Popular   \t\t{candidates[winner_popular]}")
else:
    print(f"Count Popular   \t\tInvalid")
winner_majority = election.count_majority(vote_counts)
if winner_majority >= 0:
    print(f"Count Majority   \t\t{candidates[winner_majority]}")
else:
    print(f"Count Majority   \t\tInvalid")

vote_counts_states = vote_file_processor.read_first_choice_per_state(raw_ballot_file)
electoral_college = vote_file_processor.read_electoral_college(electoral_file)

winner_electoral = election.electoral_votes(vote_counts_states, electoral_college)
if winner_electoral >= 0:
    print(f"Electoral Vote   \t\t{candidates[winner_electoral]}")
else:
    print(f"Electoral Vote   \t\tInvalid")
    
ballot = vote_file_processor.read_complete_ballot(raw_ballot_file)
winner_irv = election.IRV(ballot, {0,1,2,3})
if winner_irv >= 0:
    print(f"IRV              \t\t{candidates[winner_irv]}")
else:
    print(f"IRV               \t\tInvalid")
print("-------------------------------------------------------")