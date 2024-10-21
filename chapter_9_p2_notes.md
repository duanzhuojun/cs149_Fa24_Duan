## Announcement
1. [PA 1 Flexdoko](https://w3.cs.jmu.edu/cs149/f24/pa/pa1/)
- Reading quiz in canvas - Done
- Part A due Friday 10/25 (30 pts)
- Part B due Wednesday 10/30 (70 pts)
2. Actual quiz 4 Next Thursday 10/31, in King248
- Covers chapters 7 and 8: `while loop` and `modules`
- New way: all written format
- Make sure you review the practice quiz 4 right before the actual quiz


## Today's class
1. (25 mins)In-class practices: Strings and Lists
   - Python string methods review, practices
   - Python list methods review, practices
   - Tips to use string/list methods in Python
2. (20 mins)Review `while` loop and modules
3. (30 mins)Practice quiz 4


## In-class practices in Python `String` methods

### Commonly used Python string methods.

| Methods	      | Returns ?	|
| -----------     | --------------- |
|`find(x)`   | Returns the index of the first occurrence of the substring `x` or -1 if not found. |
|`count(x)`  | Returns the number of times `x` occurs in the string. |
|`isdigit()` | Returns True if **all** characters are the numbers 0-9.|
|`islower()` | Returns True if **all** cased characters are lowercase letters.|
|`isupper()` | Returns True if **all** cased characters are uppercase letters.|
|`startswith(x)` | Returns True if the string starts with `x`.|
|`endswith(x)` | Returns True if the string ends with `x`.|

Find more String methods: [A summary of all string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

### Tips to use String methods in Python
1. Understand the Method’s Return Type
- String methods like `replace()`, `upper()`, and `lower()` return new strings and do not modify the original string (strings in Python are immutable).
- `find(x)` returns index or -1
2. Check Case Sensitivity Before Using Case Methods
- use `islower()` or `isupper()` to check if the case conversion is necessary
- use `lower()` or `upper()` to standardize the case and avoid mismatches due to case differences

### Practice 1
Define a Python function named `end_second(first, second)` that returns `True` if the second string appears at the end of the first string, ignoring case differences.

```py
# Example
>>> end_second("csJMU", "jmu")
True
```

### Practice 2
Define a Python function named as `sumDigits(s)` returns the sum of the digits 0-9 that appear in the string `s`, ignoring all other characters. Return 0 if there are no digits in the string.

```py
# Example
>>> sumDigits("aa1bc2d3")
6
>>> sumDigits("jmu")
0
```

## In-class practices in Python `List` methods

### Commonly used Python list methods
#### Adding elements
- `append(x)` VS. `extend([x])`
- `insert(i, x)`
#### Removing elements
`remove(x)` VS. `pop(i)`
#### Advanced
- `index(x)`: Return index of first item in list with value `x`.
  - Python list has no `find(x)` method. The find() method is specific to strings
- `count(x)`: Count the number of times value `x` is in list.

### Python methods that convert strings into lists.
- The `list()` function can be used to convert a string into a list of individual characters.
- The `split()` method splits a string into a list of substrings based on a specified delimiter (default is whitespace).

### Practice 3: Codingbat [List-2](https://codingbat.com/python/List-2)

## Review `while` loop and modules

### TBA
