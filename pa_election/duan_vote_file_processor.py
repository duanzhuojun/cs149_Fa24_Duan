import unittest
from vote_file_processor import *

class TestFileProcessor(unittest.TestCase):
    test_nums = [1, 3, 5, 6, 8, 2, 1]

    def test_read_first_choice(self):
        raw_ballot_file = "data/raw_ballot.csv"
        raw_ballot_file_5 = "data/raw_ballot_5.csv"
        raw_ballot_file_100 = "data/raw_ballot_100.csv"

        assert read_first_choice("no_path.py", "") == -1, "Path does not exist"

        expect = [306, 839, 337, 818]
        assert read_first_choice("data/raw_ballot.csv", ",") == expect, "Test big ballot file"

        expect2 = [0, 2, 2, 1]
        # test , as the delimiter
        assert read_first_choice(raw_ballot_file_5, ",") == expect2, "Test small ballot file"
        # test space as the delimiter
        assert read_first_choice("data/raw_ballot_5.txt", " ") == expect2, "Test space as the delimiter v1"

        expect3 = [27, 30, 27, 16]
        assert read_first_choice(raw_ballot_file_100, ",") == expect3, "Test median size ballot file"

        # test space as the delimiter
        expect4 = [1, 6, 2, 1]
        assert read_first_choice("data/raw_ballot_10.txt", " ") == expect4, "Test space as the delimiter v2"




if __name__ == "__main__":
    unittest.main()
