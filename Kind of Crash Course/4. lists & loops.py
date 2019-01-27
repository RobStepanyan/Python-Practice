"""
Python Lists

Python has a great built-in list type named "list". 
List literals are written within square brackets [ ]. 
Lists work similarly to strings -- use the len() function
and square brackets [ ] to access data, with the first 
element at index 0.

Python-ի list-եր
Python-ը ունի մի հոյակապ ներկառուցված ցուցակի տեսակ, որը
կոչվում է "list": list-ի էլեմենտները կամ նույնն է ինչ 
տարրերը գտնվում են քառակուսի փակագծերի միջև([]):
List-երը աշխատում են string-երի նման, այսինքն դուք 
կարող եք օգտագործել len() ֆունկցիան list-ի երկարությունը
գտնելու համար(տարրերի քանակը), և քառակուսի փակագծերը ([])
տարրերին "հասնելու" համար, 0 ինդեքսով առաջին տարրով: 

"""

# Creating an empty list․
# Ստեղծենք դատարկ list։
l = []
# >>> l = []
# >>> l
# []

# Creating a list with values․
# Ստեղծենք list, որը ունի արժեքներ։
colors = ['red', 'green', 'blue']
# >>> colors = ['red', 'green', 'blue']
# >>> colors
# ['red', 'green', 'blue']

# Printing values of a list using indexes․
# Տպում ենք list-ի արժեքները օգտագործելով 
# ինդեքսները։
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[-1])
# >>> colors[0]
# 'red'
# >>> colors[1]
# 'green'
# >>> colors[2]
# 'blue'
# >>> colors[-1]
# 'blue'

# Deleting list named l․
# Ջնջում ենք l անունով list-ը։
l = [1, "Bye"]
print(l) # [1, "Bye"]

del l
print(l) # NameError: name 'l' is not defined (անվան Error, 'l'-ը հայտարարված չէ)


# Assignment with an "="" on lists does not make a copy. 
# Instead, assignment makes the two variables point to the one list in memory. 
# Հավասարեցումը փոփոխականին "=" նշանով list-ին չի ստեղծում նոր
# list նույն արժեքներով, այլ ստեղծում է երկու փոփոխական ուղղորդված
# հիշողության նուն կետին: Օրինակ`
l = [1, 2, "Hi", "4", 5] 
print(l) # [1, 2, "Hi", "4", 5]

b = l 
print(b) # [1, 2, "Hi", "4", 5]

del l[-1] 
print(l) # [1, 2, "Hi", "4"]
print(b) # [1, 2, "Hi", "4"]



# List built-in functions
# List-ի ներկառուցված ֆունկցիաները

# Max()
l = [1, 2, 3, 4]
print(max(l)) # 4

l = ["Hi", "There"]
print(max(l)) # There

l = [True, False]
print(max(l)) # True

# Min()
# It's opposite to max()․
# max()-ի հակառակը։

# len()
# The length of a list․
# list-ի տարրերի քանակը։
l = [6]
print(len(l)) # 1

l = []
print(len(l)) # 0

# sum()
# Summary of elements, if elements are numbers․
# Տարրերի գումարը, եթե տարրերը թվեր են։
l = [1, 1.2]
print(sum(l)) # 2.2

l = ["Hi", "A", "C", "B"]
print(sorted(l)) # ['A', 'B', 'C', 'Hi']
print(sorted(l, reverse= True)) # ['Hi', 'C', 'B', 'A']


# List Methods
# List-ի մեթոդները

# .append(element)
# Adding an item to the end of list․
# Ավելացնում է տարր list-ի վերջում։
l = [1, 2]
l.append(3)
print(l) # [1, 2, 3]

# .instert(index, element)
# Inserting an item to the given index, shifting elements to the right․
# Մութքագրում է տարր նշված ինդեքսում, տեղափոելով այլ տարրերը դեպի աջ։
l = [1, 2]
l.insert(0, 3)
print(l) # [3, 1, 2]

# .extend(list2)
# Adds an elements of list2 to a list․
# Ավելացնում է list2-ի տարրերը list-ին։
l = [1, 2]
l2 = [3, 4, 5]
l.extend(l2)
print(l) # [1, 2, 3, 4, 5]

# .index(element)
# Returnng an index of a first instance of the given element, throws a
# ValueError if the element does not appear. Use "in" to check existence.
# Վերադարձնում է տարրի առաջին նմուշի ինդեքսը, եթե այդպիսի տարր առկա չէ list-ում
# ապա ծրագիրը կտա ValueError(արժեքի խնդիր)։
l = [5, 6, 9, 6, 8]
print(l.index(6)) # 1
print(l.index(1)) # ValueError

# .remove(element)
# Searches for the first instance of the given element and removes it 
# (throws ValueError if not present)․
# Ջնջում է տրված տարրի առաջին նմուշը, եթե այդպիսի տարր առկա չէ list-ում
# ապա ծրագիրը կտա ValueError(արժեքի խնդիր)։
l = ["Hi", "I'm", "Michael", "Jordan", "Lewis"]
l.remove("Lewis")
print(l) # ['Hi', "I'm", 'Michael', 'Jordan']

# .sort()
# Sorts the list.
# Դասավորում է list-ը։
l = [5, 3, 1, 4, 2]
l.sort()
print(l) # [1, 2, 3, 4, 5]

