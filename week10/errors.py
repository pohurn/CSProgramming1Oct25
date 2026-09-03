
# There are different kinds of errors.

# Syntax errors — Python cannot understand the way the code is written.
# Runtime errors / exceptions — the code is written correctly, but something goes wrong while it runs.
# Logical errors — the program runs, but gives the wrong result.


# SyntaxError
# A syntax error is like writing a sentence with incorrect grammar.
# Python cannot understand the instruction.
# This code contains a syntax error

# age = 20

# if age >= 18
#     print("Adult")

#Missing closing bracket
# print("Hello"

#Indentation - Indentation Error
# if True:
# print("Hello")

# LogicalError
# A logical error is different.
# The program does not crash, but the answer is wrong.

# price = 100
# quantity = 5

# # Wrong calculation
# total = price + quantity

# print(total)

# Python did exactly what we asked.
# The problem is that our instruction was wrong.

# Exception
# An exception is an error that happens while the program is running.

# ZeroDivisionError
#e.g 1
# number = 10
# result = number / 0
# print(result)

#e.g2
# ValueError
# age = int(input("Enter your age: "))

# IMPORTANT CONCEPT
# An exception does not necessarily mean our entire program is badly written.
# Sometimes an unexpected situation happens while the program is running.

# TypeError
# A TypeError happens when we try to perform an operation using incompatible data types.

# age = 20
# print("Your age is " + age)

# NameError
# print(student_name)

# IndexError
# students = ["John", "Mary", "Ali"]
# print(students[10])

# KeyError

student = {
    "name": "John",
    "age": 20
}

# print(student["name"]) #no error

# print(student["email"]) #error

# FileNotFoundError
# file = open("students.txt")



#WHAT CAN WE DO TO FIX? - USE EXCEPT

# the code below has a problem if user inputs age as e.g twenty
# number = int(input("Enter your age: "))
# print("Your age is", number)
# print("Program Finished")

# try: # python try to run this for me
#     number = int(input("Enter your age: "))
#     print("Your age is", number)

# except: # if something goes wrong above, do this instead
#     print("Enter a valid number")

# print("Program Finished")

# #example 2
# try:
#     number = int(input("Enter your age: "))    
# except KeyError:
#     print("Key error observed!")

# except ValueError:
#     print("Value Error observed!")

# except IndexError:
#     print("Value Error observed!")

# except ZeroDivisionError:
#     print("Value Error observed!")

# # example 3

# try:
#     number1 = int(input("Enter first number: "))    
#     number2 = int(input("Enter second number: "))   

#     answer = number1/number2
#     print("Answer is", answer)

# except ValueError:
#     print("Value Error observed!")

# except ZeroDivisionError:
#     print("ZeroDivison Error observed!")


# #Example 4

# try:
#     number1 = int(input("Enter first number: "))    
#     number2 = int(input("Enter second number: "))   

#     answer = number1/number2
#     print("Answer is", answer)

# except Exception as error:
#     print(error)

# print("hellooo")

# #Example 5
# try:
#     age = int(input("Enter your age: "))  

# except ValueError:
#     print("Invalid age")

# else:
#     print("Your age is ", age)

# #Example 6
# try:
#     number = int(input("input a number: "))  
#     print("Number is", number)

# except ValueError:
#     print("Invalid number")

# finally:
#     print("This code always runs")

# #Example 7

# try:
#     number1 = int(input("Enter first number: "))    
#     number2 = int(input("Enter second number: "))   

#     answer = number1/number2
#     print("Answer is", answer)

# except ValueError:
#     print("Value Error observed!")

# except ZeroDivisionError:
#     print("Value Error observed!")

# else:
#     print("Result", answer)

# finally:
#      print("Calculation finished")


def Calculate():
    
    try:
        number = int(input("Enter a number: "))   

        return number

    except ValueError:
        return 0

    finally:
        print("Program Finished")



def Calculate():
    
    try:
        number = int(input("Enter a number: "))   

        return number

    except ValueError:
        return 0

    print("Program Finished")
    