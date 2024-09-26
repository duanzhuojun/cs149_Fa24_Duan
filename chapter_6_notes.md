## Announcement
1. Assignments:
- Complete the chapter 6 reading in zybook by next Monday 11:59pm
- Complete [HW 6](https://w3.cs.jmu.edu/cs149/f24/hw/hw6/) by 10/02(Wednesday, 11:00pm)
- Complete the HW5 reflection quiz in canvas by end of today. 
2. Event: 
- Social with Microsoft employees: Thursday, Sep 26th, 6-7pm, King348
3. Submit HW 6 – ideally:
- 1 and 2 before Friday
- 3 and 4 before Monday


## Today's class
1. (20 mins) POGIL Activity: `for` loop
2. (15 mins) Chapter 6 preview: `for` loop used in different containers
4. (10 mins) A practice for quiz 2
5. (30 mins) Quiz 2

## POGIL Activity: `for` loop
- Please complete the POGIL worksheet
- You don't need to submit anything for this activity today.
- Programs used in the activity:

```python
print("hello")
for x in [2, 7, 1]:
    print("the number is", x)
print("goodbye")
```
## Chapter 6 preview: `for` loop used in different containers
### Example 1: for each element of a list

```python
words = ["Pause", "brink", "fox", "Cup", "match", "sound",
         "president", "Restless", "despise", "Rack"]
for word in words:
    if len(word) == 5:
        print(word, "is with length of 5")
```

### Example 2: for each element of a set

```python
tasks = {"laundry", "vacuuming", "dishes", "raking", "shopping"}
for t in tasks:
    t = t + "!"
    print(t)
```

### Example 3: for each character in a string

```python
message = "cs149-cs159-cs240"
for c in message:
    if c not in ['c', 's', '-']:
        print(c, end="")
print()
```

### Example 4: for each key in a dictionary

```python
week_days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

for key in week_days:
    value = week_days[key]
    print(f"{key} is {value}.")
```

## A practice for quiz 2
Write a function named `find_larger` which complies with the docstring below. Assume the two values passed to the function are different.

```python
"""
Compare two float values and return the larger one.

Examples:
    find_larger(11.1, 12.0) returns 12.0
    find_larger(0.1, 0.2) returns 0.2

Args:
    v1 (float): The first value.
    v2 (float): The second value.

Returns:
    float: The larger of the two values.
"""
# Write your code here
```