# .reverse()
# Reverses the list.
# Շրջում է list-ը։
l = [5, 4, 3, 2, 1]
l.reverse()
print(l) # [1, 2, 3, 4, 5]

# .pop(index)
# Removes and returns the element at the given index. 
# Returns the rightmost element if index is omitted.
# Ջնջում և վերադարձնում է տրված ինդեքսում գտնվող տարրը։
# Եթե տարրը նշված չէ ապա ջնջում և վերադարձնում է ամենաաջի
# տարրը։
l = ["gf", True, 1, 2.2, 3.00, False, "Bye", 1, 3]
l.pop(1) # True
print(l) # ['gf', 1, 2.2, 3.0, False, 'Bye', 1, 3]
l.pop() # 3
print(l) # ['gf', 1, 2.2, 3.0, False, 'Bye', 1]



"""
Loops

Ցիկլեր
"""

# 'For' loop
# 'For' Ցիկլ

# For is used for giving different values to a single variable in one line of code.
# Values can be numbers in spcified range, items of lists, sets, tuples,
# dictionaries, etc. That datatypes are called "iterables", and the variable which
takes all that data called "iterator".

# For-ը օգտագործվում է մեկ փոփոխականին տարբեր արժեքներ տալու համար, որը տեղի
# կունենա ընդամենը մեկ տողում: Արժեքները կարող են լինել` թվեր մեր ընտրած միջակայքում,
# list-ի, set-ի, tuple-ի, dictionary-ի և այլ նման տեսակների տարրեր: 
# 
Այդպիսի տվյալները կոչում են "iterables", իսկ փոփոխականին, որը ստանում է այդ 
# արժեքները "iterator":

# This is how for looks like.
# Այսպիսի տեսք ունի for -ը:

# for iterator in iterable:
	# action / գործողություն

# For example
# Օրինակ
l = [1, 2, 3, 4]
for i in l:
	print("i =", i)
# i = 1
# i = 2
# i = 3
# i = 4

# range(start = 0, finish(not inclusive), step = 1)
# If starting number is not specified then it will take default value: 0,
# if step is not specified then it will take default value: 1

# range(սկիզբ = 0, վերջ (ոչ ներառյալ), քայլ = 1)
# Եթե միջակայքի սկզբնակետը նշված չէ, ապա այն վերցնում է 0 արժեքը,
# եթե քայլը նշված չէ ապա այն վերցնում է 1 արժեքը:

for i in range(5):
	print(i)

# 0
# 1
# 2
# 3
# 4

for i in range(1, 5, 2):
	print("I =", i)

# 1
# 3


# Demonstartion of advantage of using for loop.
# for ցիկլի օգտագործման առավելության ցուցադրում:

# Print the square of numbers between 1 to n.
# Տպել մինև n գտնվող թվերի քառակուսիների գումարը:

n = 10
# Without for loop/ Առանձ for-ի
print(1 * 1)
print(2 * 2)
print(3 * 3)
print(4 * 4)
print(5 * 5)
print(6 * 6)
print(7 * 7)
print(8 * 8)
print(9 * 9)
print(10 * 10)

# Using for / Օգտագործելով for -ը
for i in range(1, n+1):
	print(i*i) 


"""
While loop

While Ցիկլ
"""

# The while loop in Python is used to iterate over a block of code as long as 
# the test expression (condition) is true.
# We generally use this loop when we don't know beforehand, the number of times to iterate.
# while ցիկլը օգտագործվում է կոդի բլոկը կրկնելու համար այնքան ժամանակ քանի
# դեռ պայամանը(condition)-ը հավասար է True արժեքի:
# Հիմնականում այս ցիկլը օգտագործվում է այն ժամանակ, երբ մենք չգիտենք թե քանի անգամ
# է մեր գործողությունը կատարվելու:

# This is how while looks like.
# Ահա թե ինչ տեսք ունի while ցիկլը:
# while (condition):
	# action / գործողություն
	# step / քայլ (պարտադիր)
# For example / Օրինակ
l = [1, 2, 3, 4, 5, 6]
i = 0
while l[i] < 5:
	print(l[i])
	i += 1 # i = i + 1 

# If the step is not specified in code block of loop, then it will become an
# endless loop. To stop it use "ctrl+c" or "ctrl+ alt+ pause / break".
# Եթե քայլը նված չէ ցիկլի կոդի բլոկում, ապա ցիկլը կվերածվի անվերջ ցիկլի:
# Այդ անվերջ ցիկլը կանգնեցնելու համար օգտագործեք "ctrl+c" կամ "ctrl+ alt+ pause / break":

# break & continue
# break statement is used for stoping a loop, continue is used to give next value to 
# iterable
# break-ը օգտագործվում է ցիկլը կանգնեցնելու համար, իսկ continue-ն փոփոխականին 
# հաջորդ արժեքը տալու համար

# break

for i in range(5):
	if i == 3:
		print("Gta 3-y")
		continue
	print(i)
# 0
# 1
# 2
# Gta 3-y
# 4

for i in range(5)
	if i == 3:
		print("Gta 3-y")
		break
	print(i)

# 0
# 1
# 2
# Gta 3-y

# break and continue are working with the while loop similarly.
# break-ը և continue-ն աշխատում են նույն կերպով նաև while ցիկլի հետ: