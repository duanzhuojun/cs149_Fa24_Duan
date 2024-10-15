import election

allocation_per_state = {"VA": 13, "MD": 10, "WV": 4,
                        "NJ": 14, "PA": 19}

votes_per_state = {"VA": [10, 12, 13, 14],
                   "MD": [10, 1, 1, 10],
                   "WV": [10, 9, 8, 7],
                   "NJ": [-1, 0, 0, 10],
                   "PA": [3, 1, 2, 1]}

votes_per_state1 = {"VA": [0, 0, 0, 1],
                    "MD": [1, 0, 0, 0],
                    "WV": [0, 1, 0, 0],
                    "NJ": [0, 1, 0, 0],
                    "PA": [1, 0, 0, 1]}

w = election.electoral_votes(votes_per_state1, allocation_per_state)
print(w)
