"""
371 = 3*3*3 + 7*7*7 + 1*1*1.
"""

for num in range(1,1001):
    sum = 0
    temp = num
    count = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if num == sum:
            print(num,"is armstrong numbers")