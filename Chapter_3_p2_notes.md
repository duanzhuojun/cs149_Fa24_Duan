## Announcement
1. Assignments:
   - Complete [HW 3](https://w3.cs.jmu.edu/cs149/f24/hw/hw2/) by 09/11(Wednesday, 11:00pm)
   - In-class quiz 1 will be this Thursday(09/12) - King 248 Lab
      - The quiz 1 will cover chapter 1 and chpater 2
      - Review questions from [Practice Quiz 1](https://w3.cs.jmu.edu/cs149/f24/quiz/practice1/)
  - Events this week:
      - [First Year Kickoff 9/11](https://w3.cs.jmu.edu/cs149/f24/csit/kickoff/): Wed, Sep 11th at 5:15pm in EnGeo 2301
      - [Social meeting of WIT club](WIT_social_meeting.png): Thursday, Sep 12th at 6:00pm in King 348
2. Today’s class
   1. Mini-lecture: Relational Operators and logial operators
   2. Group activity: Tracing Practice
   3. Coding practice

## Boolean expressions

### Relational Operators:
1. ```==``` (Equal)
2. ```!=```(Not equal)
3. ```> ```(Greater than)
4. ```<``` (Less than)
5. ```>=``` (Greater than or equal to)
6. ```<= ```(Less than or equal to)

### Example:
```python
a = 10
b = 5

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False
```
### Logial Operators:
Logical operators are used to combine conditional statements and control the flow of a program based on multiple conditions. The three primary logical operators in Python are: 'and', 'or', and 'not'.

1. `and`: Returns `True` if **both** statements are `True`.
```python
x = 5
y = 10
if x > 0 and y > 5:
    print("Both conditions are True")
# Output: Both conditions are True
```
2. `or`: Returns `Tru`e if **at least one** of the statements is `True`.
```python
x = 5
y = 2
if x > 0 or y > 5:
    print("At least one condition is True")
# Output: At least one condition is True
```
3. `not`: Reverses the result, returning `True` if the statement is `False`.
```python
x = 5
if not x == 10:
    print("x is not equal to 10")
# Output: x is not equal to 10
```
#### Precedence of Logical Operators:
`not` has the highest precedence, followed by `and`, and then `o`r. Use parentheses () to explicitly control precedence when combining these operators.

## Group activity: Tracing Practice
For each example: 
1. Predict the output as a team (by hand, on paper)
2. Use Thonny to see the actual output.
### Example 1:
```python 
hat = "fedora"

if hat == "fedora":
    print("A")
else:
    print("B")

print("C")
```
### Example 2:
```python 
x = 10

if x < 100:
    print("A")
elif x < 50:
    print("B")
else:
    print("C")

print("D")
```
### Example 3:
```python 
x = 10

if x < 100:
    print("A")
if x < 50:
    print("B")

print("C")
```
### Example 4:
```python 
x = 10
hat = "fez"

if x > 100 or hat == "fez":
    print("A")
    if x < 50:
        print("B")
    else:
        print("C")
else:
    print("D")
    if hat == "fedora":
        print("E")
print("F")
```
### Example 5:
```python 
x = 1.0
y = 0.0
b1 = x > 0 and y > 0
b2 = not x <= 0 or y <= 0
b3 = not (x <= 0 or y <= 0)
print(b1, b2, b3)
```
## Coding practice 1
Alice enjoys playing outdoors during most of the day. Specifically, she plays if the temperature is between 60 and 90 degrees (inclusive). However, if it's summer, she plays even when the temperature is up to 100 degrees.
Write a program named `play.py` that begins with the following lines:
```python
# You can change the values of temperature and is_summer
temperature = 90
is_summer = False
# Add your code here
```
The program should print "play!" if Alice plays and "Not play!" otherwise.

This question is rewritten from the original version in [condingbat](https://codingbat.com/python)
### Test your code using following test cases:
- If `temperature = 70` and `is_summer = False`, the program should print "play!".
- If `temperature = 95` and `is_summer = False`, the program should print "Not play!".
- If `temperature = 95` and `is_summer = True`, the program should print "play!".
- If `temperature = 60` and `is_summer = False`, the program should print "play!".
- If `temperature = 50` and `is_summer = False`, the program should print "Not play!".


## Coding practice 2
The number 6 is a truly great number. Given two int values, `a` and `b`, print "Love6!" if either one is 6, or if their sum or difference is 6. Otherwise, print "Not Love6!". Note: the function **abs(num)** computes the absolute value of a number.

Write a program named `love6.py` that begins with the following lines:
```python
# You can change the values of a and b
a = 10
b = 4
# Add your code here
```
### Test your code using following test cases:
- If `a = 6` and `b = 4`, the program should print "Love6!".
- If `a = 6` and `b = 6`, the program should print "Love6!".
- If `a = 2` and `b = 8`, the program should print "Love6!".
- If `a = 3` and `b = 3`, the program should print "Love6!".
- If `a = 1` and `b = 4`, the program should print "Not Love6!".
- If `a = 2` and `b = 5`, the program should print "Not Love6!".
- If `a = 4` and `b = 8`, the program should print "Not Love6!".


