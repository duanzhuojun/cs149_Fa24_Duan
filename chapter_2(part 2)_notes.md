## Announcement
1. Assignments:
   - Read [chapter 2](https://canvas.jmu.edu/courses/2035420/assignments/18966141?module_item_id=40563343)
   - Complete [HW 2](https://w3.cs.jmu.edu/cs149/f24/hw/hw2/) by 09/04(Wednesday, 11:00pm)
2. Today’s class
   1. Arithmetic Expressions lecture
   2. Group activity: Practice Problems
  




## Group activity: Practice Problems

### How to complete: 
1. Solve the first problem as a team [15 min]
2. Present solution(s) to the class [10 min]
3. Solve the second problem individually
4. Note that you don't need to submit anything for this activity

### 1: Average Speed Calculator
Write a program named `bike_speed.py` that asks the user for the length of a bike race in miles and their finishing time for the race in hours, minutes, and seconds. The program then outputs their average speed in both miles per hour and kilometers per hour. When you output the speed you should show exactly 2 digits past the decimal place. 1 mile = 1.60934 kilometers.

**Here is an example run of the program:**
```
How many miles did you race? 18.66
How much time did that take you in hours, minutes, and seconds?
  Hours: 0
  Minutes: 43
  Seconds: 49

Your speed was 25.55 mph, which is 41.12 kph.
```
**Hint 1:** Figure out how to solve the problem by hand before you try to code anything. You can't program what you can't solve with a pen and paper.

**Hint 2:** You'll want to get your time into one unit. Dealing with 3 separate units is not good for computation. At the end of the day, we need to calculate distance / time in hours to solve the problem, so what is the total time in hours? Notice that 0 hours, 43 minutes, and 49 seconds is ~0.7303 hours. How do you calculate this total? With $$0 + 43/60 + 49/3600$$. How can you do this for other numbers of hours, minutes, and seconds?

### 2: Miles, Furlongs, and Feet
Write a program called `feet_convert.py` that inputs a total number of feet and divide that number into miles, furlongs, and feet. (A furlong is some old English measure nobody uses anymore, but let's do it anyway!) 1 mile is 5280 feet, and 1 furlong is 660 feet.

**Here is an example run of the program:**
```
Enter a total number of feet: 12345

12345 total feet is 2 mile(s), 2 furlong(s), and 465 feet.
```
**Hint 1:** Figure out how to solve the problem yourself by hand on paper. You can't code something you don't know how to solve.

**Hint 2:** You will need to use floor division and remainder (`//` and `%`).

**Hint 3:** Create a variable for the remaining feet. In the example above, the remaining feet is initially 12345. Once you figure out there are two full miles in 12345 feet (2 full miles is 10560 feet), then the remaining feet is 1785. How many full furlongs are in 1785 feet? Well, 2 again, since 
. And finally after we remove those 1320 from 1785, the remaining feet is 465.
