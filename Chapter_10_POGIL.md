## Announcements
1. [PA 2 World of Elections](https://w3.cs.jmu.edu/cs149/f24/pa/pa2/)
- Part A - Reading quiz in canvas - Done
- Part B due Friday 11/08 (30 pts)
- Part C due Friday 11/15 (70 pts)
2. Practice quiz 4 this Thursday 11/17, in King248
- Covers chapters 9 and 10: Sequence and File I/O

## Today's class
1. (40 mins)POGIL: File IO
2. (20 mins)Practices related to file IO:
    - `split()` method
    - how to decide file does not exist
3. (15 mins)PA2 part B hints

## POGIL: File IO
- POGIL file IO [worksheet](pogil_sheet\Act10-FileIO_Student.pdf).
- After the class, scan the worksheet with your solution, submit to canvas

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

##
