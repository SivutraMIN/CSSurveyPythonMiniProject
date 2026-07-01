import movieData
import seatData

def runBookAMovie():
    result = None
    redo = None
    while True:  # genre loop
        SomeList = []

        # List of 5 available movie genre
        print("Here is the list of genre")
        genre = ["horror", "action", "fantasy", "romance", "scifi"]
        num = 0
        for number in genre:
            num += 1
            print(f"{num}. {number}")

        Genre = input("Choose your genre: ")

        # Horror
        if Genre == "1":
            movie = movieData.getMovie("Horror")
            movieData.print_available_movie("Horror")
            while True:  # movie loop
                HorrorMovieChoice = input("Choose your movie (1-4, or 0 to pick genre again): ")
                if HorrorMovieChoice == "0":
                    break
                if HorrorMovieChoice == "1":
                    SomeList.append(movie[0][2])
                elif HorrorMovieChoice == "2":
                    SomeList.append(movie[1][2])
                elif HorrorMovieChoice == "3":
                    SomeList.append(movie[2][2])
                elif HorrorMovieChoice == "4":
                    SomeList.append(movie[3][2])
                else:
                    print("Invalid Choice.")
                    continue


                while True:  # showtime loop
                    Showtime = input("Choose your show time (1-2, or 0 to pick movie again): ")
                    if Showtime == "0":
                        SomeList.clear()
                        break
                    idx = int(HorrorMovieChoice) - 1
                    if Showtime == "1":
                        SomeList.append(movie[idx][4])
                        SomeList.append(movie[idx][6])
                    elif Showtime == "2":
                        SomeList.append(movie[idx][5])
                        SomeList.append(movie[idx][7])
                    else:
                        print("Invalid Choice.")
                        continue

                    print("Available Seats")
                    seatData.printSeat(seatData.getSeat())
                    while True:
                        userDesiredSeatRow = input("Which seat row do you prefer? (A-J): ").upper()
                        if userDesiredSeatRow not in ["A","B","C","D","E","F","G","H","I","J"]:
                            print("Invalid Choice.")
                        else:
                            break

                    while True:
                        try:
                            userDesiredSeatNumber = int(input("Which seat number do you prefer? (1-10): "))
                            if userDesiredSeatNumber not in [1,2,3,4,5,6,7,8,9,10]:
                                print("Invalid Choice.")
                            else:
                                break
                        except:
                            print("Invalid Choice.")
                    seatData.bookSeat(userDesiredSeatRow, userDesiredSeatNumber)
                    SomeList.append(userDesiredSeatRow)
                    SomeList.append(userDesiredSeatNumber)
                    setComfirmationList(SomeList,"new")
                    ticket.generateTicket() 

                    return

                if HorrorMovieChoice == "0":
                    break

        # Action
        elif Genre == "2":
            movieData.print_available_movie("Action")
            movie = movieData.getMovie("Action")
            while True:
                ActionMovieChoice = input("Choose your movie (1-4, or 0 to pick genre again): ")
                if ActionMovieChoice == "0":
                    break
                if ActionMovieChoice == "1":
                    SomeList.append(movie[0][2])
                elif ActionMovieChoice == "2":
                    SomeList.append(movie[1][2])
                elif ActionMovieChoice == "3":
                    SomeList.append(movie[2][2])
                elif ActionMovieChoice == "4":
                    SomeList.append(movie[3][2])
                else:
                    print("Invalid Choice.")
                    continue

                while True:
                    Showtime = input("Choose your show time (1-2, or 0 to pick movie again): ")
                    if Showtime == "0":
                        SomeList.clear()
                        break
                    idx = int(ActionMovieChoice) - 1
                    if Showtime == "1":
                        SomeList.append(movie[idx][4])
                        SomeList.append(movie[idx][6])
                    elif Showtime == "2":
                        SomeList.append(movie[idx][5])
                        SomeList.append(movie[idx][7])
                    else:
                        print("Invalid Choice.")
                        continue

                    print("Available Seats")
                    seatData.printSeat(seatData.getSeat())
                    while True:
                        userDesiredSeatRow = input("Which seat row do you prefer? (A-J): ").upper()
                        if userDesiredSeatRow not in ["A","B","C","D","E","F","G","H","I","J"]:
                            print("Invalid Choice.")
                        else:
                            break

                    while True:
                        try:
                            userDesiredSeatNumber = int(input("Which seat number do you prefer? (1-10): "))
                            if userDesiredSeatNumber not in [1,2,3,4,5,6,7,8,9,10]:
                                print("Invalid Choice.")
                            else:
                                break
                        except:
                            print("Invalid Choice.")
                    seatData.bookSeat(userDesiredSeatRow, userDesiredSeatNumber)
                    SomeList.append(userDesiredSeatRow)
                    SomeList.append(userDesiredSeatNumber)
                    setComfirmationList(SomeList,"new")
                    ticket.generateTicket() 

                    return

                if ActionMovieChoice == "0":
                    break

        # Fantasy
        elif Genre == "3":
            movieData.print_available_movie("Fantasy")
            movie = movieData.getMovie("Fantasy")
            while True:
                FantasyMovieChoice = input("Choose your movie (1-4, or 0 to pick genre again): ")
                if FantasyMovieChoice == "0":
                    break
                if FantasyMovieChoice == "1":
                    SomeList.append(movie[0][2])
                elif FantasyMovieChoice == "2":
                    SomeList.append(movie[1][2])
                elif FantasyMovieChoice == "3":
                    SomeList.append(movie[2][2])
                elif FantasyMovieChoice == "4":
                    SomeList.append(movie[3][2])
                else:
                    print("Invalid Choice.")
                    continue

                while True:
                    Showtime = input("Choose your show time (1-2, or 0 to pick movie again): ")
                    if Showtime == "0":
                        SomeList.clear()
                        break
                    idx = int(FantasyMovieChoice) - 1
                    if Showtime == "1":
                        SomeList.append(movie[idx][4])
                        SomeList.append(movie[idx][6])
                    elif Showtime == "2":
                        SomeList.append(movie[idx][5])
                        SomeList.append(movie[idx][7])
                    else:
                        print("Invalid Choice.")
                        continue

                    print("Available Seats")
                    seatData.printSeat(seatData.getSeat())
                    while True:
                        userDesiredSeatRow = input("Which seat row do you prefer? (A-J): ").upper()
                        if userDesiredSeatRow not in ["A","B","C","D","E","F","G","H","I","J"]:
                            print("Invalid Choice.")
                        else:
                            break

                    while True:
                        try:
                            userDesiredSeatNumber = int(input("Which seat number do you prefer? (1-10): "))
                            if userDesiredSeatNumber not in [1,2,3,4,5,6,7,8,9,10]:
                                print("Invalid Choice.")
                            else:
                                break
                        except:
                            print("Invalid Choice.")
                    seatData.bookSeat(userDesiredSeatRow, userDesiredSeatNumber)
                    SomeList.append(userDesiredSeatRow)
                    SomeList.append(userDesiredSeatNumber)
                    setComfirmationList(SomeList,"new")
                    ticket.generateTicket() 

                    return

                if FantasyMovieChoice == "0":
                    break

        # Romance
        elif Genre == "4":
            movieData.print_available_movie("Romance")
            movie = movieData.getMovie("Romance")
            while True:
                RomanceMovieChoice = input("Choose your movie (1-4, or 0 to pick genre again): ")
                if RomanceMovieChoice == "0":
                    break
                if RomanceMovieChoice == "1":
                    SomeList.append(movie[0][2])
                elif RomanceMovieChoice == "2":
                    SomeList.append(movie[1][2])
                elif RomanceMovieChoice == "3":
                    SomeList.append(movie[2][2])
                elif RomanceMovieChoice == "4":
                    SomeList.append(movie[3][2])
                else:
                    print("Invalid Choice.")
                    continue

                while True:
                    Showtime = input("Choose your show time (1-2, or 0 to pick movie again): ")
                    if Showtime == "0":
                        SomeList.clear()
                        break
                    idx = int(RomanceMovieChoice) - 1
                    if Showtime == "1":
                        SomeList.append(movie[idx][4])
                        SomeList.append(movie[idx][6])
                    elif Showtime == "2":
                        SomeList.append(movie[idx][5])
                        SomeList.append(movie[idx][7])
                    else:
                        print("Invalid Choice.")
                        continue

                    print("Available Seats")
                    seatData.printSeat(seatData.getSeat())
                    while True:
                        userDesiredSeatRow = input("Which seat row do you prefer? (A-J): ").upper()
                        if userDesiredSeatRow not in ["A","B","C","D","E","F","G","H","I","J"]:
                            print("Invalid Choice.")
                        else:
                            break

                    while True:
                        try:
                            userDesiredSeatNumber = int(input("Which seat number do you prefer? (1-10): "))
                            if userDesiredSeatNumber not in [1,2,3,4,5,6,7,8,9,10]:
                                print("Invalid Choice.")
                            else:
                                break
                        except:
                            print("Invalid Choice.")
                    seatData.bookSeat(userDesiredSeatRow, userDesiredSeatNumber)
                    SomeList.append(userDesiredSeatRow)
                    SomeList.append(userDesiredSeatNumber)
                    setComfirmationList(SomeList,"new")
                    ticket.generateTicket() 

                    return

                if RomanceMovieChoice == "0":
                    break

        # Sci-Fi
        elif Genre == "5":
            movieData.print_available_movie("Sci_Fi")
            movie = movieData.getMovie("Sci_Fi")
            while True:
                SciFiMovieChoice = input("Choose your movie (1-4, or 0 to pick genre again): ")
                if SciFiMovieChoice == "0":
                    break
                if SciFiMovieChoice == "1":
                    SomeList.append(movie[0][2])
                elif SciFiMovieChoice == "2":
                    SomeList.append(movie[1][2])
                elif SciFiMovieChoice == "3":
                    SomeList.append(movie[2][2])
                elif SciFiMovieChoice == "4":
                    SomeList.append(movie[3][2])
                else:
                    print("Invalid Choice.")
                    continue

                while True:
                    Showtime = input("Choose your show time (1-2, or 0 to pick movie again): ")
                    if Showtime == "0":
                        SomeList.clear()
                        break
                    idx = int(SciFiMovieChoice) - 1
                    if Showtime == "1":
                        SomeList.append(movie[idx][4])
                        SomeList.append(movie[idx][6])
                    elif Showtime == "2":
                        SomeList.append(movie[idx][5])
                        SomeList.append(movie[idx][7])
                    else:
                        print("Invalid Choice.")
                        continue

                    print("Available Seats")
                    seatData.printSeat(seatData.getSeat())
                    while True:
                        userDesiredSeatRow = input("Which seat row do you prefer? (A-J): ").upper()
                        if userDesiredSeatRow not in ["A","B","C","D","E","F","G","H","I","J"]:
                            print("Invalid Choice.")
                        else:
                            break

                    while True:
                        try:
                            userDesiredSeatNumber = int(input("Which seat number do you prefer? (1-10): "))
                            if userDesiredSeatNumber not in [1,2,3,4,5,6,7,8,9,10]:
                                print("Invalid Choice.")
                            else:
                                break
                        except:
                            print("Invalid Choice.")
                    seatData.bookSeat(userDesiredSeatRow, userDesiredSeatNumber)
                    SomeList.append(userDesiredSeatRow)
                    SomeList.append(userDesiredSeatNumber)
                    setComfirmationList(SomeList,"new")
                    ticket.generateTicket() 

                    return

                if SciFiMovieChoice == "0":
                    break

            

        else:
            print("Invalid Choice. Please enter 1-5.")
        
        

    

        









import ticket

def validateInput(correctDataType,inputDataType):
    pass


def setComfirmationList(someList,action=None):
    if action== "new" or action =="update":
        setComfirmationList.list = someList
    if action == "getList":
        return setComfirmationList.list

def getComfirmationList():
    return setComfirmationList(list(),action="getList")