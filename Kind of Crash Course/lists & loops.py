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

# Creating an empty list
# Ստեղծենք դատարկ list
l = []
# >>> l = []
# >>> l
# []

# Creating a list with values
# Ստեղծենք list, որը ունի արժեքներ
colors = ['red', 'green', 'blue']
# >>> colors = ['red', 'green', 'blue']
# >>> colors
# ['red', 'green', 'blue']

# Printing values of a list using indexes
# Տպում ենք list-ի արժեքները օգտագործելով 
# ինդեքսները
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

# Deleting list named l
# Ջնջում ենք l անունով list-ը
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
# It's opposite to max()
# max()-ի հակառակը

# len()
# The length of a list
# list-ի տարրերի քանակը
l = [6]
print(len(l)) # 1

l = []
print(len(l)) # 0

# sum()
# Summary of elements, if elements are numbers
# Տարրերի գումարը, եթե տարրերը թվեր են
l = [1, 1.2]
print(sum(l)) # 2.2

l = ["Hi", "A", "C", "B"]
print(sorted(l)) # ['A', 'B', 'C', 'Hi']
print(sorted(l, reverse= True)) # ['Hi', 'C', 'B', 'A']


# List Methods
# List-ի մեթոդները

# .append(element)
# Adding an item to the end of list
# Ավելացնում է տարր list-ի վերջում
l = [1, 2]
l.append(3)
print(l) # [1, 2, 3]

# .instert(index, element)
# Inserting an item to the given index, shifting elements to the right
# Մութքագրում է տարր նշված ինդեքսում, տեղափոելով այլ տարրերը դեպի աջ
l = [1, 2]
l.insert(0, 3)
print(l) # [3, 1, 2]

# .extend(list2)
# Adds an elements of list2 to a list
# Ավելացնում է list2-ի տարրերը list-ին
l = [1, 2]
l2 = [3, 4, 5]
l.extend(l2)
print(l) # [1, 2, 3, 4, 5]

# 
