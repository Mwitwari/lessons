# tuples are a sequence of value
# enclosed by()
# if the tuple has only one value always put the comma after it
# you can make sth or declare it as a tuple using inbuilt function tuple
# unlike lists it does not suppurt changing a value i.e not mutable
# but you can replace a tuple with another eg:
names=("Stanley", "Ivy", "Berlin", "David")
print(type(names))
new_names=("Immaculate", )+ (names[0:])
print(new_names)

"comparing tuples"
tuple1=(1,2,3)
tuple2=(0,0,0)
print(tuple1>tuple2)
