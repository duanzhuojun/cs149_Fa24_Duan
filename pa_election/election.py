"""Complete Election Tools.

Author: CS149 instructors
Version: 09/17/2024
"""
import math


def count_popular(vote_counts):
    """Find the popular vote.

    Popular vote - the candidate with the highest number of votes wins, and
    ties result in an invalid election.

    Args:
        vote_counts (list): votes the number of votes each candidate received.

    Returns:
        int: index of the winning candidate, or -1 if invalid, -2 if a tie
    """
    popular = -math.inf
    win = -1
    tie = False

    # find the maximum
    for i in range(len(vote_counts)):
        # invalid argument
        if vote_counts[i] < 0:
            return -1
        # current max is a tie
        if (vote_counts[i] == popular):
            tie = True
        # found a new max value
        if (vote_counts[i] > popular):
            popular = vote_counts[i]
            win = i
            tie = False

    # return the winner, unless it's a tie
        if tie:
            win = -2

    return win


def count_majority(vote_counts):
    """Find the majority vote.

    Absolute majority - the candidate with the highest number of votes wins,
    but only if the number of votes is at least 50% of all votes cast in the
    election. If the highest number of votes is not a majority or there is a
    tie, the election is invalid.

    Args:
        vote_counts (list): votes the number of votes each candidate received

    Returns:
        int: index of the winning candidate, or -1 if invalid, -2 if a tie
    """
    # first get the winner
    win = count_popular(vote_counts)
    # invalid argument or tie
    if win < 0:
        return win

    # add up the votes
    total = 0
    for vote in vote_counts:
        total = total + vote

    # check for majority
    if vote_counts[win] <= 0.5 * total:
        win = -3

    return win


def electoral_votes(votes_per_state, allocation_per_state):
    """Find the overall winner of the state-wide popular vote.

    Electoral votes - there are 538 electoral votes, and a candidate
    needs a majority of 270 electoral votes to win the presidency.
    Most states use a "winner-takes-all" system, meaning the candidate
    who wins the popular vote in a state typically receives all of that
    state's electoral votes, with exceptions in Maine and Nebraska,
    which use a proportional system.

    Args:
        votes_per_state (dict): the number of votes each candidate received per state
        allocation_per_state (dict): votes are distributed across several key states

    Returns:
        int: index of the winning candidate, or -1 if invalid
    """
    # find the winner candidate of states using count_popular
    states_winner = dict()
    for state in votes_per_state:
        votes = votes_per_state[state]
        state_winner = count_popular(votes)
        states_winner[state] = state_winner

    # Assume 4 candidates
    # calculate votes per candidates using the allocations per state
    final_votes = [0, 0, 0, 0]
    for state in states_winner:
        c = states_winner[state]
        if c >= 0:
            final_votes[c] = final_votes[c] + allocation_per_state[state]

    # use the  count_majority to find the winner
    print(final_votes)
    final_winner  = count_majority(final_votes)
    return final_winner


def IRV(ballot, candidates):
    """ Find the winner using Instant-runoff voting (IRV)

    reference: https://www.findlaw.com/voting/how-u-s--elections-work/instant-runoff-voting--how-does-it-work.html

    Args:
        ballot (dict): voters' preference over candidates
        candidates (set): candidate IDs
    """
    # candidates_set = candidates.copy()
    removed_candidates = set()
    winner = -1

    # while winner == -1 or len(removed_candidates) < 4:
    for round in range(4):
        # build a list where each item is the vote counts of a candidate
        first_choice = [0] * len(candidates)
        for rc in removed_candidates:
            first_choice[rc] = 0

        for voter in ballot:
            preference = ballot[voter]
            top = preference[1]
            i = 1
            while (top in removed_candidates and i <= 4):
                top = preference[i]
                i = i + 1
            first_choice[top] = first_choice[top] + 1
        print(first_choice)
        # Any one has a majority? If so, return the winner
        winner = count_majority(first_choice)
        if winner >= 0:
            return winner
        # two candidates left and there is a tie
        if winner == -2 and len(removed_candidates) == 2:
            break
        # Make elimination
        # Find the candidate has the fewest first-place
        fewest_counts = float('inf')
        fewest_candidate_index = -1

        for index, count in enumerate(first_choice):
            if index in removed_candidates:
                continue
            if count < fewest_counts:
                fewest_counts = count
                fewest_candidate_index = index
        # elimination
        removed_candidates.add(fewest_candidate_index)
        print(removed_candidates)

    # Handle the tie:
    if winner == -2:
        candidate_left = candidates.difference(removed_candidates)
        left = list(candidate_left)
        # check all other choices:
        second_choice = [0] * len(candidates)
        third_choice = [0] * len(candidates)
        fourth_choice = [0] * len(candidates)
        for voter in ballot:
            preference = ballot[voter]
            # print(preference)
            second_choice[preference[2]] += 1
            third_choice[preference[3]] += 1
            fourth_choice[preference[4]] += 1
        # print("second:", second_choice)
        # print("third:", third_choice)
        # print("forth:", fourth_choice)
        temp = -2
        # print(left)
        if second_choice[left[0]] > second_choice[left[1]]:
            temp = left[0]
        elif second_choice[left[0]] < second_choice[left[1]]:
            temp = left[1]

        if temp == -2:
            if third_choice[left[0]] > third_choice[left[1]]:
                temp = left[0]
            elif third_choice[left[0]] < third_choice[left[1]]:
                temp = left[1]

        if temp == -2:
            if fourth_choice[left[0]] > fourth_choice[left[0]]:
                temp = left[0]
            elif fourth_choice[left[0]] < fourth_choice[left[0]]:
                temp = left[1]
        winner = temp
    return winner
