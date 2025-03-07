"""
Name: N'din Assi 
course code: CIS 261 
Course Name: Computer programming 1 
program: Movie GuidePart1
"""

def main():
    movies=["Test Movie"]
    terminate="start"
    heading()
    while terminate!="exit":
        terminate = input("Command: ").lower()
        if terminate=="list":
            listMovies(movies)
        elif terminate=="add":
            addMovies(movies)
        elif terminate=="del":
            delMovies(movies)
        elif terminate =="exit":
            print("Program Terminating")
            break
        else:
            print("Not a valid command. Please try again.")
            
   
def heading():
    print("COMMAND MENU")   
    print("list - List all movies ")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")

def listMovies(movies):
    print("Movie List")
    for index,element in enumerate(movies):
        
        print(f"{index}. {element}")
    
def addMovies(movies):
    newmovie=input("Name: ")
    movies=movies.append(newmovie)
    print(f"{newmovie} movie added successfully.")
def delMovies(movies):
    deletemovie=int(input("Enter the number of movie to delete: "))
    deleted_movie = movies[deletemovie]
                    
                          
                         
    movies=movies.pop(deletemovie)
    
    
    print(f"{deleted_movie}Movie was deleted successfully") 

if __name__== "__main__":
    print("The Movie List Program")
    main()

