"""Unit tests for review exercises."""

import json
import os
import random

PATH = "data/fulltracks.json"
with open(PATH) as file:
    DATA = json.load(file)

A = """
Quiz 5
* Chapter 9: Sequences
* Chapter 10: File I/O
Quiz 6
* Chapter 11: Nested Data
* Chapter 12: Recursion
"""

B = """
Quiz 5
    * Chapter 9: Sequences
    * Chapter 10: File I/O
Quiz 6
    * Chapter 11: Nested Data
    * Chapter 12: Recursion
"""


def test_ch09():

    from ch09 import indent_stars
    assert indent_stars(A) == B

    from ch09 import unindent_stars
    assert unindent_stars(B) == A


def test_ch10():

    from ch10 import search_file
    assert search_file(PATH, "CS149") is None
    assert search_file(PATH, "NOID") == (3, 18)
    assert search_file(PATH, "Rah+Tah+Tah") == (72, 64)
    assert search_file(PATH, "new wave") == (186, 30)
    assert search_file(PATH, "fourteenth") == (1180, 66)

    from ch10 import strip_file
    testfile = "test_ch10.txt"
    line_cnt = 10
    with open(testfile, "w") as file:
        for i in range(line_cnt):
            spaces = random.randint(0, 20)
            file.write(f"Line {i+1}" + " "*spaces + "\n")
    strip_file(testfile)
    with open(testfile) as file:
        lines = file.readlines()
        assert len(lines) == line_cnt
        for i in range(line_cnt):
            assert lines[i] == f"Line {i+1}\n"
    os.remove(testfile)


def test_ch11(capsys):

    from ch11 import print_stats
    print_stats("Letters:", {"A", "BB", "CCC", "DDD"})
    out, err = capsys.readouterr()
    assert out == "Letters: min = 1.0, median = 2.5, mean = 2.2, max = 3.0\n"
    assert err == ""

    from ch11 import track_stats
    track_stats(DATA)
    out, err = capsys.readouterr()
    assert out == (
        "Track names: min = 3.0, median = 11.5, mean = 16.6, max = 59.0\n"
        "Artist names: min = 3.0, median = 10.5, mean = 10.6, max = 18.0\n"
        "Album titles: min = 3.0, median = 12.0, mean = 14.6, max = 39.0\n"
    )
    assert err == ""


def test_ch12():

    from ch12 import search_json
    assert search_json(DATA, "CS149") is None
    assert search_json(DATA, "NOID") == "data[0]['name']"
    assert search_json(DATA, "Rah+Tah+Tah") == "data[1]['url']"
    assert search_json(DATA, "new wave") == "data[2]['toptags']['tag'][2]['name']"
    assert search_json(DATA, "fourteenth") == "data[19]['wiki']['summary']"
