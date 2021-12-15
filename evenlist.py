# write a program to print even numbers in list
l = [1, 2, 3, 5, 6, 8, 9, 222, 345, 456]
for i in range(len(l)):
    if l[i] % 2 == 0:
        print(l[i])
