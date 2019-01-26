# Python built-in class "Str" which stands for String are used 
# for working with textual data.
# Python strings are "immutable" which means they cannot be 
# changed after they are created. Since strings can't be changed,
# we construct *new* strings as we go to represent computed values. 
# So for example the expression ('hello' + 'there') takes in the 
# 2 strings 'hello' and 'there' and builds a new string 'hellothere'.

# Same to Armenian
# Python-ի ներկառուցված կլաս "Str"-ը որը նույնն է ինչ String, օգտագործվում
# է տեքստային տվյալների հետ աշխատելու համար:
# Python-ի string-երը անփոփոխելի են, ինչը նշանակում է, որ նրանք չեն 
# կարող փոփոխել իրենց արժեքը ստանալուց հետո:
# Օրինակ, մեկ ունենք այսպիսի արտահայտություն ('Բարև' + 'բոլորին')
# Python-ը կվերցնի այդ երկուսը և կստեղծի մի նոր String` "Բարևբոլորին":

# Creating String called s, with value "Hello world":
# Ստեղծենք String, անվանելով այն s, և տալով "Hello world" արժեքը:
s = "Hello world"
# >>>s
# 'Hello world'

# Printing the type of s
# Տպում ենք s-ի տեսակը
# >>> s = "Hello World"
# >>> type(s)
# <class 'str'>

# Printing length of s
# Տպում ենք s-ի երկարություն(Տառերի քանակ + բացատների քանակ)
print(len(s))
# >>>len(s)
# 11

# Printing the first value of s
# Տպում ենք s-ի առաջին սիմվոլը
print(s[0])
# >>> s[0]
# 'H'

# Printing the last values of s
# Տպում ենք s-ի վերջին սիմվոլը
print(s[-1])
# >>> s[-1]
# 'd'

# Printing first 3 characters
# Տպում ենք առաջին 3 սիմվոլները
print(s[0:3])
print(s[:3])
# >>> print(s[0:3])
# Hel
# >>> print(s[:3])
# Hel

# Printing uppercased version of s
# Տպում ենք s-ի մեծատառերով տարբերակը
print(s.upper())
# >>> s.upper()
# 'HELLO WORLD'

# Printing lowercased version of s
# Տպում ենք s-ի փոքրատառերով տարբերակը
print(s.lower())
# >>> s.lower()
# 'hello world'

# Printing titled version of s
# Տպում ենք s-ը ամեն բառի առաջին տառը սարքելով մեծատառ
print(s.title())
# >>> s.title()
# 'Hello World'

# Printing the index where c first time appears in a, if c is not in s
# then it's returning -1
# Տպում ենք այն ինդեքսը, որտեղ առաջին անգամ հանդիպվում է c-ն, s-ի մեջ
# ձախից կարդալուց: Եթե c-ն s-ի մեջ չի հանդիպվում ապա վերադարձվում է -1
c = "H"
print(s.find(c))
# >>> s.find(c)
# 0

# Printing s where a replaced b, if a is not in s then it's just returning s.
# Տպում ենք s-ը, նրա մեջ a-ն, b-ի հետ փոխարինելով: Եթե a-ն չի հանդիպվում
# s-ում ապա նա ուղղակի վերադարձնում է s-ի սկզբնական արժեքը:
a = "H"
b = "W"
print(s.replace(a, b))
# >>> a = "H"
# >>> b = "W"
# >>> s.replace(a,b)
# 'Wello world'


# Printing True if "H" exists in s, else printing False. Same with "a"
# Տպոում ենք True եթե, "H" գտնվում է s-ում, հակառակ դեպքում տպում ենք
# False: Նույնը երկրորդ տողում "a"-հետ:
print("H" in s)
# >>> print("H" in s)
# True

print("a" in s)
# >>> print("a" in s)
# False