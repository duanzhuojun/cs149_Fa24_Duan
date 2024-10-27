## Outline: Review for quiz 4 and PA1 QA


## Announcements
1. [PA 1 Flexdoko](https://w3.cs.jmu.edu/cs149/f24/pa/pa1/)
- Part B due Friday 11/01 (70 pts) - Extended
  - PA2 will be posted next Wednesday 10/30
  - Complete 1-2 functions this Weekeend
2. Actual quiz 4 this Thursday 10/31, in King248
- Covers chapters 7 and 8: `while loop` and `modules`
- New way: all written format
- Make sure you review the practice quiz 4 and solution right before the actual quiz


## Today's class
1. (20 mins) Practice quiz 4 review
2. (25 mins) In-class practices: Strings, Lists, and Loops
3. (20 mins) PA1 part B QA

## Practice quiz 4
[Practice Quiz 4 (Ch 7–8)](https://w3.cs.jmu.edu/cs149/f24/quiz/practice4/)

## More practices:

### Trace the code below. What will it print once the code is done executing?

```python
num = 5
while num <= 15:
    print(num)
    num += 2
```

### Trace the code below. What will it print once the code is done executing?

```python
num = 5
while num <= 16:
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    num += 1
```

### Trace the code below. What will it print in each iteration? Leave the cell empty if nothing will be printed.

```python
num = 12
count = 0

while num <= 20:
    num = num + 1
    if num % 3 == 0:
        count = count + 1
        continue
    elif num % 8 == 0:
        count = count + 1
    elif num == 17:
        break
    else:
        print("not multiple")
```

### Write a function `get_largest()`, which has a while loop that continuously prompts the user for positive int values as input until they enter 'quit'. Print the largest value.
### write the solution on a hard paper.

```python
# Assume all values entered by users are positive
# Example
>>> get_largest()
input: 1
input: 2
input: 1
input: 4
input: 1
input: quit
4

```
