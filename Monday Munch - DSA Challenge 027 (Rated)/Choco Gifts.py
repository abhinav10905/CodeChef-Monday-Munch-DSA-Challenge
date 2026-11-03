**QUESTION**
Choco Gifts
A chocolate shop prepares two types of gift boxes: large boxes containing 4 chocolates each and small boxes containing 2 chocolates each.
The shop has N chocolates, where N is even. It uses them to prepare as many large boxes as possible, then prepares small boxes with the remaining chocolates.
A customer wants to buy a small gift box. Determine whether at least one will be available.

**INPUT**
The first line contains an integer T, the number of test cases.
Each test case contains a single integer N, the number of chocolates.

**OUTPUT**
For each test case, print YES if at least one small gift box is available, or NO otherwise, on a separate line.
You may print the answer in any combination of uppercase and lowercase letters.

**CONSTRAINTS**
1≤T≤100
2≤N≤1000
N is even.

**CODE**
# cook your dish here
for t in range (int(input())):
    n=int(input())
    if n%4==0:
        print("NO")
    else:
        print("YES")
