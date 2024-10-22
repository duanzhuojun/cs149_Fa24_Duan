import election

# candidates IDs: 0, 1, 2, 3
candidates = {0, 1, 2, 3}
#voter ID: {first_choice: candidateID, second_choice: candidateID,...}
# candidate IDs are 0, 1, 2, 3
A = 0
B = 1
C = 2
D = 3




# test ballot 1:
ballot1 = {"v0":  {1: B, 2: A, 3: C, 4: D},
           "v1":  {1: B, 2: B, 3: C, 4: A},
           "v2":  {1: B, 2: D, 3: C, 4: A},
           "v3":  {1: B, 2: C, 3: D, 4: A},
           "v4":  {1: C, 2: D, 3: A, 4: B},
           "v5":  {1: A, 2: C, 3: B, 4: D},
          }

# test ballot 2:
ballot2 = {"v0": {1: D, 2: B, 3: A, 4: C},
           "v1": {1: B, 2: A, 3: C, 4: D},
           "v2": {1: B, 2: D, 3: C, 4: A},
           "v3": {1: C, 2: D, 3: B, 4: A},
           "v4": {1: C, 2: D, 3: A, 4: B},
           "v5": {1: A, 2: C, 3: B, 4: D},
          }

#
ballot3 = {"v0": {1: A, 2: B, 3: C, 4: D},
          "v1":  {1: B, 2: A, 3: C, 4: A},
          "v3":  {1: B, 2: D, 3: C, 4: A},
          "v4":  {1: B, 2: C, 3: D, 4: A},
          "v5":  {1: C, 2: D, 3: A, 4: B},
          "v6":  {1: A, 2: C, 3: B, 4: D},
          "v7":  {1: B, 2: D, 3: C, 4: A}
          }

w = election.irv(ballot3, candidates)
print(w)
