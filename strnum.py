"""
Strong number -> 145 - 1! + 4! + 5! = 145
1. take input
2. separate the digits
3. find factorial of the digits
4. sum of factorials
5. compare with given number
"""
# n =int(input("enter a number:"))
n=145
sum =0
fact=1

for i in str(n):
    m = int(i)
    for i in (1,m):
        fact=fact*i
        print(fact)
        sum = sum + fact
        print(sum)
if (sum == n):
    print(" The given number is a Strong Number")
else:
    print(" The given number is not a Strong Number")