"""Process the raw ballot related files

Author: CS149 instructors
Version: 10/11/2024
"""

# Read the candidates' first choice counts 
# Should be the input for count_popular function and count_majority function
import json

def read_first_choice(ballot_file):
    """Read first choice counts from raw ballot file

    Args:
        ballot_file (String): path to the raw ballot file
    
    Returns:
        list: the candidates' first choice counts
    """
    voter_count = [0] * 4
    file = open(ballot_file, "r")
    for line in file.readlines()[1: ]:
        items = line.split(",")
        votes = [int(i) for i in items[2:]]
        first = votes.index(1)
        voter_count[first] += 1
    
    return voter_count

# Read the candidates' first choice counts per state
# Should be the input for electoral_votes function
def read_first_choice_per_state(ballot_file):
    """Read the candidates' first choice counts per state.

    Args:
        ballot_file (String): path to the raw ballot file

    Returns:
        dict: the candidates' first choice counts per state
    """
    votes_per_state = dict()
    file = open(ballot_file, "r")
    for line in file.readlines()[1: ]:
        items = line.split(",")
        state = items[1].strip()
        votes = [int(i) for i in items[2:]]
        first = votes.index(1)
        if state in votes_per_state:
            votes_per_state[state][first]  += 1
        else:
            votes_per_state[state] = [0] * 4
            votes_per_state[state][first]  += 1
    
    return votes_per_state

# Read the complete ballot
# Should be the input for IRV function   
def read_complete_ballot(ballot_file):
    """Read the complete ballot as a dict

    Args:
        ballot_file (String): path to the raw ballot data

    Returns:
        dict: complete ballot data as a dict
    """
    ballot = dict()
    file = open(ballot_file, "r")
    for line in file.readlines()[1: ]:
        items = line.split(",")
        votes = [int(i) for i in items[2:]]
        ballot[items[0]] = dict()
        for choice, rank in enumerate(votes):
            ballot[items[0]][rank] = choice
    
    return ballot

def read_electoral_college(electoral_file):
    """Read the electoral votes from a JSON file

    Args:
        electoral_file (String): path to the JSON file

    Returns:
        dict: electoral votes
    """
    # Opening JSON file
    with open(electoral_file, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        return json_object
 

    
    
            
    

if __name__ == "__main__":       
    r = read_first_choice("data/raw_ballot.csv")
    r2 = read_first_choice_per_state("data/raw_ballot.csv")
    r3 = read_complete_ballot("data/raw_ballot.csv")
    r4 = read_electoral_college("data/Electoral_College.json")
    # print(r2)
    
    