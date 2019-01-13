# 1.
# Write a Python program to add a key to a dictionary.
d = {1: 10, 2: 20}
print(d)
d.update({3: 30})
print(d)

# 2.
# Write a Python program to concatenate following dictionaries to create a new one.
d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
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
# Write a Python program to sum all the items in a dictionary.
d = {1: 10, 2: 20, 3: 30}
print(sum(d.values()))


# 6.
# Write a Python program to multiply all the items in a dictionary.
def md(d):
    prd = 1
    for x in d.values():
        prd *= x
    return prd


print(md({1: 10, 2: 20, 3: 30}))


# 7.
# Write a Python script to generate and print a dictionary
# that contains a number (between 1 and n) in the form (x, x*x).
def cd(n):
    d = {}
    for i in range(1, n + 1):
        d[i] = i ** 2
    return d


n = int(input("Input n: "))
print(cd(n))

# 8.
# Write a Python script to print a dictionary where the keys are numbers between
# 1 and 15 (both included) and the values are square of keys.
d = {i: i * i for i in range(1, 16)}
print(d)

# 9.
# Write a Python script to merge two Python dictionaries.
d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d = d1.copy()
d.update(d2)
print(d)

# 10.
# Write a Python program to remove a key from a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40}
print("D: ", d)
k = int(input("What key to remove? "))
if k in d:
    del d[k]
    print("Key was successfuly deleted!")
    print("D: ", d)
else:
    print("Key do not exist!")

# 11.
# Write a Python program to map two lists into a dictionary.
k = ['red', 'green', 'blue']
v = ['#FF0000', '#008000', '#0000FF']
d = dict(zip(k, v))
print(d)

# 12.
# Write a Python program to sort a dictionary by key.
d = {'red': '#FF0000',
     'green': '#008000',
     'black': '#000000',
     'white': '#FFFFFF'}

for k, v in sorted(d.items()):
    print(k, ":", v)

# 13
# Write a Python program to get the maximum and minimum value in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40}
print("Min:", min(d.values()))
print("Max:", max(d.values()))

# 14.
# Write a Python program to remove duplicates from Dictionary.
student_data = {'id1':
                    {'name': ['Sara'],
                     'class': ['V'],
                     'subject_integration': ['english, math, science']
                     },
                'id2':
                    {'name': ['David'],
                     'class': ['V'],
                     'subject_integration': ['english, math, science']
                     },
                'id3':
                    {'name': ['Sara'],
                     'class': ['V'],
                     'subject_integration': ['english, math, science']
                     },
                'id4':
                    {'name': ['Surya'],
                     'class': ['V'],
                     'subject_integration': ['english, math, science']
                     },
                }

s_d = {}
for k, v in student_data.items():
    if v not in s_d.values():
        s_d[k] = v

student_data = s_d

# 15.
# Write a Python program to check a dictionary is empty or not.
d = {}
if not bool(d):
    print("Dictionary is empty!")

# 16.
# Write a Python program to print all unique values in a dictionary.
L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print("List:", L)
un = set(v for d in L for v in d.values())
print("Unique Values of List:", un)

# 17.
# Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d = Counter(d1) + Counter(d2)
print(d)

# 18.
# Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
q = sum(d['success'] for d in student)
print(q)

# 19.
# Write a Python program to sort a list alphabetically in a dictionary.
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
nums = {x: sorted(y) for x, y in num.items()}
num = nums

# 20.
# Write a Python progrm to sort Counter by value.
d = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
print(sorted(d.items(), key=lambda x: x[1], reverse=True))
