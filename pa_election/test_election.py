import io
import math
import contextlib
import json
from gradescope_utils.autograder_utils.decorators import weight
from jmu_gradescope_utils import JmuTestCase, required
from election import *


FILENAME = 'election.py'
TEST_DOCSTRINGS = True
MAX_SUBMISSIONS = 10

class TestElection(JmuTestCase):

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

    @weight(2)
    def test_count_popular(self):
        count0=[10, 10, 1]
        count1=[2, 10, 1]
        count2=[-9, 10, 1]
        count3=[10, 2, 1]

        self.assertTrue(count_popular(count0) == -2, "Test tie")
        self.assertTrue(count_popular(count1) == 1, "Test valid winner")
        self.assertTrue(count_popular(count2) == -1, "Test invalid count")
        self.assertTrue(count_popular(count3) == 0, "Test valid winner")

    @weight(5)
    def test_count_majority(self):
        count0=[10, 10, 1, 2] # Tie: -2
        count1=[2, 10, 1, 1] # winner is 1
        count2=[-9, 10, 1, 1] # invalid value: -1
        count3=[3, 2, 1, 1] # not majority
        count4=[5, 2, 1, 1] # winner is 0
        count5=[1, 2, 1, 4] # winner is 3

        self.assertTrue(count_majority(count0) == -2, "Test tie")
        self.assertTrue(count_majority(count1) == 1, "Test valid winner")
        self.assertTrue(count_majority(count2) == -1, "Test invalid count")
        self.assertTrue(count_majority(count3) == -3, "Test not majority")
        self.assertTrue(count_majority(count4) == 0, "Test valid winner")
        self.assertTrue(count_majority(count5) == 3, "Test valid winner")
