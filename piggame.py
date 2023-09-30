import random

def roll():
    roll = random.randint(1,6)
    return roll

# while True:
players = int(input("Enter the number of players: "))
    # print(players)

maxScore = int(input("Maximum Score:" ))
playerScores = [0 for player in range(players)]
# print(playerScores)

while max(playerScores) < maxScore:
# while playerScores < maxScore:


    for playerIdx in range(players):
        print("\nPlayer", playerIdx + 1, "turn has just started!\n")
        print("Your total score is: ", playerScores[playerIdx], "\n")
        currentScore = 0

        while True:
            rollAgain = input("Would you like to roll (y)?")
            if rollAgain.lower() != 'y':
                break

            value = roll()

            if value == 1:
                print("Rolled 1")
                currentScore = 0
                break

            else:
                currentScore += value
                print("Rolled ", value)

            print("Your score is: ", currentScore)

        playerScores[playerIdx] += currentScore

        print("Your total score is:", playerScores[playerIdx])

maxScore = max(playerScores)
winningIdx = playerScores.index(maxScore)
print("player", winningIdx + 1, "is the winner with a score of: ", maxScore)

        
    


