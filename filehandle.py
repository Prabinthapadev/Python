# file = open("hi.txt","w")
# file.write("hello world\n")
# file.write("Hi prabin")
# file.close()

# file = open("hi.txt","r")
# content = file.read()
# print(content)
# file.close()

# name = str(input("Enter your name"))
# file1 = open("vowel.txt","w")
# file2 = open("conconent.txt","w")

# for i in range(len(name)):
#     if(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'):
#         file1.write(name[i])
#     else:
#         file2.write(name[i])
# file1.close()
# file2.close()

# reading file line by line

# file = open("hi.txt","r")
# for line in file:
#     print(line.strip())
# file.close()


# best practice for file handeling
# using with which automatically close the file

# with open("hi.txt","r") as file:
#     content = file.read()
#     print(content)

# Practice Ideas
# Create a list of your top 5 favorite movies and print them in reverse order.
# Save the list to a file using write().
# Read the file back and display it.
# Count how many lines are in a file.

