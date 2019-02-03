"""
Sets
A set is an unordered “bag” of unique values. A single set can contain values of any immutable datatype. 
Once you have two sets, you can do standard set operations like union, intersection, and set difference. 

Values of sets are inside of curly braces, and are separating from each other with commas.

Set-եր
Set-ը դա չդասավորված արժեքների պարկ է: Set-ը կարող է պարունակել ցանկացած immutable(չփոփոխվող)
արժեք: Ունենալով երկու set-եր դուք կարող եք կատարել set-ի հիմնական գործողությունները, օրինակ`
union - երկուսի տարրերը միասին,
intersection - երկուսի համար ընդհանուր տարրեր (հատում)
diiference - տարրեր որոնք կան միայն մեկի մոտ
symmetric difference - տարրեր որոնք չունեն իրենց կրկնօրինակից մյուսը set-ում, և հակառակը
(union-ի, intersection-ի....մասին կա ավելի պարզ նկարագրող նկար(https://bit.ly/2S7Sk2K))

Set-երի արժեքները գտնվում են ձևավոր փակագծերի միջև({}), և առանձնանում են միմյանցից ստորակետով:
"""

# Creating a set / Ստեղծում ենք set
s = {"Hi", 1, 3}

print(s) # {1, 3, 'Hi'}
print(type(s)) # <class 'set'>


# Creating an empty set / Ստեղծում ենք դատարկ set
s = set()
print(type(s)) # <class 'set'>

# If you write / Եթե դուք գրեք
s = {}
# It will create an empty dictionary / Կստեղծվի դատարկ dictionary
print(type(s)) # <class 'dict'>

# Creating set with values of the list / Ստեղծում ենք set list-ի արժեքներով
l = ["True", True, 45, "f"]
s = set(l)
print(s) # {True, 45, 'True', 'f'}

# Sets are removing dublicates / Set-երը ջնջում են կրկնօրինակները
s = {1, 2, 1, 2, 1, 2}
print(s) # {1, 2}

# Adding values to a set / Ավելացնում ենք արժեքներ set-ին
s = {1, 2}
s.add("Hola")
s.add(3)
print(s) # {1, 2, 3, 'Hola'}
s.add(3)
print(s) #{1, 2, 3, 'Hola'} (no duplicates)

# Removing values from a set / Հեռացնում ենք set-ի արժեքներից
print(s) # {1, 2, 3, 'Hola'}
s.remove(1)
print(s) # {2, 3, 'Hola'}
s.remove(1) # KeyError: 1
s.discard(2) 
print(s) # {3, 'Hola'}
s.discard(2) # (Not doing anything / Ոչինչ չի անում)

# Removing and returning values from a set / Ջնջում և վերադարձնում ենք արժեքներ
s = {1, 2, 3}
s.pop() # 1
print(s) {2, 3}

# Removing all values from a set / Հեռացնում ենք set-ի բոլոր արժեքները
s = {"հի", True, False}
s.clear()
print(s) # set()

# Iterating through a set
s = {1, 2, 3, 4, 5}
for i in s:
	print(i)

# 1
# 2
# 3
# 4
# 5

# Transforming Set into Ordered Values / Կերպարանափոխում ենք set-ը դասավորված արժեքների
s = {1, 2, 3, 4, 5}
print(s) # {2, 4, 5, 3, 1}
print(type(sorted(s))) # <class 'list'>


# ********* Union / Միություն, 2-ը միասին ***********
dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

# set built-in function union / set-ի ներկառուցված union ֆունկցիա
print(dataScientist.union(dataEngineer)) # {'Tableau', 'R', 'Java', 'Hadoop', 'Scala', 'Python', 'SAS', 'Git', 'SQL'}

# Equivalent Result / Համարժեք արդյունք
print(dataScientist | dataEngineer) # {'Tableau', 'R', 'Java', 'Hadoop', 'Scala', 'Python', 'SAS', 'Git', 'SQL'}
# *********************************************

# ********* intersection / հատում *********
# Intersection operation
print(dataScientist.intersection(dataEngineer)) # {'Git', 'SQL', 'Python'}

# Equivalent Result / Համարժեք արդյունք
print(dataScientist & dataEngineer) # {'Git', 'SQL', 'Python'}
# *********************************************

#********* Difference / Տարբերություն *********
# Difference Operation
print(dataScientist.difference(dataEngineer)) # {'Tableau', 'R', 'SAS'}

# Equivalent Result / Համարժեք արդյունք
print(dataScientist - dataEngineer) # {'Tableau', 'R', 'SAS'}
# *********************************************

# ********* Symmetric Difference / Սիմետրիկ Տարբերություն *********
# Symmetric Difference Operation
print(dataScientist.symmetric_difference(dataEngineer)) # {'Tableau', 'R', 'Java', 'Scala', 'Hadoop', 'SAS'}

# Equivalent Result / Համարժեք արդյունք
print(dataScientist ^ dataEngineer) # {'Tableau', 'R', 'Java', 'Scala', 'Hadoop', 'SAS'}
# **********************************************


# Membership Tests / Առկայության ստուգում
# Initialize a set / Ստեղծենք set
possibleSet = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS', 'Java', 'Spark', 'Scala'}

# Membership test
print('Python' in possibleSet) # True

# Subset / Ենթաբազմություն
possibleSkills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R'}

# If every value of the set mySkills is also a value of the set possibleSkills, then mySkills
# is said to be a subset of possibleSkills, mathematically written mySkills ⊆ possibleSkills.
# Եթե mySkills-ի ամեն մի արժեք նաև possibleSkills-ի արժեքներից է, ապա mySkills-ը possibleSkills-ի
# ենթաբազմությունն է, մաթեմատիկորեն գրված mySkills ⊆ possibleSkills:
print(mySkills.issubset(possibleSkills)) # True