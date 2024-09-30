## Announcement
1. Assignments:
- Complete the chapter 6 reading in zybook by next Monday 11:59pm
- Complete [HW 6](https://w3.cs.jmu.edu/cs149/f24/hw/hw6/) by 10/02(Wednesday, 11:00pm)
- Complete the HW6 reflection quiz in canvas by end of this Thursday. 

2. Practice quiz 3 this Thursday(10/03)
- cover chapters 5 and 6: function, for loop, range, and so on

## Today's class
- (40 mins) POGIL activity: `range` function and `for` Each Index
- (10 mins) Demo: `for` each value vs `for` each index
- (25 mins) Practice

## POGIL activity: `range` function and `for` Each Index
- Complete the two models in the worksheet in a group
- Discussion
- POGIL worksheet in [pdf](pogil_sheet\Act06-ForRange_Student.pdf)
- The solution of the POGIL activity will be avilable in canvas tomorrow(10/02)

## Demo: `for` each value vs `for` each index
**Task**: 

```
Write a python function `index_max(lst)` to find the index of the maximum value in a list.

Ex: `index_max([13, -5, 100, 0, 77])` returns 2, because the maximum value 100 is at index 2.
```
Solution using `range`

```python
def index_max(lst):
    max_value = lst[0]
    max_index = 0
    for i in range(len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i
    return max_index

if __name__ == "__main__":
    assert index_max([13, -5, 100, 0, 77]) == 2
```
Solution using `enumerate`

```python
def index_max(lst):
    max_value = lst[0]
    max_index = 0
    for i, value in enumerate(lst):
        if value > max_value:
            max_value = value
            max_index = i
    return max_index

if __name__ == "__main__":
    assert index_max([13, -5, 100, 0, 77]) == 2
```

## Extra Practices in CodingBat

**Note**: Do not use the built-in `min()`, `max()`, or `sum()` functions for any of these problems.

- [List-2 Problems](https://codingbat.com/python/List-2)
    - Easier: count_evens, has22
    - Medium: big_diff, sum13
    - Harder: centered_average, sum67

- [String-2 Problems](https://codingbat.com/python/List-2)
    - Easier: double_char, count_hi
    - Medium: count_code, cat_dog
    - Harder: xyz_there, end_other