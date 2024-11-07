## Announcements
1. [PA 2 World of Elections](https://w3.cs.jmu.edu/cs149/f24/pa/pa2/)
- Part A - Reading quiz in canvas - End of today.
- Part B due Friday 11/08 (30 pts)
- Part C due Friday 11/15 (70 pts)
2. Practice quiz 4 this Thursday 11/17, in King248
- Covers chapters 9 and 10: Sequence and File I/O
3. Grades of quiz 4 will be posted this Wednesday 11/05

## Today's class
1. (40 mins)POGIL: File IO
2. (20 mins)Demos
    - The `close()` method is crucial for saving changes and freeing resources.
    - Use the `with` statement for file handling
    - `read()` Vs. `readline()` and `readlines()`
    - To check if a file exists, use `os.path.exists()`
3. (15 mins)PA2 part B hints

## POGIL: File IO
- POGIL file IO [worksheet](pogil_sheet\Act10-FileIO_Student.pdf).
- After the class, scan the worksheet with your solution, submit to canvas
- The solution will be available this weekend in canvas

### Code snippets in model 1

```py
outfile = open("out.txt", "w")
outfile.write("Example ")
outfile.write("output ")
outfile.write("text file\n")
outfile.write("xyz Coordinates\n")
outfile.write("MODEL\n")
outfile.write(f"ATOM {1:3d}")
seq = f"n {0:5.1f}{1:5.1f}{2:5.1f}"
outfile.write(seq)
outfile.write("\n")
outfile.close()
```

### Code snippets in model 2

```py
afile.write("new line\n")
afile = open("out.txt", "a")
afile.write("new line\n")
afile.write(2.0)
afile.write("2.0")
afile.close()
afile.write("new line\n")
```
#### After running the above code, the file contents should be:

```
Example output text file
xyz Coordinates
MODEL
ATOM   1n   0.0  1.0  2.0
new line
2.0
```

### Code snippets in model 3

```py
infile = open("out.txt", "r")
infile.readline()
infile.readline()
infile.readlines()
infile.readline()
infile.close()
```

```py
infile = open("out.txt", "r")
for line in infile:
    print(line)
infile.close()
```

```py
infile = open("out.txt", "r")
for i in range(3):
    infile.readline()
line = infile.readline()
infile.close()
```

```py
line
line[0]
line[0:5]
words = line.split()
words
words[0]
```

The following file can be used for the last question:
- [names.txt](pogil_sheet\names.txt)

## Demo 1: The close() method closes an open file.
You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

### **Example:**
Write a program that creates a file named `sample.txt` and writes 5 lines like this:

```
0, sample
1, sample
```

Solution:

```Python
file = open("sample.txt", "w")
for i in range(20):
    file.write(f"{i}, sample\n")
# If the close() method is not called, the written content might not appear as expected.
file.close()
```

If a file is opened to perform a task on it(either read or write), then it must be closed once the task is done. This is to make sure the amount of open files on an operating system do not exceed the limit it sets.

## Demo 2: use `with` statement
Using the with statement ensures that the file is properly closed, so the content will be written as expected:


```python
# This way, you don't need to explicitly call close(), as the with statement automatically handles it when the block is exited.
with open("sample1.txt", "w") as infile:
    for i in range(20):
        infile.write(f"{i}, sample\n")
```
## Demo 3: `read()` method
In Python, the file object provides three primary methods for reading from a file:
- `read()`: Reads the entire content
- `readline()`: Reads a single line from the file. If a size argument is provided, it reads up to that number of bytes.
- `readlines()`: Reads all lines from the file and returns them as a list of strings.

```python
with open("sample.txt", "r") as infile:
    s = infile.read()
    print(s)
```


## Demo 4: `os` module
- In Python, the `open()` function is used to open files, not directly for interacting with the operating system.
- However, you can use the `os` module to interact with the operating system and perform file-related operations.

### `os` module provides functions for interacting with the operating system, including file system operations.
- `os.path.exists(path)`: Checks if a file or directory exists at the given path.
- `os.listdir(path)`: Lists the files and directories in a directory.
- ...

**Examples:**

```python
import os
#
if not os.path.exists("nofile.txt"):
    print("file does not exist")
else:
    with open("nofile.txt", 'r') as outfile:
        outfile.write("cs149\n")
```

## PA2: https://w3.cs.jmu.edu/cs149/f24/pa/pa2/
