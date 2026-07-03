import bookAMovie
import random

import os
baseFileLocation = os.path.dirname(os.path.abspath(__file__))
fileLocation = os.path.join(baseFileLocation,"ticketStorage.csv")

def generateTicket():
    someList = bookAMovie.getComfirmationList()
    ticket = f"{someList[2]}-{random.randint(0,1001)}"
    someList.insert(0,ticket)

    bookAMovie.setComfirmationList(someList,action="update")


import csv
def addTicketToStorage(comfirmationList):
    with open(fileLocation,"w") as file:
        writer = csv.writer(file)
        writer.writerow(comfirmationList)

def searchTicket(ticketID):
    with open(fileLocation,"r") as file:
        reader = csv.reader(file)
        someRandomList = []
        for row in reader:
            if row[0] == ticketID:
                someRandomList.append(row)
        if len(someRandomList) > 0:
            return someRandomList
        else:
            return None


