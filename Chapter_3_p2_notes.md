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
   1. Mini-lecture: boolean expressions + branches
   2. Group activity: Tracing Practice
   3. Coding practice:

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



