# 1. Reverse a string
a = "!dlrow olleH"
backward = a[::-1]

print(backward)


# 2. Dims as variables
array = [5, 10, 15, 20]
five, ten, fift, twent = array

print(five)
print(ten)
print(fift)
print(twent)


# 3. itertools
c = [[1, 2], [3, 4], [5, 6]]
import itertools as it
newlist = list(it.chain.from_iterable(c))

print(c)
print(newlist)


# 4. Unpacking
a, *b, c = [1, 2, 3, 4, 5]

print(a)
print(b)
print(c)


# 5. Enumerate
for i,w in enumerate(array):
    print(i,w)


# 6. Name slice
a = [0, 1, 2, 3, 4, 5]
LASTTHREE = slice(-3, None)
slice(-3, None, None)

print(a[LASTTHREE])


# 7. Group Adjacent Lists
a = [1, 2, 3, 4, 5, 6]  
group_adjacent = lambda a, k: zip(*([iter(a)] * k)) 

print(group_adjacent(a, 3))
print(group_adjacent(a, 2))
print(group_adjacent(a, 1))


# 8. next() iteration
g = (x ** 2 for x in range(10))

print(next(g))
print(next(g))


# 9. Counter
import collections
A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7]) 

print(A.most_common(1))
print(A.most_common(3))


# 10. Dequeue
Q = collections.deque()
Q.append(1)
Q.appendleft(2)
Q.extend([3, 4])
Q.extendleft([5, 6])
Q.pop()
Q.popleft()
Q.rotate(3)
Q.rotate(-3)
print(Q)
