import sqlite3

# Connecting to a database(creating)

students=sqlite3.connect("Students.db")
print(students)

# Cursor object
cursor= students.cursor()

# create table

# cursor.execute("""
# create table wanafunzi(
#                name TEXT,
#                gender TEXT,
#                age INTEGER)""")

# printing that out

cursor.execute("select * from wanafunzi")

# populating the table

cursor.execute("""
               insert into wanafunzi(name, gender, age) values ("Stan", "male", 19)""")

# wanafunzi.commit()
cursor.execute("select * from wanafunzi")
rows= cursor.fetchall()

for row in rows:
    print(row)