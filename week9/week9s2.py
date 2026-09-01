
#FILE I/O
# INPUT - python reads information from a file
# OUTPUT - python writes information to a file

# file.txt, file.csv, test.pdf

# name = input("What's your name? ")
# print(name)


#Example 1
# #copybook is just a variable name that is used to assign something
# #Open a file name file.txt
# copybook = open("file.txt", "w")

# # Write your text inside the file
# copybook.write("hello this is a file where i wrote something")

# # Close the file
# copybook.close()

#Example 2

# #Open a file name file.txt
# file = open("file2.txt", "w")

# # \n means next line
# # Write your text inside the file
# file.write("Anita\n")
# file.write("Goodness\n")
# file.write("Stephy\n")
# file.write("Vincent\n")
# file.write("Mosses")

# # Close the file
# file.close()

#Example 3 - creating = adding text - error if file already available

# #Open a file name file.txt
# file = open("file3.txt", "x")

# # Write your text inside the file
# file.write("THIS IS A TEST")

# # Close the file
# file.close()


#Example 4 - creating dynamic files 
# #Open a file
# filename = input("enter file name: ")
# file = open(filename, "x")

# # Write your text inside the file
# file.write("THIS IS A TEST")

# # Close the file
# file.close()