"USES KEY,VALUE PAIRS"

Stanley= {"l_name": "Mwitwari", "Age":19, "Country": "Kenya"}
# print(Stanley["l_name"])

Stanley["Age"]=20
# print(Stanley)

# to remove a key value pair
# Stanley.pop("Age")
# print(Stanley)

# .get method
# print(Stanley.get("Age"))

# print(Stanley.items())

# for i,j in Stanley.items():
#     print(f"The info for Stanley is: {i}:{j}")



# Write a Python program to sum up all the items in a dictionary.
data = {'num1': 10, 'num2': 20, 'num3': 30, 'num4': 40}

total = sum(data.values())

print(total)


# Create a dictionary to store product information (name, price, quantity). Allow users to add, update, and remove items from the inventory.



# Create a dictionary where keys are departments in a company and values are nested dictionaries containing employee information (name, role).
data={"Sales":{"Name": "Stan", "Role":"Head of Dept"}, "Marketing": {"Name":"Jeff", "Role": "Creative desginer"}}
print(data)
