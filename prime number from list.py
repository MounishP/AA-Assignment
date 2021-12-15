"""
WAPP to find th prime number from the list
"""

# for i in range(len(l)):
#     for j in range(2, i):
#         if i % j == 0:
#     if i > 0 or i=0:
#         print(i)

# if l > 1:
#     for i in range(2,len(l)):
#         if l % i == 0:
#             print(len(l), "is not prime")
#         break


# for i in range(0,len(l)):
#     if len(l) % i == 0:
#         count+=1
# if count == 0:
#     print(i)

# n = [2, 4, 3, 5, 6, 7, 99, 13, 17]
# count = 0
# for i in range(2,len(n)):
#     if len(n) % i == 0:
#         count += 1
# if count == 0:
#     print(len(n))
# else:
#     print("not prime")


# l = [2, 4, 3, 5, 6, 7, 99, 13, 17]
# print(l)
# for i in range(2,len(l)):
#     count = 0
#     for j in range(2,i):
#         if i % j == 0:
#             count += 1
#     if count == 0:
#         print(i, "is prime")



# l = [2, 4, 3, 5, 6, 7, 99, 13, 17]
# print(l)
#
# for i in l:
#   for j in range(1,i):
#     if i%j==0:
#       print(i,"is not prime")


l = [2, 4, 3, 5, 6, 7, 99, 13, 17]
print(l)
for i in l:
  count=0
  for j in range(2,i):
    if i%j==0:
      count+=1
  if count==0:
    print(i,"is prime")
