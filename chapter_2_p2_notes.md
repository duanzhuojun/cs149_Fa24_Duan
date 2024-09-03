## Announcement
1. Assignments:
   - Read [chapter 2](https://canvas.jmu.edu/courses/2035420/assignments/18966141?module_item_id=40563343)
   - Complete [HW 2](https://w3.cs.jmu.edu/cs149/f24/hw/hw2/) by 09/04(Wednesday, 11:00pm)
   - In-class quiz 1 will be next Thursday(09/12)
      - The quiz 1 will cover chapter 1 and chpater 2
      - we will practice this sample quiz 1 this Thursday(09/05) - Do not miss the class
2. Today’s class
   1. Error types 
   1. Arithmetic Expressions lecture
   2. Group activity: Practice Problems
   3. If time, HW2 QA

## Error types in Python
1. Syntax
   - Errors that Python finds before executing the code
   - Incorrect syntax and indentation
2. Runtime
   - Errors that occur in a running program
3. Logic
   - A syntactically correct program without runtime errors
   - BUT it doesn’t do what it was supposed to do
     
```python
# Syntax error example: missed the "" or '' for a string
v = input(Enter an int value:)
print(v)

# Logic Error example: should have used 3 to divide the sum of h1, h2 , and h3.
# find the average size of houses
h1 = 1200
h2 = 2600
h3 = 1300
avg = (h1 + h2 + h3) / 2

# Runtime error example: arithmetic opertor - should be applied to two numberic values
# Find the difference between two values
print("The difference is ", "1.99" - 1.00)
```

## Arithmetic Expressions 
- Arithmetic: `+`, `-`, `*`, `**`, `/`, `//`, `%`
- Strings: `+` (concatenation), `*` (repetition)

### `/`, `//`, and `%`
1. **`/` (Division Operator)**: This operator performs **true division**, which means it divides the left operand by the right operand and returns the result as a float, even if both operands are integers.
Example:
     ```python
     result = 7 / 2
     print(result)  # Output: 3.5
     ```

2. **`//` (Floor Division Operator)**: This operator performs **floor division**, which means it divides the left operand by the right operand and returns the largest integer less than or equal to the result (i.e., it floors the result).
Example:
     ```python
     result = 7 // 2
     print(result)  # Output: 3
     ```
Note that if one or both operands are floats, the result will be a float (with the decimal part truncated), but if both operands are integers, the result will be an integer.

3. **`%` (Modulus Operator)**: This operator returns the **remainder** of the division of the left operand by the right operand.
Example:
     ```python
     result = 7 % 2
     print(result)  # Output: 1
     ```
The result is the remainder when the left operand is divided by the right operand.

### Examples:

```python
# True Division
print(7 / 3)    # Output: 2.3333333333333335

# Floor Division
print(7 // 3)   # Output: 2

# Modulus
print(7 % 3)    # Output: 1
```


## Group activity: Practice Problems

### How to complete: 
1. Solve the first problem as a team
2. Present solution(s) to the class
3. Solve the second problem individually
4. Note that you don't need to submit anything for this activity

### 1: Average Speed Calculator
Write a program named `bike_speed.py` that asks the user for the length of a bike race in miles and their finishing time for the race in hours, minutes, and seconds. The program then outputs their average speed in both miles per hour and kilometers per hour. When you output the speed you should show exactly 2 digits past the decimal place. 1 mile = 1.60934 kilometers.

**Here is an example run of the program:**
```
How many miles did you race? 18.66
How much time did that take you in hours, minutes, and seconds?
  Hours: 0
  Minutes: 43
  Seconds: 49

Your speed was 25.55 mph, which is 41.12 kph.
```
**Hint 1:** Figure out how to solve the problem by hand before you try to code anything. You can't program what you can't solve with a pen and paper.

**Hint 2:** You'll want to get your time into one unit. Dealing with 3 separate units is not good for computation. At the end of the day, we need to calculate distance / time in hours to solve the problem, so what is the total time in hours? Notice that 0 hours, 43 minutes, and 49 seconds is ~0.7303 hours. How do you calculate this total? With $$0 + 43/60 + 49/3600$$. How can you do this for other numbers of hours, minutes, and seconds?

### 2: Miles, Furlongs, and Feet
Write a program called `feet_convert.py` that inputs a total number of feet and divide that number into miles, furlongs, and feet. (A furlong is some old English measure nobody uses anymore, but let's do it anyway!) 1 mile is 5280 feet, and 1 furlong is 660 feet.

**Here is an example run of the program:**
```
Enter a total number of feet: 12345

12345 total feet is 2 mile(s), 2 furlong(s), and 465 feet.
```
**Hint 1:** Figure out how to solve the problem yourself by hand on paper. You can't code something you don't know how to solve.

**Hint 2:** You will need to use floor division and remainder (`//` and `%`).

**Hint 3:** Create a variable for the remaining feet. In the example above, the remaining feet is initially 12345. Once you figure out there are two full miles in 12345 feet (2 full miles is 10560 feet), then the remaining feet is 1785. How many full furlongs are in 1785 feet? Well, 2 again, since $$660 * 2 = 1320$$
. And finally after we remove those 1320 from 1785, the remaining feet is 465.
