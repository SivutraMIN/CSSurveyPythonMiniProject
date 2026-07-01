def getFreshSeat():
    allOfTheSeat = [
    [1,2,3,4,5,6,7,8,9,10], #A (1.Num) (1.9 = A9)
    [1,2,3,4,5,6,7,8,9,10], #B
    [1,2,3,4,5,6,7,8,9,10], #C
    [1,2,3,4,5,6,7,8,9,10], #D
    [1,2,3,4,5,6,7,8,9,10], #E
    [1,2,3,4,5,6,7,8,9,10], #F
    [1,2,3,4,5,6,7,8,9,10], #G
    [1,2,3,4,5,6,7,8,9,10], #H
    [1,2,3,4,5,6,7,8,9,10], #I
    [1,2,3,4,5,6,7,8,9,10], #J
    ]   
    return allOfTheSeat

fileLocation = "seat.csv"
import csv

def setFreshSeat():
    with open(fileLocation, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(getFreshSeat())

def convertLetterToNumber(letter):
    letter = letter.lower()
    if letter == "a":
        return 0
    elif letter == "b":
        return 1
    elif letter =="c":
        return 2
    elif letter =="d":
        return 3
    elif letter == "e":
        return 4
    elif letter == "f":
        return 5
    elif letter == "g":
        return 6
    elif letter == "h":
        return 7
    elif letter == "i":
        return 8
    elif letter == "j":
        return 9
    
def bookSeat(userDesiredSeatRow,userDesiredSeatNumber):
    userDesiredSeatRow = convertLetterToNumber(userDesiredSeatRow)
    userDesiredSeatNumber -= 1
    with open(fileLocation, "r", newline='') as file:
        reader = csv.reader(file)
        rowCounter = 0
        listOfRow = []
        for row in reader:
            listOfRow.append(row)
            if rowCounter == userDesiredSeatRow:
                listOfRow[rowCounter][userDesiredSeatNumber] = "X"
            rowCounter+=1
    with open(fileLocation, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(listOfRow)

def getSeat():
    with open(fileLocation, "r", newline='') as file:
        reader = csv.reader(file)
        allSeatList = []
        for row in reader:
            allSeatList.append(row)

    return allSeatList

def printSeat(allOfTheSeat):
  letter = ["A","B","C","D","E","F","G","H","I","J"]
  tempNumLetter = 0
  for row in allOfTheSeat:
    print(f"{letter[tempNumLetter]}: ", end="")
    for colum in row:
      print(f"[{colum}]", end=" ")
    print("\n")
    tempNumLetter+=1