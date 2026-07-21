
# Loops, Lists, Break and Continue

# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")


#for loop
#example 1:

# range(5) generates numbers 0 to 4
# 0 1 2 3 4
# for number in range(5):
#     # This line runs once for every number
#     print("Happy")
#     print(number)

#example 2:

# range(1, 5) generates numbers 1 to 4
# 1 2 3 4
# for number in range(1, 5): # 5-1 = 4 ; so it's going to print 4 times
#     print(number)

#example 3:

# start at 2
# stop before 11
# Increase 2

# 2 4 6 8 10 12 14
# for number in range(2, 11, 2):
#     print(number)

#example 4:

# word = "Python"
# for letter in word:
#     print(letter)

# print("We're out of the loop")


#example 5:

#for multiplication from 1 to 10

# number = 5
# for multiplier in range(1, 11):
#     ans = number * multiplier
#     print(number, "X", multiplier, "=", ans)

##
## WHILE LOOPS
# A while loop will continue executing while the condition is true
##

#example 1:

# number = 1
# while number <= 5:
#     print(number)
#     number = number + 1


# example 2:

# countdown = 10
# while countdown > 0:
#     print(countdown)
#     countdown  = countdown - 1


#example 3:

# password = ""

# while password != "programming1":
#     password = input("Enter the password please: ")
# print("Access Granted!")




#
# LISTS
#

fruits = ["Apple", "Orange", "Banana"]

# #remove banana from the list
# fruits.remove("Banana")
# print(fruits)

#Error handling
# fruit_to_remove = "grapes"

# if fruit_to_remove in fruits:
#     fruits.remove(fruit_to_remove)
#     print("fruit removed")
# else:
#     print("fruit not found")


## removing using position

# fruits.pop(1) #removing item from index 1
# print(fruits)

# fruits.pop() #removing item from last index
# print(fruits)









# s = "Python"

# - len(s) - 1: Start at the last index
# - -1: Ensures the loop stops after the first character
# - -1: The step value to iterate backwards
# for i in range(len(s) - 1, -1, -1):
#     print(s[i])