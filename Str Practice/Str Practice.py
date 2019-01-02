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

# 8.
# Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def html(t, s):
	return f"<{t}>{s}</{t}>"

t = input("Input tag: ")
s = input("Input word: ")
print(html(t,s))

# 9.
# Write a Python function to convert a given string to all 
# uppercase if it contains at least 2 uppercase characters 
# in the first 4 characters. If the string contains less than
# 4 characters then return original string
def smup(s):
	if len(s) < 4:
		return s
	else:
		q = 0
		for i in s[:4]:
			if i == i.upper():
				q +=1
		if q >=2:
			return s.upper()
		return s

s = input("Input: ")
print(smup(s))

# 10.
# Write a Python program that accepts a comma separated 
# sequence of words as input and prints the unique 
# words in sorted form (alphanumerically).
s = input("Input: ")
s = s.split(", ")
print(", ".join(sorted(s)))

# 11.
# Write a Python program to print the following 
# floating numbers upto 2 decimal places.
n = float(input("Input: "))
print("N: {:.2f}".format(n))

# 12.
# Count occurrences of a substring in a string
s = input("String:")
ss = input("Substring: ")
print("There are " + str(s.count(ss)) + " " + ss + " in the sentence")

# 13.
# Write a Python program to reverse words in a string.
def rev(s):
	ss = ""
	s = s.split()
	for i in range(len(s)-1, -1, -1):
		ss += s[i] + " "
	return ss
s = input("Input: ")
print(rev(s))

# 14.
# Strip a set of characters from a string
def stch(s, c):
	return "".join(i for i in s if i not in c)

s = input("Input str.: ")
c = input("Input unallowed chars: ")
print(stch(s,c))

