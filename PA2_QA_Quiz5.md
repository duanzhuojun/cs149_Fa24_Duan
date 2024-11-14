## Announcements
1. [PA 2 World of Elections](https://w3.cs.jmu.edu/cs149/f24/pa/pa2/)
- Part A - Reading quiz in canvas - Done.
- Part B due Friday 11/08 - Done.
- Part C due Friday 11/15 (60 pts)
2. [Project 3](https://w3.cs.jmu.edu/cs149/f24/pa/pa3/) (due Dec 03)
- Part A due Tuesday, 11/19
- Part B due Friday, 11/22
- Part C due Wednesday, 12/04
- Main Idea
    - Read last.fm data from json files
    - Build playlists and find new songs
    - PA 3 specification and [sample data](https://w3.cs.jmu.edu/cs149/f24/pa/pa3/stubs/sample_data.py)

## Today's class
1. (20 mins) Load JSON file
2. (25 mins) PA2 QA
3. (30 mins) Quiz 5

### JSON file
A JSON file stores data in key-value pairs and arrays. There may be a dictionary or a list at the top level.
JSON allows developers to store various data types as human-readable code, with the keys serving as names and the values containing related data.

**In order to understand the structure of the data in these files, you can either open the files in VS Code and format them, you can open them in Chrome and Chrome can format them, or you can go to one of many JSON pretty print websites such as jsonformatter.org and paste the data there for formatting.**

### JSON Data example:
- JSON sample files [download](https://support.oneskyapp.com/hc/en-us/articles/208047697-JSON-sample-files)
- Real dataset: County Demographics [download](https://corgis-edu.github.io/corgis/json/county_demographics/)


```python
import json
from pprint import pprint

with open("county_demographics.json") as file:
    data = json.load(file)

for item in data:
    if item["County"] == "Harrisonburg city":
        pprint(item)
```

## Quiz 5
- 1st sheet: written potion
- 2nd sheet: coding potion
- 3rd sheet: reference sheet
Turn off monitor during quiz
