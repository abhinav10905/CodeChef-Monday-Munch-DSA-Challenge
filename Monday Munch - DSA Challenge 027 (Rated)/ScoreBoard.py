**QUESTION**
ScoreBoard
A game has two rounds. A player scores A points in the first round and B points in the second round. The scoreboard displays C as the total score.
Determine whether the displayed total is correct.

**INPUT**
The first line contains an integer T, the number of test cases.
Each test case contains three space-separated integers A, B, and C.

**OUTPUT**
For each test case, print YES if the displayed total is correct, or NO otherwise, on a separate line.
You may print the answer in any combination of uppercase and lowercase letters.

**CONSTRAINTS**
1≤T≤100
0≤A,B,C≤100

**CODE** 
# cook your dish here
for t in range (int(input())):
    a,b,c=map(int,input().split())
    if a+b==c:
        print("YES")
    else:
        print("NO")
