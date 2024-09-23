## Announcement
1. Assignments:
   - Complete [HW 5](https://w3.cs.jmu.edu/cs149/f24/hw/hw5/) by 09/25(Wednesday, 11:00pm)
   - Complete the HW5 reflection quiz in canvas by end of today. 
2. Quiz 2 this Thursday
      - Chapters 3 and 4
      - Please review the [Practice quiz 2](https://w3.cs.jmu.edu/cs149/f24/quiz/practice2/)
      - ask for help: office hours, TA hours
3. My available time before the quiz 2:
    - Wednesday: 10:20-11:20 & 12:30-2:30 & 4 - 5pm
    - Thursday: 11:00 - 12:40pm

## Today's class
1. (10 mins) Review Python List and Tuple
1. (40 mins) POGIL Activity: Container
2. (10 mins) HW5 hints
3. (25 mins) [Lab: Function practice](https://canvas.jmu.edu/courses/2035420/assignments/19169987?module_item_id=40887017)

## POGIL Activity: Container
### Instruction:
1. We will skip the **Model 1 Indexes and Values** during the class, you have to complete it after class
2. Work as groups to complete **Model 2 School Acronyms** and **Model 3 Keys and Values**
3. After the class, scan the POGIL worksheet into a single PDF, submit the PDF to canvas. 

### Code for model 2
Python Code:
```python
va_schools = {"JMU", "GMU", "VCU", "VT", "ODU", "WM", "UVA"}
two_letter = {"MU", "VT", "ND", "WM", "BC"}
```

### Hints for HW5
#### HW5.1
Every variable references exactly one object
- In [Python Tutor](https://pythontutor.com/visualize.html#mode=edit), a **reference** is shown as an arrow
- See [complex example](https://pythontutor.com/render.html#mode=display) with many types of objects
- `is` keyword compares object id's(variable's reference)
- Example:

```python
a = "123"
b = "12"
b = b + "3"
if a == b: # compare values of variables
    print("a and b are with same value")
else:
    print("a and b are with different values")

if a is b: # compare references of variables
    print("a and b references the same object")
else:
    print("a and b references the different objects")
```
The output is

```
a and b are with same value
a and b references the different objects
```
#### HW5.2
The easiest way to sort three numbers in ascending order is by using a few simple comparisons. Here's a clear approach:

- Start by comparing the first two numbers: If the first number is larger than the second, swap them.
- Next, compare the second and third numbers: If the second number is larger than the third, swap them.
- Finally, compare the first and second numbers again: If the first is still larger than the second, swap them once more.

After these steps, the three numbers will be sorted in ascending order.
### Lab
[Lab: Function practice](https://canvas.jmu.edu/courses/2035420/assignments/19169987?module_item_id=40887017)
