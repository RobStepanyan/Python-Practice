# 1.
# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def freq(s):
	d = {}
	for char in s:
		if char in d.keys():
			d[char] += 1
		else:
			d[char] = 1

	return d

s = input("Input: ")
print(freq(s))

# 2.
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'

def nds(s):
	if len(s) < 2:
		return ""
	return s[:2]+s[-2:]

s = input("Input: ")
print(nds(s))

# 3.
# Write a Python program to get a string from a given string where all occurrences 
# of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def tod(s):
	fc = s[0]
	s = s.replace(fc, "$")
	s = fc + s[1:]
	return s

s = input("Input: ")
print(tod(s))

# 4.
# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

def no4(s1, s2):
	aa = s2[:2] + s1[2:]
	bb = s1[:2] + s2[2:]
	return aa + " " + bb

s1 = input("Input1: ")
s2 = input("Input2: ")
print(no4(s1, s2))

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
# Strip a set of characters from a string.
def stch(s, c):
	return "".join(i for i in s if i not in c)

s = input("Input str.: ")
c = input("Input unallowed chars: ")
print(stch(s,c))

# 15.
# Count repeated characters in a string.
def rep(s):
	d = {}
	for i in s:
		if s.count(i) > 1 and i not in d.keys():
			d[i] = s.count(i)
	for k, v in d.items():
		print(k, v)

s = input("Input: ")
rep(s)

# 16.
# Write a Python program to find the first
# non-repeating character in given string. 
def frnon(s):
	l = list(s)
	for i in l:
		if s.count(i) == 1:
			return "First non-repeating character is: " + i
	return "All chars are repeating"

s = input("Input: ")
print(frnon(s))

# 17.
# Write a Python program to find the
# first repeated character in a given string.
def frrep(s):
	l = list(s)
	for i in l:
		if s.count(i) >= 2:
			return "First repeated character: " + i
	return "There are no repeating characters"

s = input("Input: ")
print(frrep(s))

# 18.
# Write a Python program to compute 
# sum of digits of a given string.
def sumod(s):
	sm = 0
	l = list(s)
	for i in l:
		if i.isdigit():
			sm = sm + int(i)
	return sm

s = "adjjr5nmkkfdjf9ko"
print(sumod(s))

# 19.
# Remove leading zeros from an IP address
def rmvz(s):
	ns = ".".join([str(int(i)) for i in s.split(".")])
	return ns

s = input("Input: ")
print(rmvz(s))

# 20.
# Write a Python program to count
# and display the vowels of a given text.
def vowels(s):
	l = list(s)
	q = 0
	for i in l:
		if i.lower() in "aeiou":
			print(i)
			q +=1
	print("There are " + str(q) + " vowels.")

s = input("Input: ")
vowels(s)