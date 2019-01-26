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
