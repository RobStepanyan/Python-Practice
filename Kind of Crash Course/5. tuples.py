"""
# English version
Tuples

Tuples are ordered, immutable sequences of values. 
A tuple can not be changed in any way once it is created. 
In Python tuples are written with round brackets.

1. A tuple is defined in the same way as a list, except that the whole set of elements
is enclosed in parentheses instead of square brackets.
2. The elements of a tuple have a defined order, just like a list. Tuple indices are 
zero-based, just like a list, so the first element of a non-empty tuple is always a_tuple[0].
3. Negative indices count from the end of the tuple, just like a list.
4. Slicing works too, just like a list. When you slice a list, you get a new list; when you 
slice a tuple, you get a new tuple.

>>> a_tuple = ("a", "b", "mpilgrim", "z", "example")  1
>>> a_tuple
('a', 'b', 'mpilgrim', 'z', 'example')
>>> a_tuple[0]                                        2
'a'
>>> a_tuple[-1]                                       3
'example'
>>> a_tuple[1:3]                                      4
('b', 'mpilgrim')


The major difference between tuples and lists is that tuples can not be changed. In technical 
terms, tuples are immutable. In practical terms, they have no methods that would allow you to 
change them. Lists have methods like append(), extend(), insert(), remove(), and pop(). 
Tuples have none of these methods. You can slice a tuple (because that creates a new tuple), 
and you can check whether a tuple contains a particular value (because that doesn’t change 
the tuple), and… that’s about it. 

1.	You can’t add elements to a tuple. Tuples have no append() or extend() method.
2.	You can’t remove elements from a tuple. Tuples have no remove() or pop() method.
3.	You can find elements in a tuple, since this doesn’t change the tuple.
4.	You can also use the in operator to check if an element exists in the tuple. 

# continued from the previous example
>>> a_tuple
('a', 'b', 'mpilgrim', 'z', 'example')

>>> a_tuple.append("new")               1
Traceback (innermost last):
  File "<interactive input>", line 1, in ?
AttributeError: 'tuple' object has no attribute 'append'

>>> a_tuple.remove("z")                 2
Traceback (innermost last):
  File "<interactive input>", line 1, in ?
AttributeError: 'tuple' object has no attribute 'remove'

>>> a_tuple.index("example")            3
4

>>> "z" in a_tuple                      4
True


So what are tuples good for?

    Tuples are faster than lists. If you’re defining a constant set of 
    values and all you’re ever going to do with it is iterate through it, 
    use a tuple instead of a list.
    
    It makes your code safer if you “write-protect” data that doesn’t need
    to be changed. Using a tuple instead of a list is like having an implied 
    assert statement that shows this data is constant, and that special thought 
    (and a specific function) is required to override that.
    
    Some tuples can be used as dictionary keys (specifically, tuples that contain 
    immutable values like strings, numbers, and other tuples). Lists can never be 
    used as dictionary keys, because lists are not immutable. 

Tuples can be converted into lists, and vice-versa. The built-in tuple() function 
takes a list and returns a tuple with the same elements, and the list() function 
takes a tuple and returns a list. In effect, tuple() freezes a list, 
and list() thaws a tuple. 

1.	In a boolean context, an empty tuple is false.
2.	Any tuple with at least one item is true.
3.	Any tuple with at least one item is true. The value of the items is irrelevant. 
But what’s that comma doing there?
4.	To create a tuple of one item, you need a comma after the value. Without the comma, 
Python just assumes you have an extra pair of parentheses, which is harmless, but it 
doesn’t create a tuple. 

>>> is_it_true(())             1
no, it's false

>>> is_it_true(('a', 'b'))     2
yes, it's true

>>> is_it_true((False,))       3
yes, it's true

>>> type((False))              4
<class 'bool'>

>>> type((False,))
<class 'tuple'>


>>> v = ('a', 2, True)
>>> (x, y, z) = v       1

>>> x
'a'
>>> y
2
>>> z
True

1	v is a tuple of three elements, and (x, y, z) is a tuple of three variables. 
Assigning one to the other assigns each of the values of v to each of the variables, 
in order. 

>>> (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(1,8)  ①
>>> MONDAY                                                                       ②
1
>>> TUESDAY
2
>>> SUNDAY
7


# ********************* Armenian version *************************
Tuples

Tuple-ը կարգավոր(հերթականությունը պահպանող), անփոփող(immutable) արժեքների հաջորդականություն է: 
Tuple-ի պարունակությունը հնարավոր չէ փոփոխել այն ստեղծելուց հետո:
Python-ում tuple-ների արժեքները գրվում են փակագծերի մեջ.

1. Tuple-ը հայտարարվում է list-ի նման, քառակուսի փակագծերի տեղը օգտագործելով սովորական փակագիծ:
2. Tuple-ի արժեքները list-երի նման ունեն հաստատուն հաջորդականություն: Tuple-ի ինդեքսները սկսվում են
0-ից, նույնպես list-երի նման, այպիսով եթե վերցնենք ոչ դատարկ tuple, a_tuple անվամբ ապա նրա առաջին
արժեքը տպելու համար ուղղակի կգրենք print(a_tuple[0]):
3. Բացասական ինդեքսները հաշվվում են վերջից, list-երի նման:
4. Slicing-ը(կտրատելը([start:end:step])) աշխաում է նույնպես, list-երի նման: Երբ դու slice-ես անում list-y, 
դու ստանում ես նոր list` tuple-ի դեպքում նոր tuple: 

Օրինակներ`
>>> a_tuple = ("a", "b", "mpilgrim", "z", "example")  1

>>> a_tuple
('a', 'b', 'mpilgrim', 'z', 'example')

>>> a_tuple[0]                                        2
'a'

>>> a_tuple[-1]                                       3
'example'

>>> a_tuple[1:3]                                      4
('b', 'mpilgrim')


Ամենամեծ տարբերությունը tuple-ի ու list-ի միջև դա այն է որ tuple-ի արժեքները անփոփոխ են: 
Տեխնիկալ տերմիններով ասած imutablե: Պրակտիկալ ասած, նրանք չունեն այնպիսի մեթոդներ, որոնք
մեզ կոգնեն փոփոխել tuple-ի արժեքները: Օրինակ list-երը ունեն մեթոդներ ինչպիսիք են append(), 
extend(), insert(), remove(), and pop(). Tuple-ները չունեն այս մեթոդները: Դուք կարող եք slice 
անել tuple-ը, որովհետև այն ստեղծում է նոր tuple, և դուք կարող եք ստուգել արդյոք այն պարունակում
է որոշակի տարր, որովհետև այդպիսով դուք չեք փոփոխում tuple-ի պարունակությունը, և այդպես շարունակ:

1.	Դուք չեք կարող ավելացնել արժեքներ tuple-ին: Tuple-ները չունեն append() կամ extend() մեթոդները:
2.	Դուք չեք կարող ջնջել արժեքներ tuple-ից: Tuple-ները չունեն remove() կամ pop() մեթոդները:
3.	Դուք կարող եք փնտրել արժեքներ tuple-ում քանի որ այդպես դուք չեք փոփոխում tuple-ը:
4.	Դուք կարող եք ստուգել արդյոք որևէ արժեք գտնվում է նրա մեջ օգտագործելով "in" օպերատորը:

# Շարունակելով անցյալ օրինակից:
>>> a_tuple
('a', 'b', 'mpilgrim', 'z', 'example')

>>> a_tuple.append("new")               1
Traceback (innermost last):
  File "<interactive input>", line 1, in ?
AttributeError: 'tuple' object has no attribute 'append'

>>> a_tuple.remove("z")                 2
Traceback (innermost last):
  File "<interactive input>", line 1, in ?
AttributeError: 'tuple' object has no attribute 'remove'

>>> a_tuple.index("example")            3
4

>>> "z" in a_tuple                      4
True


Այսպիսով ո՞րն է tuple-ի առավելությունը:

    Tuple-ները ավելի արագ են քան list-երը. Եթե դուք հայտարարում եք հաստատուն
    արժեքների հավաքածու, և դուք այն օգտագործելու եք միայն iterate(using loops) 
    լինելու համար, ապա list-ի փոխարեն օգտագործեք tuple:
    
    Այպես դուք ձեր կոդը կլինի ավելի ապահով, քանի որ արժեքները, որոնք պետք չէ
	փոփոխել կմնան անփոփոխ: Tuple-ի օգտագործումը list-ի փոխարեն, ենթադրում է
	հաստատուն արտահայտություն, որը ցույց է տալիս, որ տվյալները հաստատուն են: 
    

Tuple-ները կարող են փոխակերպվել list-երի, և հակառակը: Ներկառւոցված tuple() ֆունկցիան
վերցնում է list-ը, և վերդարձնում tuple պահպանելով արժեքները, և list(), որը վերցնում է 
tuple-ը և վերադարձնում list: Ասյպես ասած tuple()-ը "սառեցնում է" list-ը, 
և list()-ը հալեցնում է tuple-ը: 

1.	Որպես boolean դիտարկելիս, դատարկ tuple-ը False-է:
2.	Ցանկացած tuple գոնե մեկ արժեքով True-է:
3.	Ցանկացած tuple գոնե մեկ արժեքով True-է, և կապ չունի թե այդ մեկը ինչ արժեք ունի,
բայց ի՞նչ է անում այս ստորակետը այստեղ:
4.	Մեկ արժեքով tuple ստեղծելու համար պետք է արժեքից հետո դնել ստորակետ: Առանձ 
ստորակետ Python-ը ենթադրում է, որ դուք ուղղակի դրել եք ավելորդ փակագծեր, և որ դրանք
անվտանգ են, և այդպիսով tuple չի ստեղծվում:
 

>>> is_it_true(())             1
no, it's false

>>> is_it_true(('a', 'b'))     2
yes, it's true

>>> is_it_true((False,))       3
yes, it's true

>>> type((False))              4
<class 'bool'>

>>> type((False,))
<class 'tuple'>


>>> v = ('a', 2, True)
>>> (x, y, z) = v       1

>>> x
'a'
>>> y
2
>>> z
True

1.	v-ն tuple է, որն ունի 3 արժեք, և (x, y, z) նույնպես tuple է որը պարունակում է 3
փոփոխական: Վերագրելով մեկ tuple-ը մյուսին` ամեն մի փոփոխական հերթականությամբ
վերցնում է v-ից իրեն համապատասխան արժեքը:
 
# Նմանատիպ ևս մեկ օրինակ:

>>> (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(1,8)  ①
>>> MONDAY                                                                       ②
1
>>> TUESDAY
2
>>> SUNDAY
7