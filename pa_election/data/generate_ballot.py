"""Generate the fake ballot data 

Author: CS149 instructors
Version: 10/08/2024
"""
import random

def create_states():
    states = set()
    file = open("Electoral_College.csv")
    for line in file.readlines()[1:]:
        lst = line.split(",")
        states.add(lst[1])
    file.close()
    print(states)    

states = {'ND', 'MT', 'GA', 'KS', 'PA', 'DE', 'NV', 'NY', 'ME', 'MI', 'NE', 'SC', 'MO', 'AK', 'NH', 'NJ', 'CT', 'WA', 'IL', 'WV', 'DC', 'AR', 'NC', 'MA', 'TX', 'MN', 'MS', 'TN', 'ID', 'OH', 'OR', 'VT', 'MD', 'WI', 'OK', 'SD', 'KY', 'RI', 'CA', 'CO', 'FL', 'LA', 'IN', 'IA', 'WY', 'UT', 'NM', 'AL', 'AZ', 'VA', 'HI'}   

states_list = list(states)
def create_fake_ballot_csv():
    out = open("raw_ballot.csv", "w")
    out.write("voterID, State, A, B, C, D\n")
    preference = [1,2,3,4]
    for i in range(1000):
        random.shuffle(preference)
        line = f"Voter{i}, {random.choice(states_list)}, {', '.join(map(str, preference))}"
        out.write(line + "\n")
    out.close()
create_fake_ballot_csv()    