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








