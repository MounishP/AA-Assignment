"""
WAPP to find the given number is perfect number
"""

# n = int(input("enter the number:"))
# i = 0
# for j in range(1, n):
#     if n % j == 0:
#         i = i + 1
# if i == n:
#     print("True")

n = int(input("enter the number:"))
# count = 0
for i in range(1, n): #i=2
    count=0  #0
    if n % i == 0:
        count += i  #0+1=1
if count == n:
    print("true")
else:
    print("false")

