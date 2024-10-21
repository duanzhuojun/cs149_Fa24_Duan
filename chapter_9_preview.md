## Table of Content: Chapter 9 preview
- [Table of Content: Chapter 9 preview](#table-of-content-chapter-9-preview)
- [Announcements](#announcements)
- [Today's class](#todays-class)
- [POGIL: Advanced Strings](#pogil-advanced-strings)
  - [Code snippets used in Model 1:](#code-snippets-used-in-model-1)
  - [Code snippets used in Model 2:](#code-snippets-used-in-model-2)
- [Lab: List Play](#lab-list-play)

## Announcements
1. [PA 1 Flexdoko](https://w3.cs.jmu.edu/cs149/f24/pa/pa1/)
- Reading quiz in canvas due Tuesday 10/22 - Today (10 pts)
- Part A due Friday 10/25 (30 pts)
- Part B due Wednesday 10/30 (70 pts)
1. Practice quiz 4 this Thursday 10/24, in King248
- Covers chapters 7 and 8: `while loop` and `modules`
- New way: all written format, NO gradescope, NO canvas.
- Do not miss it
1. Reminder
- [Set up Visual Studio Code]((https://w3.cs.jmu.edu/cs149/f24/info/vscode/)) for your own devices
- Ask for help from TA hours or my office hours
1. Withdraw date is Wednesday 10/23
- I posted your Mid-term letter grades in canvas
- Talk to your advisor and me if you have any concern.

## Today's class
1. (35 mins)POGIL: Advanced Strings
2. (30 mins)Lab: List Play
3. (10 mins)PA1 hints and QA

## POGIL: Advanced Strings
1. [POGIL worksheet](pogil_sheet\Act09-ListString_Student.pdf) in PDF
2. After the class, scan it and submit to canvas individually
3. Solution will be posted this weekend.

### Code snippets used in Model 1:

```python
dna = 'CTGACGACTT'
dna[5]
dna[10]
len(dna)
dna[:5]
dna[5:]
dna[5:10]
triplet = dna[2:5]
print(triplet)
dna[-5]
dna[-10]
dna[:-5]
dna[-5:]
triplet = dna[-4:-1]
print(triplet)
```

### Code snippets used in Model 2:

```python
dna = 'CTGACGACTT'
dna.lower()
print(dna)
lowercase = dna.lower()
print(lowercase)
dnalist = list(dna)
print(dnalist)
dnalist.reverse()
print(dnalist)
type(dna)
dna = dna.split('A')
print(dna)
type(dna)
dna.replace('C', 'g')
print(dna[0])
type(dna[0])
dna[0].replace('C', 'g')
print(dna)
```

## Lab: List Play
- Complete the lab and submit your code to gradescope
- Complete it by this Wednesday. But you can still submit your solution to Gradescope by this Sunday.
