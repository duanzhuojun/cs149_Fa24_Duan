## Announcement
1. Assignments:
   - Reading chapter 5 in zybook - Next Monday 11:59pm
   - Complete [HW 5](https://w3.cs.jmu.edu/cs149/f24/hw/hw5/) by 09/25(Wednesday, 11:00pm)
   - Complete the HW4 reflection quiz in canvas by end of today. 
2. Quiz 2 next Thursday
      - Chapters 3 and 4
3. Event: [What is CS Research?](https://w3.cs.jmu.edu/cs149/f24/csit/research/) - Friday 9/20 from 11:25–12:25 in King 259

## Today's class
1. (5 mins) Demo: [in1to10](https://codingbat.com/prob/p158497)
2. (10 mins) Scope of variables and functions
3. (20 mins) Introduction to container
4. (30 mins) Practice quiz 2

## Scope of variables and functions
A variable or function object is only visible to part of a program, known as the object's scope.

### Local Variables
- A local variable is defined inside a function and only accessible within that function.
- **Scope**: It is limited to the block of code (usually a function) where it is defined. Once the function execution is complete, the local variable is destroyed.
- **Used** when you want the variable to be restricted to a specific function to avoid interference with the global scope.
```python
def local():
    name = "cs149"  # Local variable
    print(name)


local()  # Output: cs149

print(name)  # Error: NameError because name is not accessible outside the function
```

### Global Variables
- A global variable is one that is defined at the top level of a program or module, outside of any function.
- **Scope**: It is accessible throughout the program, including inside functions (unless overridden by a local variable).
- Typically **used** when you need to access the same data across multiple functions.

```python
name = "cs159"  # Global variable

def my_global():
    print(name)  # Use global variable

my_global()  # Output: cs159
```

### To modify a global variable inside a function, you need to use the `global` keyword.
```python
name = "cs240"  # Global variable

def change_global():
    global name
    name = "cs261"  # Modifying the global variable
    print(name)  # Output: cs261

change_global()
print(name)  # Output: cs261 (global variable is modified)
```

## Chapter 5 preview: Object, variable

1. Everything in Python is an **object**, including numbers, strings, functions, and classes. Each object in Python has a value, a type, and an identity
    - `type()` and `id()` functions

2. Variables are names or labels that reference objects. A variable is like a tag that points to an object stored in memory. The variable itself doesn't store the actual object, just a reference to it.

```python
x = 5 # x is a variable that points to the object 5

a = 5
b = a
# Both a and b point to the same object (5), but they are different variables.
```

3. In summary, objects are the actual data, while variables are references or labels that point to these objects.

4. In [Python Tutor](https://pythontutor.com/visualize.html#mode=edit), a reference is shown as an arrow

5. **Container**: A container is an object that contains (references) other objects
    - list: `[1, 2, 3]` in brackets
    - tuple: `(1, 2, 3)` in parentheses
    - set: `{1, 2, 3}` in braces
    - dict: `{"one": 1, "two": 2, "three": 3}` braces + colons
