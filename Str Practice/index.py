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