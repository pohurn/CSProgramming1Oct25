
# # myFunction()

# # def myFunction():
# #     print("Hello Class")


    
# # myFunction()

# x = 3

# if x==5:
#      #true
#     print("x is 5")
# elif x > 4:
#     #true
#     print("x is greater than 4")
# else:
#     print("x is less than 4")

#     # >
#     # <
#     # >=
#     # <=
#     # ==
#     # !=

def myFunction():
    x = 3

    if x==5:
        #true
        print("x is 5")
    elif x > 4:
        #true
        print("x is greater than 4")
    else:
        print("x is less than 4")


# myFunction()


#finction start
def check_password(pw):
    if(pw == 1234):
        print("Allan  is here")
    elif(pw == 1565):
        print("Akiola is here")
    else:
        print("Access Denied")

#function already ended

def helloFunction():
    print("hello this is a fuinction not related to the previous one")



print("Hello user please enter your pw")
password = input("Enter password: ")

check_password(int(password))