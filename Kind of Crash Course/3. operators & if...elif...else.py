"""
Operators
Operators are special symbols in Python that carry out arithmetic or logical computation. 
The value that the operator operates on is called the operand.

For example:
2 + 3 = 5
+   is the operator that perfoms operation
2 and 3 are operands
5 is the output of the operation

Օպերատորներ
Օպերատորները դրանք հատուկ սիմվոլներ են որոնք նախատեսված են թվաբանական և, տրամաբանական
հաշվարկների համար:  Այն արժեքը, որի հետ գործում է օպերատորը կոչվում է operand.

Օրինակ`
2 + 3 = 5
+ -ը դա օպերատորն է, որը կատարում է operand-ների մշակումը
2 և 3-ը operand-ներն, որոնց մշակում է operator-ը
5-ը դա օպերացիայի արդյունքն է
"""


# Arithemetic operators / Թվաբանական օպերատորներ

print(4+2) # 6
print(4-2) # 2
print(4*2) # 8
print(4/2) # 2
print(4**3) # 64 (4*4*4)
print(5%2) # 1 (Modulus: 5 - 2 - 2 = 1)
print(5//2) # 2 (Floor division: 5 - 2 - 2 = 1(5 can only contain two times 2 / 
# 5-ը կարող է պարունակել ընդամենը 2 հատ 2))


# Comparison operators / Համեմատող օպերատորներ

print(4 > 2) # True (Greater than / Մեծ է )
print(4 >= 2) # True (Greater than or equal / Մեծ է կամ հավասար )
print(4 < 2) # False (Less than / Փոքր է )
print(4 <= 2) # False (Less than or equal to / Փոքր է կամ հավասար)
print(4 == 2) # False (Equal to / Հավասար է )
print(4 != 2) # True (Not equal to / Հավասար չէ )


# Logical operators / Տրամաբանական օպերատորներ

# and - True if both the operands True / True եթե երկու operand-ները True-են
# or - True if either of the operands True / True եթե որևէ operand True-է
# no - True if operand is False / True եթե operand-ը False-է
print(True and True) # True
print(False and True) # False
print(True and False) # False
print(False and False) # False

print(True or True) # True
print(True or False) #True
print(False or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True


# Assignment operators / Վերագրման օպերատորներ

x = 5
print(x) # 5

x += 1
print(x) # 6 (x = x + 1)

x = 5
x -= 1
print(x) # 4

x = 5
x *= 2
print(x) # 10 (x = x * 2)

x = 5
x /= 2
print(x) # 2.5

x = 5
x %= 2
print(x) # 1

x = 5
x //= 2
print(x) # 2

x = 4
x **=3
print(x) # 64


# Identity operators / Նույնկանության օպերատորներ

x = True
print(x is True) # True
print(x is not True) # False


# Membership operators / Անդամակցության օպերատորներ

word = "Hi"
print("H" in word) # True
print("B" in word) # False
print("B" not in word) # True