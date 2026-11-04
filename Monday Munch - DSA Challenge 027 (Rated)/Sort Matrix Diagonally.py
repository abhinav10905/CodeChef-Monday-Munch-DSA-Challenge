**QUESTION**
Sort Matrix Diagonally
A matrix diagonal consists of cells that follow the same diagonal. Two cells A[i][j] and A[x][y] belong to the same diagonal if i - j = x - y, using 0-based indexing.
Given an N x M matrix, sort the elements of each diagonal in ascending order from top-left to bottom-right.
For eg. see the following matrix and its diagonal sorting:

**INPUT**
The first line of input will contain two space separated integers N and M, denoting the no. of rows and columns in the input matrix.
Next N lines contains M space separated integers, the elements of the matrix.

**OUTPUT**
Output N lines, each containing M space separated integers, the elements of diagonally sorted matrix.

**CONSTRAINTS**
1≤N,M≤100
The elements of the matrix are non-negative and won't exceed 1000.

**CODE**
n,m=map(int,input().split())
l=[]
for i in range (n):
    a=list(map(int,input().split()))
    l.append(a)
hash={}
for i in range (0,n):
    for j in range (0,m):
        if (i-j) in hash:
            hash[i-j].append(l[i][j])
        else:
            hash[i-j]=[l[i][j]]
for i in hash:
    hash[i].sort()
for i in range (n-1,-1,-1):
    for j in range (m-1,-1,-1):
        l[i][j]=hash[i-j].pop()
for i in l:
    print(*i)

**ABOUT MY CODE**
TIME :-O(t*n(log(n)))
SPACE :- O(n)
APPROACH :- Math, Array, Hash Map, Sorting
