from random import randint

mountain = []

for item in range(5):
    mountain.append(["*"]*5)

def printMountain(mountain):
    for row in mountain:
        print(" ".join(row))

def randomRow(mountain):
    row = randint(0, len(mountain)-1)
    return row
def randomColumn(mountain):
    column = randint(0, len(mountain)-1)
    return column

treasureRow = randomRow(mountain)
treasureColumn = randomColumn(mountain)

print('There is a hidden treasure in this mountain, find it!')
print("\n")
printMountain(mountain)

for turn in range(4):
    print("\n")
    guessRow = int(input("Guess Row (0 is first row): "))

    guessColumn = int(input("Guess Column (0 is first column: "))

    if guessRow == treasureRow and guessColumn == treasureColumn:
        print('Congrats! You found the treasure!')
        mountain[treasureRow][treasureColumn] = "W"
        printMountain(mountain)
        break
    elif guessRow not in range(len(mountain)) or guessColumn not in range(len(mountain)):
        print('You are outside the mountain!Try again')
    else:
        mountain[guessRow][guessColumn] = "L"
        printMountain(mountain)
        print('Nope, try again!')
        print("You have {0} turn(s) left you are on turn {1}".format(3-turn , turn+1))
print('You are out of lives! Restart to try again!')
