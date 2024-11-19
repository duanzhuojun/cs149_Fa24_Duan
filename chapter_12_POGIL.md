## Announcements
1. [Project 3](https://w3.cs.jmu.edu/cs149/f24/pa/pa3/) (due Dec 03)
   - Part A due Tuesday, 11/19
   - Part B due Friday, 11/22
   - Part C due Wednesday, 12/04
   - Main Idea
     - Read last.fm data from json files
     - Build playlists and find new songs
     - PA 3 specification and [sample data](https://w3.cs.jmu.edu/cs149/f24/pa/pa3/stubs/sample_data.py)
2. No additional office hours this Friday
   1. I will be in a conference this Friday
   2. Please complete the Part B by Thursday(11/21) if possible
3. Thursday's class
   1. Practice Quiz 6
   2. Help with PA3
4. [CS/IT game night event](https://w3.cs.jmu.edu/cs149/f24/csit/gamenight/): Today at 5:30pm in King Hall 259

## Today's class
1. (45 mins) POGIL: Recursive Functions
2. (10 mins) Command-line arguments
   1. Zybook: chapter 10.5
3. (20 mins) PA3 QA

## POGIL: Recursive Functions
- POGIL Recursive Functions [worksheet](pogil_sheet\Act12-Recursive_Student.pdf).
- After the class, scan the worksheet with your solution, submit to canvas
- The solution will be available this weekend in canvas
- Demo: [Recursion Tree Visualizer](https://recursion.vercel.app/)

### Code snippet used in model 1

```python
def factorial(n):
    # base case
    if n == 0:
        return 1
    # general case
    product = 1
    for i in range(n, 0, -1):
        product *= i
    return product
```

### Code snippet used in model 2

```python
def fibonacci(n):
    # base case
    if n == 1 or n == 2:
        return 1
    # general case
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    for i in range(1, 6):
        print(fibonacci(i))
```
## Command-line arguments
Command-line arguments are values entered by a user when running a program from a command line.
###
1. To execute commands, opening PowerShell/commandline shell on Windows, or Opening Terminal on Mac.
2. Ensure the script file (e.g., `command_line.py`) is saved in a directory you can access. Or change to the directory containing the script:
```
cd /path/to/your/command_line.py
```
3. Run the Script
```
python command_line.py
```
4. Pass Arguments when running the script:
```
python3 command_line.py arg1 arg2
```
### Command-line arguments example

```py
import sys
import os

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python command_line.py <input_file>")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print(f'Input file {sys.argv[1]} does not exist.')
        sys.exit(1)

    print("argv0 is", sys.argv[0], "argv1 is", sys.argv[1])

```
