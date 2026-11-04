**QUESTION**
Power Badges
There are N players in a game. Player i has a power level of Ai.
A player earns a badge if the number of players with power levels less than or equal to their own is strictly greater than the number of players with higher power levels. The player themselves is included in the first count.
Find the number of players who earn a badge.

**INPUT**
The first line contains an integer T, the number of test cases.
For each test case:
The first line contains an integer N, the number of players.
The second line contains N space-separated integers A1,A2,…,AN, the power levels of the players.

**OUTPUT**
For each test case, print the number of players who earn a badge on a separate line.

**CONSTRAINTS**
1≤T≤1000
1≤N≤100
0≤Ai≤100

**CODE**
# cook your dish here
for t in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    hash={}
    for i in a:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    c=0
    d=0
    for i in hash:
        c+=hash[i]
        if c>(n/2):
            d+=hash[i]
    print(d)
