## Announcements
1. [Project 3](https://w3.cs.jmu.edu/cs149/f24/pa/pa3/) (due Dec 03)
   - Part C and D due Wednesday, 12/04
2. Thursday's class
   1. Quiz 6
      1. Based on Ch 11 and Ch 12 and PA 3
      2. Review questions from [Practice Quiz 6](https://w3.cs.jmu.edu/cs149/f24/quiz/practice6/)
      3. Study the challenge activities in zyBook
   2. Review and practice final exam
3. [CS/IT study night event](https://w3.cs.jmu.edu/cs149/f24/csit/wit_study_night/)
   1. This Thursday 5-7pm, in King348
   2. Snacks and musics!
   3. Meet CS149/CS159 professors and students


## Today's class
1. (30 mins) Solution of Practice quiz 6
2. (20 mins) PA3 QA
3. (25 mins) Review activities for chapters 9-12


### Solution of Practice quiz 6
- [Practice quiz 6 worksheet](https://w3.cs.jmu.edu/cs149/f24/quiz/practice6/)
- Please download the solution for Practice quiz 6:
  - [Solution for Practice quiz 6](pogil_sheet\PracticeQuiz6_Answers.pdf)
- Review the solution and ask questions.

### PA3 part C
#### About 'Test circular friendships':
Here is the test cases in gradescope:

```Python
data = {"A": ["B"], "B": ["C"], "C": ["B", "A"]}
assert influence(data, "B") == 4, "check return values in influence()"
assert separation(data, "B", "A") == 2, "check return values in separation()"
```
If your code cannot pass the case above, I will return points to you manually.

### Review activities for chapters 9-12
- [Review activities](https://duanzhuojun.github.io/cs149_Fa24_Duan/review2.html)
- Complete it before the final exam.
