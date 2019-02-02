"""
Dictionaries
A dictionary is an unordered set of key-value pairs. When you add a key to a dictionary, 
you must also add a value for that key. (You can always change the value later.) 
Python dictionaries are optimized for retrieving the value when you know the key, 
but not the other way around. 

# Example of key, value pair
name: "George"  (name - key, "George" - value)
surname: "Washington" (surname - key, "Washington" - value)

Dictionaries
Dictionary-ն դա առանձ հերթականություն key-value(բանալի - արժեք) զույգերի հավաքածու է:
Dictionary-ին key(բանալի) ավելացնելիս անպայման պետք է ավելացնել արժեք  այդ key-ի համար
(հետագայում այդ արժեքը կարող եք հեշտությամբ փոփոխել:) 
Python-ի dictionary-ները օպտիմալացված են արժեքներ(values) վերադարձնել երբ դուք գիտեք այդ
արժեքի բանալին(key), բայց ոչ այդ նույնը հակառակ կերպ:

# key, value զույգի օրինակ
անուն: "Նիկոլ" (անուն - բանալի(key), "Նիկոլ" - արժեք(value))
ազգանուն: "Փաշինյան" (ազգանուն - բանալի(key), "Փաշինյան" - արժեք(value))
"""

# Creating an empty dictionary / Ստեղծում ենք դատարկ dictionary

d = {}
print(d) # {}
print(type(d)) # <class 'dict'>
print(bool(d)) # False (d equals to False, because there's no any key: value pairs / d-ն հավասարվեց False-ի որ այն չի պարունակում որևէ key: value զույգ:)

# Giving values to a dictionary / Տալիս ենք արժեքներ dictionary-ին
d["name"] = "Rob"
print(d) # {'name': 'Rob'}

# Updating whole dictionary / Թարմացնենք ամբողջ dictionary-ին
d = {"nickname": "Sasunci", "name": "David", "weight": 100, "male": True}
print(d) # {'male': True, 'name': 'David', 'nickname': 'Sasunci', 'weight': 100}
print(d["name"]) # 'David'
print(d["David"]) # KeyError (Բանալու Error)
print(d["male"]) # True

# Editing value / Փոփոխենք արժեքը
print(d["weight"]) # 100
d["weight"] = 90
print(d["weight"]) # 90

# Printing dictionary / Տպում ենք dictionary-ին
d = {0: "Monday", 1: "Tuesday", 2: "Wednesday"}
print(d) # {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday'}

# Printing dictionary using for loop / Տպում ենք dictionary-ին
# օգտագործելով for ցիկլը:
for key, value in d.items():
	print(key, "->", value)

# 0 -> Monday
# 1 -> Tuesday
# 2 -> Wednesday

for key in d.keys():
	print(key)

# 0
# 1
# 2

for value in d.values():
	print(value)

# Monday
# Tuesday
# Wednesday


# Deleting items from dictionary / Ջնջում ենք տարրեր dictionary-ից
d = {0: "Monday", 1: "Tuesday", 2: "Wednesday"}
print(d) # {0: "Monday", 1: "Tuesday", 2: "Wednesday"}
del d[0] 


print(d) # {1: "Tuesday", 2: "Wednesday"}

# Deleting whole dictionary / Ջնջում ենք dictionary-ին ամբողջովին 
print(d) # {1: "Tuesday", 2: "Wednesday"}
del d # NameError: name 'd' is not defined (Անվան Error 'd'-ն հայտարարված չէ)

# Another examples with dictionaries / Այլ dictionary-ների օրինակներ
website = {'URL': "Example.com", 
		   "Users": [0, 1, 2, 3], 
		   "Databases": ["SQl", "MySQl", "Oracle"]}

print(website) # {'URL': 'Example.com', 'Users': [0, 1, 2, 3], 'Databases': ['SQl', 'MySQl', 'Oracle']}

print(website["Databases"]) # ['SQl', 'MySQl', 'Oracle']
for i in website["Databases"]:
	print(i)

# 'SQL'
# 'MySQL'
# 'Oracle'

print(len(website)) # 3

# .get(key)
# .get() method gets the value of key, if key is not dictionary it's not giving an error.
# .get() մեթոդը վերցնում է key-ը, և վերադարձնում է արժեքը: Եթե key-ը չի գտնվում dictionary-ում,
# այն Error չի տալիս, այն ուղղակի ոչինչ չի անում(դա նրա առավելությունն է:)
# Example / Օրինակ
colors = {0: "Red", 1: "Green", 2: "Blue"}
print(colors[4]) # KeyError
print(colors.get(4)) # 

# .clear()
# Remove all items form the dictionary.
# Ջնջում է dictionary-ի բոլոր էլեմենտները:
d = {0: "Red", 1: "Green", 2: "Blue"}
print(d) # {0: "Red", 1: "Green", 2: "Blue"}
d.clear()
print(d) # {}

# .pop(key[,d]) 
# Remove the item with key and return its value or d if key is not found. 
# If d is not provided and key is not found, raises KeyError.
# Ջնջում, և վերադարձնում է key-ին համապատասխան արժեքը, եթե key-ը
# չի գտնվում dictionary-ում, և d-n տրված է ապա այն վերադարձնում է d-ն:
# Եթե key-ը չի գտնվում dictionary-ում, և d-ն տրված չէ, այն կվերադարձնի
# KeyError:

# Example / Օրինակ
d = {0: "Red", 1: "Green", 2: "Blue"}
b = d.pop(2)
print("b =", b) # b = Blue
print("d =", d) # d = {0: 'Red', 1: 'Green'}

b = d.pop(2, "Blue is not here!")
print("b =", b) # b = 'Blue is not here!'
print("d =", d) # d = {0: 'Red', 1: 'Green'}

b = d.pop(2) # KeyError: 2

































