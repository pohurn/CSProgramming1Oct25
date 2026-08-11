
# OBJECT ORIENTED PROGRAMMING

#1. Inheritance - ok
#2. Polymorphism - ok
#3. Encapsulation - ok
#4. Abstraction - 

# polymorphism => one thing can take many forms

# If you break it into 2 => poly ; morphism
# poly => many
# morph => forms

# in python - > e.g: a method can perform different actions depending on who calls it


# class Dog:
#     def speak(self):
#         print("woof!")

# class Cat:
#     def speak(self):
#         print("meow!")

# class Bird:
#     def speak(self):
#         print("tweet!")

# dog = Dog()
# cat = Cat()
# bird = Bird()


#e.g1:
# dog.speak()
# cat.speak()
# bird.speak()

# e.g2:

#store the objects in a list
# animals = [dog, cat, bird]

#call the same method for every object

# for animal in animals:
#     animal.speak()

# Polymorphism with Inheritance
# ------------------------------

# Parent class:
# class Animal:
#     def speak(self):
#         print("Animals make sound!")


# child classes:
# class Dog(Animal): 
#     def speak(self):
#         print("Dog says woof!")

#     def Eat(self):
#             print("Dog eats!")

# class Cat(Animal):
#     def speak(self):
#         print("Cat says meow!")

#     def Sleeps(self):
#             print("Cat sleeps!")    

# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()

# animals  = [Dog(), Cat()]

# for animal in animals:
#     animal.speak()

# the example above just showed: Method overriding
# method overriding is one of the most common form of polymorphism



# this function is polymorphic
def checkFruit(fruit):
    fruit.Describe()

# Parent class:
class Fruit:
    def Describe(self):
        print("I am a fruit")

# Children:
class Apple(Fruit):
    def Describe(self):
        print("I am an apple")

class Orange(Fruit):
    def Describe(self):
        print("I am an orange")


orange1 = Orange()
apple1 = Apple()

# checkFruit(orange1)
# checkFruit(apple1)

#duck typing - dynamic

def show(value):
    print(value)

show("hello")
show(123)
show([1,5])

# Python

# Java

# JavaScript
# C#
# PHP
# C++
# C
# TypeScript
# JQuery
# Golang
# Kotlin
# Swift
# Apex

# W3Schools



class Animal:
    def speak(self):
        print("Animals make sound!")

class Dog(Animal): 
    def speak(self):
        print("Dog says woof!")

    def Eat(self):
            print("Dog eats!")

class Cat(Animal):
    def speak(self):
        print("Cat says meow!")

    def Sleeps(self):
            print("Cat sleeps!")    

animals  = [Dog(), Cat()]


# Method we want to find
target = "Eat"

# Check every animal object
for animal in animals:

    # Get all attribute and method names belonging to the object
    for name in dir(animal):

        # Check whether the name matches the target
        if name == target:

            # Retrieve the actual attribute or method
            attr = getattr(animal, name)

            # Check whether it is a method that can be called
            if callable(attr):
                print(
                    f"The method '{name}' was found "
                    f"in {animal.__class__.__name__}"
                )

                # Call the method
                attr()