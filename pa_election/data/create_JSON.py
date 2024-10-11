"""Create .JSON for electoral college

reference: https://www.w3schools.com/python/python_json.asp
Author: CS149 instructors
Version: 10/11/2024
"""
import json

# Create a Python object(dict) from the cvs

file = open("Electoral_College.csv", "r")
json_dict = dict()

for line in file.readlines()[1:]:
    items = line.split(",")
    state = items[1]
    count = int(items[2])
    json_dict[state] = count
    
# convert into JSON:
y = json.dumps(json_dict)

# Electoral_College.json
with open("Electoral_College.json", "w") as outfile:
    outfile.write(y)
        
