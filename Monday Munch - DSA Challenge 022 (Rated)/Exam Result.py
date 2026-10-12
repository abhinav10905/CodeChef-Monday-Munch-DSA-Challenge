**QUESTION**
Exam Result
Chef has received his exam results. He answered C questions correctly and W questions incorrectly. Each correct answer earns M marks, while each incorrect answer deducts P marks.
Chef needs a final score of at least R marks to pass. Determine whether he passes the exam. His final score may be negative.

**INPUT**
The only line contains five space-separated integers C, M, W, P, and R.

**OUTPUT**
Print YES if Chef passes the exam, otherwise print NO.

**CONSTRAINTS**
0≤C,W≤100
1≤M,P≤10
0≤R≤1000

**CODE**
# cook your dish here
c,m,w,p,r=map(int,input().split())
a=c*m
a-=(w*p)
if a>=r:
    print("YES")
else:
    print("NO")

**ABOUT MY CODE**
TIME :-O(1)
SPACE :- O(1)
APPROACH :- Math
