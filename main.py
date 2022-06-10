import random

print("Welcome,lets play")
print("Instructions")
print("R for Rock")
print("P for Paper")
print("S for Scissors")

computerscore = 0
playerscore = 0
tiescore = 0

PossibleHands = ["R","P","S"]

def CheckForWinner(playerHand, compterHand):
    if(playerHand == "R" and computerHand == "P"):
        print("Sorry,you lost")
        return "computer"
    elif(playerHand == "R" and computerHand == "S"):
        print("Congrats! You Have Won")
        return "player"
    elif(playerHand == "S" and computerHand == "P"):
        print("Congrats! You Have Won")
        return "player"
    elif(playerHand == "S" and computerHand == "R"):
        print("Sorry,you lost")
        return "computer"
    elif(playerHand == "P" and computerHand == "R"):
        print("Congrats! You Have Won")
        return "player"
    elif(playerHand == "P" and computerHand == "S"):
        print("Sorry,you lost")
        return "computer"
    else:
        print("it's a tie, play again")
        return "Tie"

while(playerscore != 1 and computerscore != 1):
    while True:
        playerHand = input("\nPick a hand. R, P, or S: ")
        if(playerHand == "R" or playerHand == "P" or playerHand == "S"):
          break
        else:
            print("ERROR")
    computerHand = random.choice(PossibleHands)
    
    print("Your hand: ", playerHand)
    print("Computer hand: ", computerHand)
    result = CheckForWinner(playerHand, computerHand)
    if(result == "player"):
        playerscore += 1
    elif(result == "computer"):
        computerscore += 1
    else:
        tiescore += 1
    #print("Your Score: ", playerscore, "Computer: ", computerscore, "Ties: ", tiescore)
    
print("GAME OVER! Thank You For Playing")











