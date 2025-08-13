import json

# converting json string to python object using json.loads()
# json_string = '{"name":"prabin","age":21,"skills":["python","django"]}'

# data = json.loads(json_string)
# print(data)
# print(data["skills"])

# converting python object into json string using json.dumps()

# data = {
#     "name":"prabin",
#     "age":21,
#     "skills":[
#         "java",
#         "python",
#         "javascript"
#     ]
# }
# print(json.dumps(data))

# now using json.load() to read a json file 
# with open("data.json","r") as file:
#     json_data = json.load(file)

#     print(json_data)

# writing json into the file using json.dump()

# data = {
#     "name":"prabin",
#     "age":21,
#     "skills":[
#         "java",
#         "python",
#         "javascript"
#     ]
# }
# with open("json.txt","w") as file:
#     json.dump(data,file)