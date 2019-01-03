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