**QUESTION**
Ticket Queue
There are N people waiting in a queue at a single ticket counter. The i-th person requires Ti units of service time.
The counter serves the person at the front of the queue for exactly 1 unit of time. If that person still requires more service, they move to the back of the queue. Otherwise, they leave the queue.
Given an index K (0≤K<N), find the total time elapsed until the person who was initially at index K completes their service.

**INPUT**
The first line contains two space-separated integers N and K — the number of people and the index of the target person.
The second line contains N space-separated integers T0,T1,…,TN−1 — the service time required by each person.

**OUTPUT**
Print a single integer — the total time elapsed until the K-th person completes their service.

**CONSTRAINTS**
1≤N≤2×105
0≤K<N
1≤Ti≤109

**CODE**
# cook your dish here
n,k=map(int,input().split())
t=list(map(int,input().split()))
c=0
i=0
while i<n:
    if t[i]<t[k]:
        c+=t[i]
    elif t[i]==t[k] and i<=k:
        c+=t[i]
    elif i<k:
        c+=t[k]
    else:
        c+=(t[k]-1)
    i+=1
print(c)

**ABOUT MY CODE**
TIME :-O(n)
SPACE :- O(1)
APPROACH :- Array
