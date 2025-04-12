# opening a file

# file =open("example.txt", "r")
# content= file.read()
# print(content)

# with open("example.txt", "r") as file:
#     print(file.read())

# with open("example2.txt", "w")as file:
#     file.write("i am learning python")

with open("example2.txt", "a")as newfile:
    newfile.write("\ni am appending this file \n can we really add another line?")
