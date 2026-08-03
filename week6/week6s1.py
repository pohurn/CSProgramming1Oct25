##
##INHERITANCE
##

#why?
# Imagine we a Dog and a Cat classes

#without inheritance:

# class Dog:
#     def eat(self):
#         print("Eating...")

#     def sleeps(self):
#         print("Sleeping...")

# class Cat:
#     def eat(self):
#             print("Eating...")

#     def sleeps(self):
#         print("Sleeping...")

#With Inheritance, we fix the above issue

# class GrandMother:
#     def cook(self):
#         print("cooking")

# class Mother(GrandMother):
#     def eat(self):
#         print("Eating...")

#     def sleep(self):
#         print("Sleeping...")

# class Father:
#     def cry(self):
#         print("I can cry")


# class Dog(Mother, Father):
#     def bark(self):
#         print("woof")

# class Horse(Mother, Father,):
#     def Scream(self):
#         print("hiyaaa")

# horse1 = Horse()
# dog1 = Dog()

# horse1.eat()
# horse1.sleep()
# horse1.cry()
# horse1.cook()


# class Animal:
#     def __init__(self, name):
#         self.name = name

# dog1 = Animal("Chase")
# print(dog1.name)

# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age


# dog2 = Dog("Buddy", 3)
# print(dog2.name)



#NOT VERY IMPORTANT FOR NOW BELOW

# class Student:
#     school = "ALU"

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school
#         # print(cls.class_variable)

# # access class method


# Student.change_school("ALCHE")

# print(Student.school)
