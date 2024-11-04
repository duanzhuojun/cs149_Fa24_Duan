# Practice Quiz 4 (Ch 7–8)

<style>
  samp, .samp {
    display: inline !important;  /* inline = show answers, none = hide answers */
  }
</style>

<p style="float: right; font-size: large; margin-top: -3.25rem;">
Name: ___________________________________
</p>

<div style="display: flex; gap: 1rem; align-items: end;">
  <div style="font-style: italic;">
  This work complies with the JMU Honor Code.
  I have neither given nor received unauthorized assistance.
  I will not discuss the quiz contents with anyone who has not taken the quiz.
  </div>
  <div>
  Initials:&nbsp;____________
  </div>
</div>


## Question 1 &nbsp;(3 pts)

``` py
my_dog = "Pongo"
all_dogs = ["Pongo", "Nina", "Duke"]

def feed_dog(dog_to_feed):
    message = "appreciates the meal!"
    print(dog_to_feed, message)

feed_dog(my_dog)
print(len(all_dogs))
```

Determine the namespace (**built-in**, **global**, or **local**) of each item.

Item       | Namespace             | | Item          | Namespace
---------- | --------------------- | | ------------- | ---------------------
`my_dog`   | <samp>global</samp>   | | `message`     | <samp>local</samp>
`print`    | <samp>built-in</samp> | | `dog_to_feed` | <samp>local</samp>
`feed_dog` | <samp>global</samp>   | | `len`         | <samp>built-in</samp>


## Question 2 &nbsp;(4 pts)

For each code snippet, determine: (1) how many times the loop runs; (2) what is printed on the screen.

---
``` py
flavors = ["vanilla", "chocolate", "mint", "strawberry", "banana"]

i = 4
while i >= 0:
    print(flavors[i], end=" ")
    i -= 2
print(i)
```

**How many times the loop runs:** &nbsp;
<samp>3</samp>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**What is printed on the screen:** &nbsp;
<samp>banana mint vanilla -2</samp>

<div style="page-break-before: always;"></div>

---
``` py
i = 0

while i < 20:
    i += 1

    if i % 2 == 0:
        continue
    elif i == 5:
        break
    else:
        print(i, end=" ")
```

**How many times the loop runs:** &nbsp;
<samp>5</samp>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**What is printed on the screen:** &nbsp;
<samp>1 3 </samp>


## Question 3 &nbsp;(3 pts)

**money.py**
``` py
def get_change(price, paid):
    return paid - price

print("Money", end=" ")

if __name__ == "__main__":
    print(get_change(3, 4), end=" ")
```

**restaurant.py**
``` py
import money

BURGER_PRICE = 3

def process_payment(customer, paid):
    change = money.get_change(BURGER_PRICE, paid)
    print(customer, end=" ")
    print(change, end=" ")

process_payment("Ronald", 5)
```

---
a. What will be printed when `money.py` is run?
&nbsp; <samp>Money 1</samp>

---
b. What will be printed when `restaurant.py` is run?
&nbsp; <samp>Money Ronald 2</samp>


<div style="page-break-before: always;"></div>

## Question 4 &nbsp;(7 pts)

Implement the following function.
Please write clearly and indent your code using four spaces.

<pre>
def <b>count_woofs</b>(noises):
    """Return the number of times "woof" appears in a list.

    You MUST use a <b>while</b> loop! Use of count() is NOT allowed.

    Example: count_woofs(["woof", "meow", "woof"]) returns 2, because
    "woof" appears two times in the list.

    Args:
        noises (list): a list of strings.

    Returns:
        int: number of times "woof" appeared.
    """
</pre>

<pre class="samp">
    i = 0
    count = 0
    while i < len(noises):
        if noises[i] == "woof":
            count += 1
        i += 1
    return count
</pre>


<div style="page-break-before: always;"></div>

## Question 5 &nbsp;(8 pts)

Implement the following function.
Please write clearly and indent your code using four spaces.

<pre>
def <b>get_numbers</b>(limit):
    """Get a list of numbers from the user that are less than the limit.

    Repeatedly prompts the user to input numbers (int) into a list until
    the user enters a number that is greater than or equal to the limit.

    In the following example, get_numbers(5) is called. The user inputs
    the numbers 1, 3, and 5. The function then returns the list [1, 3].

    >>> get_numbers(5)
    Enter a number: 1
    Enter a number: 3
    Enter a number: 5
    [1, 3]

    Args:
        limit (int): The limit for determining when to stop.

    Returns:
        list: The numbers entered (except for the last one).
    """
</pre>

<pre class="samp">
    numbers = []
    while True:
        value = int(input("Enter a number: "))
        if value >= limit:
            return numbers
        numbers.append(value)
</pre>
