import unittest
from election import *
class TestElection(unittest.TestCase):
    test_nums = [1, 3, 5, 6, 8, 2, 1]

    def test_count_popular(self):
        count0=[10, 10, 1]
        count1=[2, 10, 1]
        count2=[-9, 10, 1]
        count3=[10, 2, 1]

        assert count_popular(count0) == -2, "Test tie"
        assert count_popular(count1) == 1, "Test valid winner"
        assert count_popular(count2) == -1, "Test invalid count"
        assert count_popular(count3) == 0, "Test valid winner"

    def test_count_majority(self):
        count0=[10, 10, 1, 2] # Tie: -2
        count1=[2, 10, 1, 1] # winner is 1
        count2=[-9, 10, 1, 1] # invalid value: -1
        count3=[3, 2, 1, 1] # not majority
        count4=[5, 2, 1, 1] # winner is 0
        count5=[1, 2, 1, 4] # winner is 3

        assert count_majority(count0) == -2, "Test tie"
        assert count_majority(count1) == 1, "Test valid winner"
        assert count_majority(count2) == -1, "Test invalid count"
        assert count_majority(count3) == -3, "Test not majority"
        assert count_majority(count4) == 0, "Test valid winner"
        assert count_majority(count5) == 3, "Test valid winner"


if __name__ == "__main__":
    unittest.main()
