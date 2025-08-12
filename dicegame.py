import random

move = "roll"
exit = "quit"

user = str(input("Enter roll to start and quit to end:"))

if user == exit:
    print("Game has ended")
elif user == move:
    print(f"your number is {random.randint(1,6)}")
else:
    print("Please enter the correct option")