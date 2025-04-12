# lists sequence of values
# characters in a list are called items
# enclosed with[]
list= ["Stan", 2.0, 44, ["Mwitwari", 19]]
# list in a list is a nested list
# [] is an empty list
list_2=["Stan", 34, 34.4]
error=[]
# print(list_2, error)

# lists are mutable(you can change the order of a list or reassign a value in a list)
# names=["Stanley", "Ivy", "Berlin", "David"]
# print(names[0])
# names[1]="Immaculate"
# print(names)

# -1 counts backwards in a list
# print(names[-1])

# in operator also works in lists
# print("Berlin" in names)
# transversing a list
# numbers=[1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)



"LIST OPERATIONS"
"combining 2 lists"
numbers=[1, 2, 3]
other_numbers=[4, 5, 6]
list_3=numbers+other_numbers
# print(list_3)

"the * operator repeats a list"
# print(list_3*2)



"list slicing"
# : is the slice operator
list=[2, 3, 4, 5, 6]
# print(list[0:3])

# print(type(list))



"sorting"
numbers=[2, 6, 1, 5, 8]
# numbers.sort(reverse=True)
# print(numbers)
numbers.remove(1)
# print(numbers)

names=["Stanley", "Victor"]
# names.remove("Victor")
# print(names)

names.extend(["Ivy", "Immaculate", "Joseph", "David"])
# print(names)

names.append("Berlin")
print(names)






