# list in python
# lists = ["banana","apple","cherry"]
# lists.append("orange") #list["banana","apple","cherry","orange"]
# lists.remove("banana")
# # now displaying list
# for list in lists:
#     print(list)

    # list for favourite movies
    # movies =["hanuman","narshima","bahubali","I","Theri","salar"]
    # movies.append("Lover")
    # movies.append("Aandhadun")
    # movies.remove("salar")
    # for movie in movies:
    #     print(movie)

# tuples  in python
# coordinates = (10,20)
# print(coordinates[0])


# city = ("Gaindakot","Naranghat","chitwan")
# print(city)


# set in python

# colors = {"red","green","blue"}
# print("red" in colors)# returns true
# colors.add("yellow")
# colors.remove("red")

# number = {1,2,1,3,4}
# number.add(4)
# for num in number:
#     print(num)


# dictonary in python

student = {"namee":"Prabin","age":21,"grade":"A"}
print(student["namee"])
student["age"]=25
student["address"]="chitwan"

for key,value in student.items():
    print(f"{key}:{value}")