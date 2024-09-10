# Strings
name = "Yogi"
# str
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))


a = "90"
age = 90
print(type(a))
print(type(age))

name = "This is a Big Line "
print(type(name))
name = name + str(1)
print(name)

first_name = "Pramod"
last_name = "Dutta"
full_name = first_name+last_name # CONCAT
print(full_name)


how_many_planes_i_have = None
print(type(how_many_planes_i_have)) # NoneType
# null is not present in Python

val = 0 # This is int

# id
age = 10
age2 = 11
print(id(age)) # 4336051480
print(id(age2)) # 433603232