actual_number = 50
guess = None  # initialize guess

while guess != actual_number:
    guess = int(input("Guess a number: "))

    if guess == actual_number:
        print("Your guess is correct")
    elif guess < actual_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
