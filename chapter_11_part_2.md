## Announcements
1. [PA 2 World of Elections](https://w3.cs.jmu.edu/cs149/f24/pa/pa2/)
- Part A - Reading quiz in canvas - Done.
- Part B due Friday 11/08 - Done.
- Part C due Friday 11/15 (60 pts)
1. Quiz 5 this Thursday 11/14, in King248
- Covers chapters 9 and 10: Sequence and File I/O
- Review the solution of Practice quiz 5
  - Solution will be posted after the class today

## Today's class
1. (30 mins) POGIL: Nested Structures
2. (30 mins) Practice quiz discussion
3. (15 mins) PA2 QA

## Chapter 11(Nested data) preview

**POGIL: Nested data**
   - Complete model 2 and model 3
   - [Worksheet](pogil_sheet\Act11-Nested_Student.pdf)
   - No submission today.

Code snippet in Model 1:

```python
grid = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['Y', ' ', ' ', ' ', 'Y', 'Y', ' '],
    ['R', ' ', ' ', 'Y', 'R', 'R', ' '],
    ['R', 'R', 'Y', 'R', 'Y', 'R', ' '],
    ['R', 'Y', 'R', 'Y', 'Y', 'Y', 'R'],
]
```

Code snippet in Model 2:

```python
groceries = ["Apples", "Milk", "Flour", "Chips"]
for item in groceries:
    print("Don't forget the", item)

count = 0
for row in grid:  # outer loop
    print("row =", row)
    for cell in row:  # inner loop
        print("cell =", cell)
        if cell == ' ':
            count += 1
print(count, "spaces remaining")
```

Code snippet in Model 3:

```python
movies = {
    "Casablanca": {
        "year": 1942,
        "genres": ["Drama", "Romance", "War"],
    },
    "Star Wars": {
        "year": 1977,
        "genres": ["Action", "Adventure", "Fantasy"],
    },
    "Groundhog Day": {
        "year": 1993,
        "genres": ["Comedy", "Fantasy", "Romance"],
    },
}
```

## Practice quiz 5
- Practice quiz 5 [worksheet](https://w3.cs.jmu.edu/cs149/f24/quiz/practice5/)
- [Reference sheet](https://w3.cs.jmu.edu/cs149/f24/quiz/reference/)
  - will be available during the actual quiz too


## PA2 part C QA
