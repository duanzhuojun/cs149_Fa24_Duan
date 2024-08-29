## Announcement
1. Assignments:
   - Complete the [HW1 reflection quiz](https://canvas.jmu.edu/courses/2035420/quizzes/4476512?module_item_id=40470309) by end of today.
   - Read [chapter 2](https://canvas.jmu.edu/courses/2035420/assignments/18966141?module_item_id=40563343)
   - Complete [HW 2](https://w3.cs.jmu.edu/cs149/f24/hw/hw2/) by 09/04(Wednesday, 11:00pm)
2. Prepare for the next week
4. Thursday’ class: In King 248 lab
5. Today’s class
   1. HW1 debrief
   2. Python String formatting(f-String)
   3. POGIL - Arithmetic Expressions
         - Scan the solution of POGIL and submit it to gradescope
         - [How to scan](https://wiki.cs.jmu.edu/student/canvas/start)


## Python String formatting(f-String)
A Python f-string is a way to format strings in Python, f-strings are prefixed with an f or F before the opening quotation mark and allow you to embed expressions inside curly braces {} within the string. These expressions are evaluated at runtime, making f-strings a powerful tool for dynamic string generation.
{} is called placeholder expressions or replacement field
### Example 1
```python
name = "Tom"
age = 18

# Using an f-string
message = f"My name is {name} and I am {age} years old."
print(message)
```
The output is
```
My name is Tom and I am 18 years old.
```
### Example 2
```python
v1 = 10
v2 = 11

# Pay attention to the use of =
print(f'The results is {v1 + v2}')
print(f'The results is {v1 + v2 = }')
```
The output is
```
The results is 21
The results is v1 + v2 = 21
```
### Example 3
f-strings can also format numbers, specify precision, and even call functions directly inside the string.
```python
price = 1.99
weight = 600.78

cost = price * weight
print(f'The cost is {cost:f}')
print(f'The cost is {cost:.2f}')
print(f'The cost is {cost:,.2f}')
```
The output is
```
The cost is 1195.552200
The cost is 1195.55
The cost is 1,195.55
```


