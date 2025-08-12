# Practice Ideas
# Create a list of your top 5 favorite movies and print them in reverse order.
# Save the list to a file using write().
# Read the file back and display it.
# Count how many lines are in a file.


movies = ["Hanuman","Champa","krish","Krishn","Bahubali"]
movies.reverse()
for movie in movies:
    print(movie)

file = open("movies.txt","w")
file.write(str(movies))
file.close()

with open("movies.txt","r") as file:
    content = file.read()
    print(content)