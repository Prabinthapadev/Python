demo = "hi my name is prabin thapa"
file = open("demo.txt", "w")
file.write(demo)
file.close()

with open("demo.txt", "r") as file:
    content = file.read()
    count = 1  # start with 1 because the last word won't have a space
    for char in content:
        if char == " ":
            count += 1

print(f"The length of content is {len(content)}")
print(f"The number of words are {count}")


# or you can do it using slpit() function

print(f"Numbers of words = {len(content.split())}")