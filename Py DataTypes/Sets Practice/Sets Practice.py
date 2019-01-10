# 1.
# Write a Python program to create a set.
s = set()
print(s)
ss = set({1, 2, 3})
print(ss)

# 2.
# Write a Python program to iteration over sets.
ss = {1, 2, 3}
for i in ss:
    print(i)

# 3.
# Write a Python program to add member(s) in a set.
ss = {1, 2, 3, 4, 5}
print(ss)
ss.add("Hi")
print(ss)
ss.update(["Wo", "rld"])
print(ss)
ss.add("You")
print(ss)

# 4.
# Write a Python program to remove item(s) from set.
ss = {1, 2, 3, 4}
ss.pop()
ss.discard(1)  # Removes an item if it exist, else no-op
ss.remove(2)  # Removes an item if it exist, else KeyError
print(ss)

# 5.
# Write a Python program to create an intersection of sets.
s1 = {"Hi", "Dear", "Anton"}
s2 = {"Hi", "Dear", "deer"}
print(s1 & s2)
print(s1.intersection(s2))

# 6.
# Write a Python program to create a union of sets.
s1 = {"You", "Are", "Different"}
s2 = {"Yes", "You're", "right"}
print(s1 | s2)
print(s1.union(s2))

# 7.
# Write a Python program to create set difference.
s1 = {1, 2, 3, 4}
s2 = {5, 6, 3, 4}
print(s1 - (s1 & s2))
print(s1.difference(s2))

# 8.
# Write a Python program to create a symmetric difference. .
s1 = {1, 2, 3, 4}
s2 = {5, 6, 3, 4}
print((s1 | s2) - (s1 & s2))
print(s1.symmetric_difference(s2))

# 9.
# Write a Python program to issubset and issuperset.
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
print("s1: ", s1)
print("s2: ", s2)
print("Is s2 subset in s1? ", s2 <= s1)
print("Is s2 subset in s1? ", s2.issubset(s1))
print("------------------")
print("Is s1 superset to s2? ", s1 >= s2)
print("Is s1 superset to s2? ", s1.issuperset(s2))

# 10.
# Write a Python program to create a shallow copy of sets.
s = {1, 2, 4}
s1 = s.copy()
print(s1)
print(s)

# 11.
# Write a Python program to clear a set.
s = {1, 2, 3, 4, 5}
print(s)
s.clear()
print(s)

# 12.
# Write a Python program to use of frozensets.
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
# use isdisjoint(). Return True if the set has no elements in common with other.
print(x.isdisjoint(y))
# use difference(). Return a new set with elements in the set that are not in the others.
print(x.difference(y))
# new set with elements from both x and y
print(x | y)

# 13.
# Write a Python program to find maximum and the minimum value in a set..
s = {1, 2, 3, 4}
print(max(s))
print(min(s))

# 14.
# Write a Python program to find the length of a set.
s = {1, 2, 3, 4}
print(len(s))

# 15.
# Sieve of Eratosthenes - Set Version. Find prime numbers in range[2, 5000].
primes = set(range(2, 5001))
p = 2
while p <= 5000:
    s = p
    pp = True
    for j in range(2, p // 2):
        if p % j == 0:
            pp = False
            break
    if pp == False:
        primes.discard(p)
    else:
        k = p + p
        while k <= 5000:
            primes.discard(k)
            p += 1
            k = p + p
    p = s + 1

print(primes)