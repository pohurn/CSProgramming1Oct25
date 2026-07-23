
# A dictionary stores data as key-value pairs
# Word -> Meaning
# A key has to be unique

# "Apple" -> "A fruit"

# "Apple" -> "A fruit"

#student information

# student = {
#     "name" : "Allan", # "text"
#     "age" : 20, # int/ number
#     "course" : "Software Engineering" # string / text
# }

# student.name => Allan
# student.age => 20
# student.course => sftware eng

# print(student)

# student["age"] => trying to access the value for this specific key

#first way to get value

# print(student["name"])
# print(student["age"])
# print(student["course"])

# second way using .get() ; which is the proper way (it is safer)

# print(student.get("course"))

# print(student.get("Allan"))
# print("I am still working!")


# Human = {
#     "name" : "Anita"
# }
# #to add new key - value

# Human["age"] = 20
# print(Human)

# # to change value of 1 key
# Human["name"] = "Titilayo"

# print(Human)

#looping through a dictionary

student = {
    "name" : "Allan", # "text"
    "age" : 20, # int/ number
    "course" : "Software Engineering" # string / text
}

# for key in student:
#     print(key)

#if you want to print values, you need to use .values()
# for value in student.values():
#     print(value)


# for key, value in student.items():
#     print(key, ":", value)


# student = {
#     "name" : "Allan", # "text"
#     "age" : 20, # int/ number
#     "course" : "Software Engineering" # string / text
# }

# if "age" in student:
#     print("key Age exists!")
# else:
#     print("Does not exist")


#how to remove?
# Human = {
#     "name" : "Anita",
#     "age" : 21,
#     "address" : "pamplemousses"
# }

# Human.pop("name") # remove specific

# Human.popitem() # removes last key value pair

# Human.clear() # removes everything from the dictionary

# print(Human)


# How we copy?
Human = {
    "name" : "Anita",
    "age" : 21,
    "address" : "pamplemousses"
}

#original still affects copy this way

# CopyOfHuman = Human
# Human.pop("age")
# print(CopyOfHuman)


#original does not affect copy this way
# CopyOfHuman = Human.copy()
# Human.pop("age")
# print(CopyOfHuman)


#MODULES
import math
import random
import numpy

# print(math.sqrt(25))

# print(random.randint(1,10))

