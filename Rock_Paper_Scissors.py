import random

print("-------------------- Rock, Paper, Scissors --------------------")

user_wins = 0
computer_wins = 0

RPS = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter one of the following letters to do the following : \n r = Rock \n p = paper \n s= scissors \n q= quit\n")
    if user_input == "q" :
        break

    if user_input not in RPS: 
        continue

    random_number = random.randint(0, 2)

    computer_pick = RPS[random_number]
    print("Computer picked : " + computer_pick + "." ) 

    if user_input == "rock" and computer_pick == "scissors" :
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock" :
        print("You win")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_wins += 1
    else:
        print("You lost")
        computer_wins += 1
        
print("You have won ", user_wins, " times")
print("The computer has won", computer_wins, " times")
print("Goodbye")