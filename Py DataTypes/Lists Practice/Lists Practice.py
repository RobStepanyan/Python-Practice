# 1.
# Write a Python program to sum all 
# the items in a list.
l = [1,1,1,2,2,3,4,5]
print(sum(l))

# 2.
# Write a Python program to multiplies 
# all the items in a list.
def prodl(l):
	prd = 1
	for i in l:
		prd *=i
	return prd

l = [1,1,1,2,2,3,4,5]
print(prodl(l))

# 3.
# Write a Python program to get 
# the largest number from a list.
l = [1,1,2,4,5,7,8,5,6]
print(max(l))

# 4.
# Write a Python program 
# to get the smallest number from a list.
l = [2, 4, 6, 3, 4, 1, 5]
print(min(l))

# 5.
# Write a Python program to count the number of strings where
# the string length is 2 or more and the first and last character
# are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']. Expected Result : 2
l = [1, 2, 3,4 ,4, 5 ,3, 54, 6, 3223, "aba"]
q = [1 for i in l if len(str(i))> 1 and str(i)[0] == str(i)[-1]]
print(sum(q))

# 6.
# Write a Python program to get a list, sorted in 
# increasing order by the last element in each tuple 
# from a given list of non-empty tuples.
x = lambda x: x[1]
l = [(2,1), (2,2), (2,1), (2,4), (2,3)]
print(sorted(l, key = x))

# 7.
# Write a Python program to remove duplicates 
# from a list. Write a Python program to remove
# duplicates from a list.
l = [1, 1, 2, 2, 3, 3,3]
def rmvdup(l):
	new_l = []
	for i in l:
		if i not in new_l:
			new_l.append(i)
	return new_l

print(rmvdup(l))

# 8.
# Write a Python program to check a list is empty or not.
def emptn(l):
	if len(l) == 0:
		return "List is empty!"
	return "List is NOT empty!"

l = []
l2 = ["I'm", "NOT", "Empty", "."]
print("List1: ", emptn(l))
print("List2: ", emptn(l2))

# 9.
# Write a Python program to 
# convert a list of characters into a string.
l = ["H", "e", "l", "l", "o"]
print("".join(l))

# 10.
# Write a Python program to find the 
# index of an item in a specified list
l = ["Python", "JavaScript", "Haskell", "PHP"]
ch = input("What item's index to find: ")
print(l.index(ch))

# 11.
# Write a Python program to append a list to the second list.
l1 = [1,1,1,1,1]
l2 = [2,2,2,2,2]
print(l1 + l2)

# 12.
# Write a Python program to select an item randomly from a list.
import random
l = [1, 2, 3,5,6,7,8,5]
print(random.choice(l))

# 13.
# Write a python program to check 
# whether two lists are circularly identical.
def circ(l1, l2):
	ans = " ".join(map(str,l1)) in " ".join(map(str,l2*2))
	return ans

l1 = [1,2,3,9,9,9]
l2 = [9,1,2,3,9,9]
print(circ(l1,l2))

# 14.
# Write a Python program to get the 
# frequency of the elements in a list.
import collections as cll
l = [1,2,3,4,5,1,2,3,4,5,6]
print(cll.Counter(l))

# 15.
# Write a Python program to count the number 
# of elements in a list within a specified range.
def inrng(l, s, e):
	q = 0
	for i in l:
		if i >=s and i<=e:
			q +=1
	return q

s = input("Count items in range (from): ")
e = input("Count items in range (to): ")
l = ["a", "b", "c", "d", "e"]
print(inrng(l, s, e))

# 16.
# Write a Python program using Sieve of 
# Eratosthenes method for computing primes 
# upto a specified number.
def prime(n):
	for i in range(2, n+1):
		for j in range(2, i):
			if i%j == 0:
				break
		else:
			print(i, " ")
prime(10)

# 17.
# Write a Python program to create a list by 
# concatenating a given list which range goes from 1 to n.
l = ["A", "B", "C"]
n = int(input("Input n: "))
print(["{}{}".format(x, y) for y in range(1, n +1) for x in l])

# 18.
# Write a Python program to convert list to list of dictionaries.
color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{"color_name": n, "color_code": c} for n, c in zip(color_name, color_code)])
