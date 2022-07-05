number = 23

for x in range(1,5):
    user_input = int(input("Guess a number: "))
    message = "you have " + str(5-x) +" chances remaining"
    if user_input == number:
        print("You win!")

    if user_input > number:
        print("too high, " + message )

    if user_input < number:
        print("too low, " + message)

