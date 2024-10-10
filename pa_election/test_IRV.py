import election

candidates = {0, 1, 2, 3}
#voter ID: {first_choice: candidateID, second_choice: candidateID,...}
# candidate IDs are 0, 1, 2, 3

# test ballot 1: there is a tie when two candidates left
ballot1 = {"v0": {1: 0, 2: 1, 3: 2, 4: 3}, 
          "v1": {1: 1, 2: 1, 3: 2, 4: 0},
          "v3": {1: 1, 2: 3, 3: 2, 4: 0}, 
          "v4": {1: 1, 2: 2, 3: 3, 4: 0},
          "v5": {1: 2, 2: 3, 3: 0, 4: 1},
          "v6": {1: 0, 2: 2, 3: 1, 4: 3},
          }

# test ballot 2: winner decided in the first round
ballot2 = {"v0": {1: 1, 2: 0, 3: 2, 4: 3}, 
          "v1": {1: 1, 2: 1, 3: 2, 4: 0},
          "v3": {1: 1, 2: 3, 3: 2, 4: 0}, 
          "v4": {1: 1, 2: 2, 3: 3, 4: 0},
          "v5": {1: 2, 2: 3, 3: 0, 4: 1},
          "v6": {1: 0, 2: 2, 3: 1, 4: 3},
          }

# test ballot 3: winner decided in the first round
ballot3 = {"v0": {1: 2, 2: 1, 3: 2, 4: 3}, 
          "v1": {1: 1, 2: 1, 3: 2, 4: 0},
          "v3": {1: 1, 2: 3, 3: 2, 4: 0}, 
          "v4": {1: 3, 2: 2, 3: 1, 4: 0},
          "v5": {1: 2, 2: 3, 3: 0, 4: 1},
          "v6": {1: 0, 2: 2, 3: 1, 4: 3},
          }

w = election.IRV(ballot3, candidates)
print(w)