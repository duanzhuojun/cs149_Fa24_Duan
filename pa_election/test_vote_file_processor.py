import io
import math
import contextlib
import json
from gradescope_utils.autograder_utils.decorators import weight
from jmu_gradescope_utils import JmuTestCase, required
from election import *
from vote_file_processor import *


FILENAME = 'vote_file_processor.py'
TEST_DOCSTRINGS = True
MAX_SUBMISSIONS = 10
class TestFileProcessor(JmuTestCase):

    @required()
    @weight(0)
    def test_submitted_files(self):
        """Check submitted files"""
        self.assertRequiredFilesPresent([FILENAME])

        # test docstring
        if TEST_DOCSTRINGS:
            self.assertDocstringsCorrect(FILENAME)

        # Submission count
        try:
            meta = json.load(open("/autograder/submission_metadata.json"))
        except FileNotFoundError:
            print("WARNING: metadata not found (please notify your instructor)")
            return  # This error should happen only when testing the autograder

        count = 1 + len(meta["previous_submissions"])
        print(f"Submission {count} of {MAX_SUBMISSIONS}")
        if count > MAX_SUBMISSIONS:
            self.fail("Limit exceeded. Please click the Submission History button "
                      "and activate the submission you would like us to grade.\n")

        # Check requirements
        self.assertMatchCount(FILENAME, r"\bcount\(", 0, "Calls to count are not allowed")
        self.assertMatchCount(FILENAME, r"\bCounter\(", 0, "Use of the Counter collection is not allowed")

        # PEP 8 checks
        self.assertPassesPep8(FILENAME)

    @weight(7)
    def test_read_first_choice(self):
        raw_ballot_file = "test_data/raw_ballot.csv"
        raw_ballot_file_5 = "test_data/raw_ballot_5.csv"
        raw_ballot_file_100 = "test_data/raw_ballot_100.csv"
        expect = [306, 839, 337, 818]
        self.assertTrue(read_first_choice(raw_ballot_file) == expect, "Test big ballot file")

        expect2 = [0, 2, 2, 1]
        self.assertTrue(read_first_choice(raw_ballot_file_5) == expect2, "Test small ballot file")

        expect3 = [27, 30, 27, 16]
        self.assertTrue(read_first_choice(raw_ballot_file_100) == expect3, "Test median size ballot file")
