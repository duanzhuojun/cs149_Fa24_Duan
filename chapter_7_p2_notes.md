## Announcement
1. Assignments:
- Complete [HW 7](https://w3.cs.jmu.edu/cs149/f24/hw/hw7/) by 10/09(Wednesday, 11:00pm, no later than 8:00am this Thursday)
- Complete the HW7 reflection quiz in canvas by end of this Thursday. 
2. Quiz 3 this Thursday(10/10)
- cover chapters 5 and 6: container, for loop, range, and so on
    - No while and no random
- How to Prepare for Quiz 3:
    - Review the [practice Quiz 3](https://w3.cs.jmu.edu/cs149/f24/quiz/practice3/)
        - Retake the practice Quiz 3 within 24 hours before the actual quiz.
    - Review all POGIL solutions related to the quiz on Canvas.
    - Go over Homework 5 and 6 thoroughly.
3. Optional Lab: [Haiku](https://canvas.jmu.edu/courses/2035420/assignments/19197962).
    - Practice conditionals, functions, using a helper function, loops, lists and strings
    - This lab would not go into your grades. 

## Today's class
- (35 mins)POGIL: `Random Numbers`  and `while vs for`
- (10 mins)Practice quiz 3 coding portion review
    - review container
- (20 mins)In-class practices
- HW7 QA


## POGIL: `Random Numbers`  and `while vs for`
- Work with your group partners to complete Models 2 and 3:[POGIL worksheet](pogil_sheet\WhileRandom.pdf).
- The code used in the POGIL activities is provided below.
- After class, submit your solutions for Models 2 and 3 and submit them to Canvas.
    - If you missed class today, you can download the [POGIL worksheet](pogil_sheet\WhileRandom.pdf), complete it, and submit it to Canvas.
- Solutions will be posted in canvas this weekend.

### Code snippets used in Model 3:
**Program A (while loop)**

```python
import random

print("Guess my number!")
number = random.randint(1, 100)

guess = 0
while guess != number:
    guess = int(input("Guess: "))
    if guess > number:
        print("Too high!")
    elif guess < number:
    print("Too low!")

print("You got it!")
```

**Program B (for loop)**

```python
import random

heads = 0
tails = 0
times = 1000000

for _ in range(times):
    if random.random() < 0.5:
        heads += 1
    else:
        tails += 1

heads = round(heads / times * 100, 2)
tails = round(tails / times * 100, 2)

print(f"Head: {heads}%, Tail: {tails}%")
```

## Practice quiz 3 coding portion
Tips to implement a function in the quiz
- Read the description and identify the function name, parameters, parameter types, and expected output. Determine whether the function uses a print statement or return statement. If the function returns values, specify the return types.
- Use the provided example to connect the input(parameters) and output(`print` or `return`).

### `names_cap` function

```python
# first way: use str.isupper(item[0])
def names_cap(names):
    for item in names:
        if str.isupper(item[0]):
            print(item)

# second way: use item[0].isupper()
def names_cap(names):
    for item in names:
        if item[0].isupper():
            print(item)
```

### `limit_letters` function

```python
def limit_letters(counts, limit):
    s = set() # the only way to create empty set
    for letter in counts:
        if counts[letter] <= limit:
            s.add(letter)
    return s
```
Notes: the two practices below are from Dr. Mayfield. 

## In-class practice 1
Write a function named `find_M(words)` that takes a list of words and returns the words that with first letter as 'M'. Do not change the list you are given. Instead, follow these steps:

1. Create an empty list.
2. Write a for loop that adds one word at a time to the end of the list.
3. Return the resulting list. 

Repeat the exercise using `set` and `dict` as the return type. For `dict`, use the word for the key and the length for the value.

## In-class practice 2
Write a function named `five_star(hotels)` that takes a dictionary of hotel names and ratings. Return a list of hotels that have a rating of 4.5 or higher. 
- Ex: Given `{"Ritz": 5.0, "Marriott": 4.5, "Madison": 4.2}`, return `["Ritz", "Marriott"]`.

- Repeat the exercise using a list of tuples as the input. Ex: [("Ritz", 5.0), ("Marriott", 4.5), ("Madison", 4.2)].
