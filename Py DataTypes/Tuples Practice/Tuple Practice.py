# 1. 
# Create an empty tuple
t1 = ()
print(t1)
t2 = tuple()
print(t2)

# 2.
# Create a tuple with different data types
t = ("Hey", True, 1)
print(t)

# 3.
# Write a Python program to unpack a tuple in several variables.
tp = (1, 2, 3)
n1, n2, n3 = tp
print(n1)
print(n2)
print(n3)

# 4.
# Add an item in a tuple with different ways.
tuplex = (1, 2, 3, 4)
print(tuplex)

tuplex = tuplex + (5,)
print(tuplex)

tuplex = list(tuplex)
tuplex.append(6)
print(tuple(tuplex))
tuplex.remove(6)
tuplex = tuple(tuplex)
print(tuplex)

tuplex = tuplex[:4] + (6,) + tuple(reversed(tuplex[:4]))
print(tuplex)

# 5.
# Tuple to a string
t = ("H", "o", "w", "d", "y", "h", "o", ", ", "b", "ch.")
s = "".join(t)
print(s)

# 6.
# Get the 4th element and 4th element from last of a tuple.
t = (1, 2, 3, "4", 5, 6, "7", 8, 9 ,10)
print("4th element:", t[3])
print("4th element from last:", t[-4])

# 7.
# Create the colon of a tuple.
from copy import deepcopy
t = (1, 2, [])
print(t)
tt = deepcopy(t)
tt[2].append("Hi")
print(tt)
print(t)

# 8.
# Find how many times do specified item appears in the tuple.
i = input("What to find: ")
t = (1, 2, 3, 4, 5, i)
print(t.count(i))

# 9.
# Check whether an element exists within a tuple.
i = input("Input to check presence: ")
t = (1, 2, 3, 4, 5)
if i in t:
	print(i, "exists in", t)
else:
	print(i, "is not in", t)

# 10.
# Write a Python program to remove an item from a tuple.
t = (1, 2, 3, 4, 5, 6)
i = input("What you want to remove from tuple? ")
if i in t:
	t = t[:t.index(i)] + t[t.index(i)+1:]
	print("Removed", i, "from a tuple.\n", t)
else:
	print(i, "is not in tuple.")

# 11
# Write a Python program to find the index of an item of a tuple.
i = input("What item's index you want to find? ")
t = (1, 2, 3, 4, 5, 6, i)
print(t.index(i))

# 12.
# Write a Python program to find the length of a tuple.
t = (1, 2, 3, 4, 5)
print(len(t))

# 13.
# Convert a tuple to a dictionary.
t = ((1, "H"), (2, "e"), (3, "l"), (4, "l"), (5, "o"))
d = (dict((x, y) for x, y in t))
print(d)

