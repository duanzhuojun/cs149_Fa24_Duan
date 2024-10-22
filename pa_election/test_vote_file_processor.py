import unittest
from vote_file_processor import *

class TestFileProcessor(unittest.TestCase):
    test_nums = [1, 3, 5, 6, 8, 2, 1]

    def test_read_first_choice(self):
        raw_ballot_file = "data/raw_ballot.csv"

        print(read_first_choice(raw_ballot_file))




if __name__ == "__main__":
    unittest.main()
