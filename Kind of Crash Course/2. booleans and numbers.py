# Booleans

# Variables with type of boolean can contain only to values: True or False.
# Boolean տեսակի փոփոխականները կարող են ընդունել միայն երկու արժեք` True կամ False:
b = True
print(type(b))
# <class 'bool'>

b = False
print(type(b))
# <class 'bool'>


# Numbers

# There are three types of numbers in Python: integers, floats and complex numbers.
# Integers and floats are used for working with 10base numbers.
# Python-ում կան 3 տեսակի թվեր` integers(ամբողջ թվեր), floats(կոտորակով թվեր) և
# complex numbers(համակարգային թվեր): 
# Integer-ները և, float-երը օգտագործվում են 10-ային համակարգով թվերի համար:


# Integers
i = 1
print(type(i))
# <class 'int'>

f = 1.0
print(type(f))
# <class 'float'>

s = ""
print(type(s))
# <class 'str'>

b = True
print(type(b))
# <class 'bool'>


# isinstance(element, type)
# isinstance function is used for checking, either element belongs to a specified 
# type, or not. It returns a boolean(True or False).
# isintstance ֆունկցիան ստուգում է արդյո`ք տարրը պատկանում է նված տեսակին թե ոչ:
# Ծրագիրը որպես պատասան վերադարձնում է boolean(True կամ False):
i = 3
f = 1.0
b = False
s = "Hi"
print(isinstance(i, int)) # True
print(isinstance(i, str)) # False
print(isinstance(f, float)) # True
print(isinstance(b, bool)) # True
print(isinstance(s, str)) # True