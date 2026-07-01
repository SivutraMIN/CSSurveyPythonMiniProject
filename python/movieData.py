import os
baseFileLocation = os.path.dirname(os.path.abspath(__file__))
fileLocation = os.path.join(baseFileLocation,"data.csv")


def getGenre():
    listOfGenres = ["Horror","Action","Fantasy","Romance","Sci_Fi"]
    return listOfGenres

def getMovie(genre):
    with open(fileLocation,"r") as movieData:
        data = csv.reader(movieData)
        resultMovieList = []
        for row in data:
            if row[1] == genre:

                resultMovieList.append(row)
        
    return resultMovieList
                

# Adding and Removing Movies
import csv



def addMovie(MovieID,MovieGenre,MovieName,MovieDuration,MovieTime1,MovieTime2,MovieDate1,MovieDate2):
    with open(fileLocation,"a") as movieData:
        # movie = ['Movie_ID', 'Movie_Genre', 'Movie_Name', 'Movie_Duration', 'Movie_Time_1', 'Movie_Time_2', 'Movie_Date_1', 'Movie_Date_2']

        movie = [MovieID,MovieGenre,MovieName,MovieDuration,MovieTime1,MovieTime2,MovieDate1,MovieDate2]
        data = csv.writer(movieData)

        data.writerow(movie)

def removeMovie(movieID):
    with open(fileLocation,'r',newline='') as movieData:
        reader = csv.reader(movieData)
        bigAllMovie = []
        for row in reader:
            if row[0] == movieID:
                continue
            bigAllMovie.append(row)

    with open(fileLocation,"w") as movieData:
        writer = csv.writer(movieData)
        for row in bigAllMovie:
            writer.writerow(row)
    
def addGenres(listOfGenres, whatToBeAdded):
  listOfGenres.append(whatToBeAdded)

def printGenres(listOfGenres):
  num = 1
  for genre in listOfGenres:
    print(f"{num}. {genre} ")
    num+=1

def print_available_movie (genre):
    Number = 1
    List = 0
    MovieName = 2
    MovieDuration = 3
    MovieTime1 = 4
    MovieTime2 = 5
    MovieDate1 = 6
    MovieDate2 = 7
    print ("Available Movies: ")
    print ("No. | Movie Name | Movie Duration | Movie Time1 on Movie Date1 | Movie Time2 on Movie Date2")
    movie = getMovie(f"{genre}")
    for i in movie:
        print(
            f"{Number}. {movie[List][MovieName]} | {movie[List][MovieDuration]} mins | {movie[List][MovieTime1]} on {movie[List][MovieDate1]} | {movie[List][MovieTime2]} on {movie[List][MovieDate2]}")
        Number += 1
        List += 1