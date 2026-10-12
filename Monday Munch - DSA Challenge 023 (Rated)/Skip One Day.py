**QUESTION**
Skip One Day
Chef has recorded his trading results for N days in an array A. On day i, he earned Ai coins. A negative value represents a loss.
Chef wonders what his total profit would have been if he had skipped exactly one day. Skipping a day removes its profit or loss from the total; the results of all other days remain unchanged.
Find the maximum total profit he could have earned. The answer may be negative.

**INPUT**
The first line contains an integer T — the number of test cases.
For each test case:
The first line contains an integer N — the number of days.
The second line contains N space-separated integers A1,A2,…,AN.

**OUTPUT**
For each test case, print the maximum total profit after skipping exactly one day on a separate line.

**CONSTRAINTS**
1≤T≤1000
1≤N≤105
−100≤Ai≤100
The sum of N over all test cases won't exceed 106.

**CODE**
# cook your dish here
for t in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=0
    c=a[0]
    for i in a:
        b+=i
        if i<c:
            c=i
    b-=c
    print(b)

**ABOUT MY CODE**
TIME :-O(t*n)
SPACE :- O(1)
APPROACH :- Math, Array
