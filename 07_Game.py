
import random
randomNumber = random.randint(1, 99)

# Priting the random number
print(randomNumber)


userGuess = None
guesses = 1

while (userGuess != randomNumber):
    # Getting input from user
    userGuess = int(input("Please enter your number :"))
    print("Entered Number is : ", userGuess)

    if (userGuess == randomNumber):
        print("You guess is right ")

    else:

        if(userGuess > randomNumber):
            print("Please enter smaller number ")
        else:
            print("Please enter larger number")
        guesses += 1

with open("highscore.txt", "r") as f:
    hiscore = int(f.read())


if(guesses < hiscore):
    print("You have just broken the hight score ")
    with open("highscore.txt", "w") as f:
        guessStr = str(guesses)
        f.write(guessStr)


print(f"you guessed the number in {guesses}")
