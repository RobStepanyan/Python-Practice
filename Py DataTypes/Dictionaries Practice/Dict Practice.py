# 1.
# Write a Python program to add a key to a dictionary.
d = {1: 10, 2: 20}
print(d)
d.update({3: 30})
print(d)

# 2.
# Write a Python program to concatenate following dictionaries to create a new one.
d1 = {1: 10, 2:20}
d2 = {3: 30, 4:40}
d3 = {5: 50, 6: 60}
print("d1:", d1)
print("d2:", d2)
print("d3:", d3)
d4 = {}
for d in (d1, d2, d3):
    d4.update(d)
print("d1 + d2 + d3 =", d4)

# 3.
# Write a Python script to check if a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def keyex(x, d):
    if x in d:
        return "Key exists."
    return "Key is not in specified dictionary."

x = int(input("What key to find: "))
print(keyex(x, d))

# 4.
# Write a Python program to iterate over dictionaries using for loops.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def itd(d):
    for k, v in d.items():
        print(k, v)

itd(d)

# 5.
#