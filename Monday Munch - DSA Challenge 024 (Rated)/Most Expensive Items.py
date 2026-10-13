**QUESTION**
Most Expensive Items
Chef is given the prices of N items and wants to buy exactly K of them.
Find the maximum possible total price of the K items he can choose.

**INPUT**
The first line contains an integer T — the number of test cases.
For each test case:
The first line contains two space-separated integers N and K — the number of items and the number of items Chef wants to buy.
The second line contains N space-separated integers C1,C2,…,CN — the prices of the items.

**OUTPUT**
For each test case, print a single integer — the total cost of the K most expensive items.

**CONSTRAINTS**
1≤T≤100
1≤K≤N≤100
1≤Ci≤100

**CODE**
# cook your dish here
for t in range (int(input())):
    n,k=map(int,input().split())
    c=list(map(int,input().split()))
    c.sort()
    c=c[::-1]
    i=0
    d=0
    while i<k:
        d+=c[i]
        i+=1
    print(d)

**ABOUT MY CODE**
TIME :-O(t*n(log(n)))
SPACE :- O(n)
APPROACH :- Math, Array, Sorting
