import bookAMovie
import random

def generateTicket():
    someList = bookAMovie.getComfirmationList()
    ticket = f"{someList[2]}-{random.randint(0,1001)}"
    someList.insert(0,ticket)

    bookAMovie.setComfirmationList(someList,action="update")


import csv
fileLocation = "ticketStorage.csv"
def addTicketToStorage(comfirmationList):
    with open(fileLocation,"w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(comfirmationList)

def searchTicket(ticketID):
    with open(fileLocation,"r", newline='') as file:
        reader = csv.reader(file)
        someRandomList = []
        for row in reader:
            if row[0] == ticketID:
                someRandomList.append(row)
        if len(someRandomList) > 0:
            return someRandomList
        else:
            return None


