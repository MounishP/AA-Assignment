
for n in range(1,1001):
    sum = 0
    temp = n
    while temp != 0:
        digit = temp % 10 #splitting of number using place values
        sum += digit ** 3
        temp //= 10
        # print (sum)
    if n == sum:
        print(n,"is a armstrong number")