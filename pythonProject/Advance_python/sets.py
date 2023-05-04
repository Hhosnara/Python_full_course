'''
myset = {1, 2, 3}
print(myset)

myset.add(1)
myset.add(2)
myset.add(3)

print(myset.pop())
print(myset)


for x in myset:
    print(x)'''


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(primes)
print(u)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setA.symmetric_difference(setB)
print(diff)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.update(setB)
print(setA)





















