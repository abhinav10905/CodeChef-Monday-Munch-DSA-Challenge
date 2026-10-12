**QUESTION**
Discount
You are buying an item that costs N rupees.
The shopkeeper gives you a special discount: you may remove exactly one digit from the decimal representation of N. The remaining digits, in the same order, form the new price you have to pay.
Your task is to find the minimum possible price after removing exactly one digit.
The resulting number may contain leading zeros. However, while printing the answer, leading zeros must not be printed.

**INPUT**
The first line contains an integer T, the number of test cases.
Each of the next T lines contains a single integer N.

**OUTPUT**
For each test case, print the minimum price that can be obtained after removing exactly one digit from N.

**CONSTRAINTS**
1≤T≤105
10≤N≤109

**CODE**
# cook your dish here
for t in range (int(input())):
    n=input()
    j=len(n)-1
    for i in range (0,len(n)-1):
        if n[i]>n[i+1]:
            j=i
            break
    c=n[:j]+n[j+1:]
    if int(c)>0:
        print(int(c))
    else:
        print("0")

**ABOUT MY CODE**
TIME :-O(n)
SPACE :- O(n)
APPROACH :- String
