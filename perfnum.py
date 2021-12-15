""""
waap to check if the given number is perfect number
a number is perfect if sum of its factors give that number
6=1+2+3
"""

i=int(input("enter the number:"))
count=0
for j in range(1, i):
    if (i % j == 0):
        count=count+i
if (count==i):
    print ("perfect number")
else:
    print("not a Perfect number")