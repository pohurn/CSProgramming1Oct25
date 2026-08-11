
#ENCAPSULATION

# => It means a class has data and it has methods that manipulate that data
# => It means keeping data and the methods that work with that data together inside a class
# while controling how that data can be accesses or changed

#e.g 1 :

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

# account = BankAccount(1000)
# print(account.balance)

# Problem: anyone can change the balance directly
# account.balance = -5000
# print(account.balance)



#WITH ENCAPSULATION

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:            
#             self.balance += amount
#             #balance = balance + amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             #balance = balance - amount
#         else:
#             print("Not enough money!")


# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(200)


# print(account.balance)

# account.deposit(13700)

# print(account.balance)

#balance => the data
# deposit() and withdraw() => methods that control what happens to the data
# And they are all grouped inside BankAccount

# so this is the basic idea of encapsulation


#Public Attributes (Public => means that it is accessible from anywhere)
# class Student:
#     def __init__(self, name):
#         self.studentname = name

# student = Student("Goodness");

# print(student.studentname)

# student.studentname = "Allan"

# print(student.studentname)

#Protected Attribute
# python uses a single underscore _ as a convention meaning:
# this is intended for internal use. please do not access it directly unless necessary
# name -> public
# _name -> protected by convention


# class Student:
#     def __init__(self, name):
#         self._studentname = name

#     def changeName(self, name):
#         self._studentname = name

# student = Student("Goodness");

# student.changeName("Allan")
# print(student._studentname)


# Private Attributes
# for private attributes we use 2 _
# two underscores trigger the python's name mangling mechanism

# class Student:
#     def __init__(self, name):
#         self.__studentname = name

#     def get_name(self):
#         return self.__studentname;

#     def set_name(self, name):
#         self.__studentname = name

        

# student = Student("Fatine")
# # print(student.__studentname) -> gives an error because studentname is private

# print(student.get_name())


# student.set_name("Allan")

# print(student.get_name())



#=====================

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:            
#             self.__balance += amount
#             #balance = balance + amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             #balance = balance - amount
#         else:
#             print("Not enough money!")

#     def CheckBalance(self):
#         print(self.__balance)


# account = BankAccount(5000)

# account.__balance = 15000

# print(account.__balance)

# account.deposit(200)

# account.withdraw(500)

# account.CheckBalance()


# Remaining to explain:
# => getter / setter
# => @property keyword