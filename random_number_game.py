import random

print("---------------------- Guessing Game ----------------------")

top_of_range = input("Type of Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number larger than 0")
        quit()

else : 
    print("Please enter a number")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True : 
    guesses += 1 
    user_guess = input("Make your guess: ") 
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else :
        print("Please enter a number")
        continue

    if user_guess == random_number :
        print ("Congratulations you got the number.")  
        break
    elif user_guess >= random_number :
        print("Your guess is higher than the random number.")
    else :
        print ("Your guess is lower than the random number.")


print("You got the answer in", guesses, "guesses")







