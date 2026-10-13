**QUESTION**
Sweet Shopping
Chef visits a shop with N sweets arranged in a row. The i-th sweet costs Ai​ rupees, and Chef has M rupees.
Chef can choose any starting position, but the sweets he buys must form a consecutive segment of the row. Their total cost must be at most M. The row does not wrap around: the first sweet does not follow the last.
Find the maximum number of sweets Chef can buy. If he cannot afford any sweet, the answer is 0.

**INPUT**
The first line contains an integer T — the number of test cases.
For each test case:
The first line contains two space-separated integers N and M.
The second line contains N space-separated integers A1,A2,…,AN.

**OUTPUT**
For each test case, print the maximum number of sweets Chef can buy on a separate line.

**CONSTRAINTS**
1≤T≤1000
1≤N≤105
1≤M≤109
1≤Ai≤109
The sum of N over all test cases does not exceed 105.

**CODE**
# cook your dish here
for t in range (int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    i=0
    j=0
    d=0
    sum=0
    while i<n:
        if sum>m:
            c=max(c,d-1)
            sum-=a[j]
            j+=1
            d-=1
        else:
            sum+=a[i]
            i+=1
            d+=1
    if sum>m:
        c=max(c,d-1)
    elif sum<=m:
        c=max(c,d)
    print(c)
