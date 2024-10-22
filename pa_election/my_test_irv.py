import election

# candidates IDs: 0, 1, 2, 3
candidates = {0, 1, 2, 3}
#voter ID: {first_choice: candidateID, second_choice: candidateID,...}
# candidate IDs are 0, 1, 2, 3
A = 0
B = 1
C = 2
D = 3


# test ballot 1: there is a tie when two candidates left
ballot1 = {"v0": {1: A, 2: B, 3: C, 4: D},
          "v1":  {1: B, 2: A, 3: C, 4: A},
          "v3":  {1: B, 2: D, 3: C, 4: A},
          "v4":  {1: B, 2: C, 3: D, 4: A},
          "v5":  {1: C, 2: D, 3: A, 4: B},
          "v6":  {1: A, 2: C, 3: B, 4: D},
          }

# test ballot 2: winner decided in the first round
ballot2 = {"v0": {1: B, 2: A, 3: C, 4: D},
          "v1":  {1: B, 2: B, 3: C, 4: A},
          "v3":  {1: B, 2: D, 3: C, 4: A},
          "v4":  {1: B, 2: C, 3: D, 4: A},
          "v5":  {1: C, 2: D, 3: A, 4: B},
          "v6":  {1: A, 2: C, 3: B, 4: D},
          }

# test ballot 3: winner decided in the first round
ballot3 = {"v0": {1: C, 2: B, 3: A, 4: D},
          "v1": {1: B, 2: A, 3: C, 4: D},
          "v3": {1: B, 2: D, 3: C, 4: A},
          "v4": {1: D, 2: C, 3: B, 4: A},
          "v5": {1: C, 2: D, 3: A, 4: B},
          "v6": {1: A, 2: C, 3: B, 4: D},
          }

w = election.irv(ballot3, candidates)
print(w)
