print('------------------- QUIZ GAME -------------------')

playing = input(" Do you want to play the game : ")

if playing.lower() != "yes":
        quit()

print("Okay let's play")
score = 0
        
answer = input("what does CPU stand for: ")
if answer.lower() == "central processing unit":
        print("Correct")
        score += 1
else :
    print ("incorrect")

answer = input("What are the Red Haired Apes called: ")
if answer.lower() == "orangutans":
        print("Correct")
        score += 1
else :
    print ("incorrect")

answer = input("What was the most played game in 2018: ")
if answer.lower() == "fortnite":
        print("Correct")
        score += 1
else :
    print ("incorrect")

answer = input("Who are you? : ")
if answer.lower() == "me":
        print("Correct")
        score += 1
else :
    print ("incorrect")


print("\n")
print("Your final score is: " + str(score) + ". Congratulations")
    