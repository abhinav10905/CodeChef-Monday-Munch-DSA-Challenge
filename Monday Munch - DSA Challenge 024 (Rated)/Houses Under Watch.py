**QUESTION**
Houses Under Watch
A street has 100 houses, numbered 1 through 100 from left to right. Cops are stationed at M distinct houses, given by A1,A2,…,AM.
Each cop can travel up to X house positions per minute and has Y minutes to search. Therefore, a house numbered H is within reach of a cop at house Ai if 
∣H−Ai∣≤X×Y. The cop's own house is also within reach.
Devu wants to hide in a house that is outside the reach of every cop. Find the number of such houses.

**INPUT**
The first line contains an integer T — the number of test cases.
For each test case:
The first line contains three space-separated integers M, X, and Y.
The second line contains M space-separated integers A1,A2,…,AM — the houses where cops are stationed.

**OUTPUT**
For each test case, print the number of safe houses on a separate line.

**CONSTRAINTS**
1≤T≤104
1≤M,X,Y≤10
1≤Ai≤100
All Ai are distinct.

**CODE**
# cook your dish here
for t in range (int(input())):
    m,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    hash=[0]*102
    for i in a:
        z=x*y
        n=max(1,i-z)
        hash[n]+=1
        n=min(100,i+z)
        hash[n+1]-=1
    c=0
    d=0
    for i in range (1,101):
        d+=hash[i]
        if d==0:
            c+=1
    print(c)
