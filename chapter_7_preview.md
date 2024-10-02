## Announcement
1. Assignments:
- Complete the chapter 7 reading in zybook by next Monday 11:59pm
- Complete [HW 7](https://w3.cs.jmu.edu/cs149/f24/hw/hw7/) by 10/09(Wednesday, 11:00pm)
- Complete the HW6 reflection quiz in canvas by end of this Thursday. 

2. Quiz 3 next Thursday(10/10)
- cover chapters 5 and 6: function, for loop, range, and so on
- How to Prepare for Quiz 3:
    - Review all POGIL solutions related to the quiz on Canvas.
    - Go over Homework 5 and 6 thoroughly.
    - Retake the practice Quiz 3 within 24 hours before the actual quiz.
3. Optional Lab: [Haiku](https://canvas.jmu.edu/courses/2035420/assignments/19197962).
    - Practice conditionals, functions, using a helper function, loops, lists and strings
    - This lab would not go into your grades. 

## Today's class
-(20 minutes) POGIL activity: `while` loop introduction
-(15 minutes) Demo: 
    - `while` loop
    - `random` module
-(30 minutes) Practice quiz 3

## POGIL activity: `while` loop introduction
- Complete the `while` loop introduction worksheet in 10 minutes
    - [`while` loop introduction worksheet](pogil_sheet\While_Loops_part1.pdf)
- Discuss using the correct solution with your deskmates:

## Demo: `while` loop

### Task 1: Ask the user to enter 5 integer values using the keyboard, then calculate and print the average of those values.

```python
total = 0

# Use a while loop to prompt the user for 10 integers
i = 0
while i < 5:
    num = int(input(f"Enter integer: "))
    total = total + num
    i += 1

# Calculate the average of the entered numbers
average = total / 5

# Print the average
print(f"The average of the entered numbers is: {average}")
```

### Task 2: Prompt the user to enter integer values using the keyboard until they enter 0, then calculate and print the average of the entered values (excluding the 0).

```python
total = 0
count = 0

# Use a while loop to prompt the user for integers until 0
num = int(input(f"Enter integer: "))
while num != 0:
    total = total + num
    num = int(input(f"Enter integer: "))
    count = count + 1

# Calculate the average of the entered numbers
average = total / count

# Print the average
print(f"The average of the entered numbers is: {average}")
```

### `random` module
The random module, in the Python Standard Library, provides methods that return random values. 

```python
# imports random module
import random

# The random() method returns a random floating-point value each time the function is called, in the range 0 (inclusive) to 1 (exclusive).
# Generates a random floating point number 
print(random.random())
print(random.random())

# randint(min, max)
# Generate a random int between min and max inclusive.
x = random.randint(1, 10)
print(x)

# Generate 20 random int from 1 to 6, and put them in a list
rand = []
i = 0
while i < 20:
    y = random.randint(1,6)
    rand.append(y)
    i = i + 1

print(rand)
```



