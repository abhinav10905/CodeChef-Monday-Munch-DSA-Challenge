**QUESTION**
Pyramid of Bricks
You are given N bricks and want to construct a pyramid. A pyramid is built in layers where the i-th layer (from the top) requires i bricks.
The 1st layer requires 1 brick.
The 2nd layer requires 2 bricks.
The 3rd layer requires 3 bricks.
And so on.
Your task is to determine the maximum number of complete layers you can build using the given N bricks.

**INPUT**
The first line of the input contains the number of test cases, T.
For each test case, a single integer, N, represents the number of bricks available.

**OUTPUT**
For each test case print a single integer representing the maximum number of complete layers you can build in new line.

**CONSTRAINTS**
1≤T≤50
1≤N≤109

**CODE**
def main():
    # Write your code here
    for t in range (int(input())):
        n=int(input())
        c=0
        i=1
        while i<=n:
            c+=1
            n-=i
            i+=1
        print(c)
if __name__ == "__main__":
    main()

**ABOUT MY CODE**
TIME :-O(t*(root(n)))
SPACE :- O(1)
APPROACH :- Math
