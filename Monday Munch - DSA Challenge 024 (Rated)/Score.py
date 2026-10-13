**QUESTION**
Score
Chef takes part in a discus throw competition, where each player gets three throws. A player's final score is the longest distance achieved among their three throws.
Chef's throws cover distances of A, B and C units. Find his final score.

**INPUT**
The first line contains an integer T — the number of test cases.
Each test case contains three space-separated integers A, B, and C — the distances of Chef's three throws.

**OUTPUT**
For each test case, print Chef's final score on a separate line.

**CONSTRAINTS**
1≤T≤100
1≤A,B,C≤100

**CODE**
# cook your dish here
for t in range (int(input())):
    a,b,c=map(int,input().split())
    print(max(a,b,c))

**ABOUT MY CODE**
TIME :-O(t)
SPACE :- O(1)
APPROACH :- Math
