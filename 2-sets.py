#[]-arrays, {}-sets

f={'a','b','c'}
print(len(f))

for item in f:
    print(item) #no specific order, sets are unordered

f.add('d')
f.update('e','f')
print(f)

f.remove('c')
f.discard('e')
f.pop() #random element pop
print(f)

a={1,2,3,4,6,8}
b={6,7,8}

print(a|b) #A union B
print(a.union(b))

print(a&b) #A intersect B
print(a.intersection(b))

print(a-b)
print(a.difference(b))

#quiz
c={'a', 5, 'string', 'a', 312}
print(c)

d=set(['a','b','c']) #valid set
print(d)

set1 = set([4, 5, (6, 7)])

set1.update([5, 2, 6])

check1 = 2 in set1

check2 = 6 in set1

print(check1 and check2)