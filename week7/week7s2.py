# #ABSTRACTION

# # it means using something complicated without needing to know what is happening inside

# # so we define what an object should be able to do while letting the child classes decide how they do it

# from abc import ABC, abstractmethod

# class House(ABC):
    
#     @abstractmethod
#     def BuildDoor(self):
#         print("Door is built in House")

#     @abstractmethod
#     def BuildWindow(self):
#         print("Window is built in the House")


# class SmallHouse(House):
#     def BuildDoor(self):
#         print("Door is built in Small House")
    
#     def BuildWindow(self):
#         print("Window is built in the Small House")

# class BigHouse(House):
#     def BuildDoor(self):
#         print("Door is built in Big House")
    
#     def BuildWindow(self):
#         print("Window is built in the Big House")


# smallHouse = SmallHouse()
# smallHouse.BuildWindow()
# smallHouse.BuildDoor()

# bigHouse = BigHouse()
# bigHouse.BuildDoor()
# bigHouse.BuildWindow()

# JAVA FOR EXAMPLE
# you can look into these for the future:
# public, protected, private, abstract classes
# interface

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod # -> Method that child classes MUST implement
    def send(self, message):
        pass


class Email(Notification):
    def send(self, message):
        print(f"sending email: {message}")

class SMS(Notification):
    def send(self, message):
        print(f"sending SMS: {message}")

class WhatsApp(Notification):
    def send(self, message):
        print(f"sending WhatsApp: {message}")


class Firebase(Notification):
    def send(self, message):
        print(f"sending Firebase Push Notif: {message}")



notifications = [
    Email(),
    SMS(),
    WhatsApp(),
    Firebase()
]

for notification in notifications:
    notification.send("Hello")



##
## 1. Abstraction hides unnecessary details
## 2. An abstract class can define what child classes must do
## 3. @abstractmethod forces the child classes to implement the specific method


#IF YOU WANT YOU CAN LOOK INTO:
# data abstraction
# deep decorator theory


# # class Animal:
# #     def make_sound(self):
# #         print("parent")

# # class Dog(Animal):
# #     def Bark(self):
# #         print("bark")


# # class Cat(Animal):
# #     def make_sound(self):
# #         print("Meow!")

# # dog = Dog()
# # cat = Cat()

# # dog.make_sound()
# # cat.make_sound()

# # dog.Bark()

# # if you look at the class Animal, it says that each child should have the method make_sound()


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         print("I am from the parent and not needed in child - sound")

#     @abstractmethod
#     def Eat(self):
#         print("I am from the parent and not needed in child - eat")




# class Penguin(Animal):
#     def Sleep(self):
#         print("Peinguin sleeps")

#     def make_sound(self):
#         print("I am from the child - sound")

#     def Eat(self):
#         print("I am from the child - eat")


# penguin = Penguin()

# penguin.Eat()
# penguin.make_sound()

# # class Cat(Animal):
# #     def make_sound(self):
# #         print("Meoww")

# # class Dog(Animal):

# #     # def make_sound(self):
# #     #     print("wooooffff")

# #     def Bark(self):
# #         print("bark")


# # cat = Cat()
# # dog = Dog()

# # cat.make_sound()
# # dog.make_sound()