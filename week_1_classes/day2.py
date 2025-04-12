"""
OPERATORS IN PYTHON

i)Arithmetic operators
"""

# a= 5
# b= 2
"addition"
# print(a + b)

"subtraction"
# print(a - b)

"multiplication"
# print(a * b)

"division"
# print(a/b)

"Raising to a certain power"
# print(a**b)

"Modulus(getting the remainder)"
# print(a % b)

"floor division(whole number rounded down)"
# print(a//b)

"ii) COMPARISON OPERATORS"
# x= 5
# y= 7

"equal to (==)"
# print(x==y)

"not equal to !="
# print(x != y)

"greater and less than"
# print(x > y)
# print(x < y)
# print(x <= y)


"iii) LOGICAL OPERATORS (and, or, not)"
# x= 10
# y= 20

# # and (both conditions met)
# print(x < y and y > 2)

# # or (one condition met)
# print(x > y or y > 5)

# # not
# print(not(x<y))


"ASSIGNMENT (COMPOUND ASSIGNMENT)"
# a= 5
# print(a)
# a= 5 + 3=8 you can do: or any arithmetic calculation 

# a *=3
# print(a)


"iv)MEMBERSHIP OPERATOR (in, not in)"
'LISTS []'

# fruits=['Watermelon', 'mango', 'orange']
# print(fruits)

# print('mango' not in fruits)
# print('Watermelon' in fruits)


"CONDITIONS IN PYTHON"

# x= int(input("Enter a number:"))
# if x == 1:
#     print("Number 1")
# elif x == 2:
#     print("Number 2")
# elif x == 3:
#     print("Number 3")
# else:
#     print("Invalid entry")

"nested condiotions"

# score= int(input("Enter your score:"))
# if score >=50:
#     print("Above Average")
#     if score>=80:
#         print("Excellent")
#     else:
#         print("Great but not excellent")
# else:
#     print("You have failed")


"Combining logical operators with nested conditional statements"

age= int(input("Enter your age:"))
income= int(input("Enter your income:"))
if age>=18 and income >=120000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")










