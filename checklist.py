# list methods and tuple methods

l = [1, 2, 3, 2, 5, 1, 2, 8, 9, 8, 9, 7, 4, 5, 6, 1, 2, 10]

print(l)
print(l.count(2))
print(sorted(l,reverse=True))
print(l.copy())
l.insert(5, 15)
print(l)
print(l.index(5))
l.reverse()
print(l)
l.clear()
