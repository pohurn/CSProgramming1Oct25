# import page2


# answer = page2.add(5,2)
# print(answer)
# print(page2.add(5,2))

# print(page2.subtract(8,10))


#PYTHON CLASSES
# - everything in python is treated as an object
# - objects have :
#  1. properties (data)
# 2. methods (things that they can do)

# e.g: - PHONE:
# Properties of the phone
# Brand = Samsung
# Camera = 100mp
# Color = Red

#things that the phone can do: (methods)
# - Call()
# - Text()
# - TakePhoto()


# A python object works exactly the same way


# A class is like a blueprint
# e.g building a house

# blueprint -> Drawing of the house (it just describes no of rooms etc...)

# class Student:
#     pass

#pass => when you currently don't have anythong to put inside the class
# why we need this? => because python expects something inside the class


# class Student:
# #whenever an object is created, python automatically runs: __init__()
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # self.num = age
#         # self.address = name


# # Student => the blueprint
# # student1 => the actual object created from the blueprint
# student1 = Student("Modupe", 20)
# student2 = Student("Marcel", 17)

# print(student1.name)


# SELF => it means this object
# imagine student1, student2, student3 => they have their own data
# when python creates student1, self becomes student1


class Student:
    def __init__(self, name):
        self.username = name
        self.age = 20
        self.address = "slkmlds"

    def introduce(self):
        print("Hello, my name is", self.username)

student1 = Student("Navin")
student2 = Student("Titilayo")

# student1.introduce()
student2.introduce()

