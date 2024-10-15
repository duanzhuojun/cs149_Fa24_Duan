"""Test the functions in election using  5 states in USA

The 5 States: New Jersey, Pennsylvania, Maryland, Virginia, and West Virginia
Reference: https://www.worldatlas.com/geography/mid-atlantic.html


Author: CS149 instructors
Version: 09/28/2024
"""
import election

allocation_per_state = {"VA": 13, "MD": 10, "WV": 4,
                        "NJ": 14, "PA": 19}

votes_per_state = {"VA": {0: 10, 1: 19, 2: 30},
                   "MD": {0: 30, 1: 10, 2: 4},
                   "WV": {0: 1, 1: 9, 2: 5},
                   "NJ": {0: 2, 1: 0, 2: 9},
                   "PA": {0: 11, 1: 11, 2: 0}}



def test_count_popular():
    count0=[10, 10, 1]
    count1=[2, 10, 1]
    count2=[-9, 10, 1]
    count3=[10, 2, 1]

    assert election.count_popular(count0) == -2
    assert election.count_popular(count1) == 1
    assert election.count_popular(count2) == -1
    assert election.count_popular(count3) == 0
    print("count_popular function looks good")

def test_count_majority():
    count0=[10, 10, 1, 2] # Tie: -2
    count1=[2, 10, 1, 1] # winner is 1
    count2=[-9, 10, 1, 1] # invalid value: -1
    count3=[4, 2, 1, 1] # not majority
    count4=[5, 2, 1, 1] # not majority

    assert election.count_majority(count0) == -2
    assert election.count_majority(count1) == 1
    assert election.count_majority(count2) == -1
    assert election.count_majority(count3) == -3
    assert election.count_majority(count4) == 0
    print("count_majority function looks good")

candidates = {0, 1, 2, 3}


# w = election_list.IRV(ballot, candidates)
# print(w)
# count_popular_test()
test_count_majority()


# w = election.count_majority([-1, 6, -1, -1])
# print(w)
