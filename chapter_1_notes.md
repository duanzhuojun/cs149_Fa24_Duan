## Announcement
1. Assignments: Complete HW 1 by 08/28(Wednesday, 11:00pm)
2. [Video](https://www.youtube.com/watch?v=rtnzmbBqVfI) to Explain Gradescope feedback.  From Dr. Nathan Sprague
3. Thursday’ class: In King 248 lab
4. Today’s class
   1. Short lectures about chapter 1 
   2. In-class practice

## Python Style Guide [10 min]

- PEP = Python Enhancement Proposal
   - PEP 8 – Style Guide for Python Code(Prettier version: https://pep8.org/)
- PEP 257 – Docstring Conventions
- Check your code before submitting to Gradescope!
   - Installing Thonny, flake8
   - Docstring Requirements

## Mini lectures/Demos
Keywords: `print`, `input`, `end = `, `sep = `, 'escape', 'variable', 'String'
### In Python, the print() function is used to output data to the console. There are several ways to use print() depending on what you want to achieve.
1. Basic way
   ```python
   print("Hello, World!")   #output is Hello, World!
   
   name = "cs149"
   print("This is", name)   #output is This is cs149
   ```

2. Keeping output on the same line by 'end'
   ```python
   print("Hello", end=", ")
   print("World!")

   # output is Hello, World!
   ```
3. Specifying the separator between multiple arguments by 'sep'
    ```python
   print("Hello", "World", "!", sep="-")
   # output is Hello-World-!
   ```
4. Escape characters in Python are used to represent certain special characters within a string. They are introduced with a backslash (`\`).
   Here’s a list of common escape characters in Python and their meanings:
   1. Newline (`\n`)
      ```python
      print("Hello\nWorld!")
      ```
      Output is
      ```python
      Hello
      World!
      ```
   2. Tab (`\t`): Inserts a horizontal tab (equivalent to pressing the Tab key).
      ```python
      print("Hello\tWorld!")
      ```
      Output is
      ```python
      Hello   World!
      ```
   3. Backslash (`\\`): Inserts a literal backslash in the string.
      ```python
      print("This is a backslash: \\")
      ```
       Output is
      ```python
      This is a backslash: \
      ```
   4. [More about escape sequences](https://learn.zybooks.com/zybook/JMUCS149Fall2024/chapter/1/section/7)
   ### The `input()` function in Python allows you to take user input from the console. The function reads a line from the input, converts it into a string, and returns it.
   1. Simple Input
   ```python
   name = input("Enter your name: ")
   print("Hello,", name)
   ```
   This code will display the message "Enter your name: " and wait for the user to type something. Once the user presses   
    Enter, it captures the input as a string and stores it in the variable name, then prints a greeting.

   2. Converting Input. By default, `input()` returns the entered data as a string. To use the input as a different data type, you need to convert it.
   ```python
   a = int(input("Enter first Integer: "))
   b = int(input("Enter second Integer: "))

   print("a + b =", a + b)
   ```
   The output will be
   ```
   Enter first Integer: 10
   Enter second Integer: 12
   a + b = 22
   ```
 ### variables 
 In Python, variables can store different types of data, including strings, integers, and floats. 
 1. String Variables: A sequence of characters enclosed in quotes
   ```python
   name = "cs149" # double quotaion
   greeting = 'Welcome to' # single quotation

   full_greeting = greeting + ", " + name + "!" #Concatenation
   repeat = "Ha" * 3                            #Repetition
   print(full_greeting)
   print(repeat)
   ```
   The output is
   ```
   Welcome to, cs149!
   HaHaHa
   ```
2. Integer variables are whole numbers without decimals and float variables are numbers with decimals.
   ```python
   num1 = 25 #integer 
   num2 = 2024  #integer
   price = 1.99 # float

   bill = price * 2
   s = num1 + num2
   ```

