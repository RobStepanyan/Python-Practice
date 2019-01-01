# 5. 
# Write a Python program to add 'ing' at the end of a given 
# string (length should be at least 3). If the given string already 
# ends with 'ing' then add 'ly' instead. If the string length of the 
# given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly
def ingly(s):
	if len(s)<3:
		return s
	else:
		if s[-3:] == "ing":
			return s+"ly"
		return s+"ing"

s = input("Input: ")
print(ingly(s))


# 6.
# Write a Python function that takes a list of words 
# and returns the length of the longest one.
def no6(l):
	m = 0
	mm = ""
	for i in l:
		if len(i) > m:
			mm = i
			m = len(i)
	return mm

s = ["Python", "Java", "JavaScript", "PHP", "SQL", "Haskell"]
print(no6(s))


# 7.
# Write a Python program to count the 
# occurrences of each word in a given sentence.
def occ(s):
	w = s.split()
	d = {}
	for i in w:
		if i in d:
			d[i] +=1
		else:
			d[i] = 1
	return d

s = input("Input: ")
print(occ(s))