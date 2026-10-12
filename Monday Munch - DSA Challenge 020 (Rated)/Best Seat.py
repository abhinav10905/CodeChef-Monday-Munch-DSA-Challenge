**QUESTION**
Best Seat
You are given an array A of N distinct integers, where Ai represents the number of the i-th available seat in a cinema hall.
The center position is defined as the average of the smallest and largest values in A.
This position may not be an integer and may not correspond to an available seat.
Find the available seat closest to the center position. If two seats are equally close, choose the one with the smaller seat number.

**INPUT**
The first line contains an integer N, the number of available seats.
The second line contains N distinct integers A1,A2,…,AN in any order.

**OUTPUT**
Print a single integer — the chosen seat number.

**CONSTRAINTS**
1≤N≤1000
1≤Ai≤109 
All seat numbers are distinct.

**CODE**
# cook your dish here
n=int(input())
z=list(map(int,input().split()))
a=0
b=0
c=(min(z)+max(z))/2
z.sort()
for i in z:
    if abs(c-i)<abs(c-a):
        a=i
        b=abs(c-i)
print(a)

**ABOUT MY CODE**
TIME :-O(n*logn)
SPACE :- O(1)
APPROACH :- Math, Array, Sorting 
