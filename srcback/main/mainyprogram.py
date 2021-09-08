from sys import path
from os import getcwd
from pathlib import Path
import datetime

now = datetime.datetime.now()

path.append(str(Path(getcwd()).parent.absolute()) + "/actor")
from actor import Actor
path.append(str(Path(getcwd()).parent.absolute()) + "/director")
from director import Director
path.append(str(Path(getcwd()).parent.absolute()) + "/moviedescription")
from moviedescription import MovieDescription
path.append(str(Path(getcwd()).parent.absolute()) + "/date")
from date import Date
path.append(str(Path(getcwd()).parent.absolute()) + "/movie")
from movie import Movie

movies = []

def add_name ():
    name = input("Write name of this person: ")
    return name 

def add_surname():
    surname = input("Write surname of this person: ")
    return surname

def add_nationality():
    nationality = input("Write nationality of this person: ")
    return nationality

def add_date_of_birth():
    day = int(input("Write day of date of birth: "))
    month = int(input("Write month of date of birth: "))
    year = int(input("Write year of date of birth: "))
    date_of_birth = Date(day, month, year)
    return date_of_birth

def add_date_of_death():
    click = input("If person is still alive write yes, otherwise no")
    if click =="no":
        day = int(input("Write day of date of death: "))
        month = int(input("Write month of date of death: "))
        year = int(input("Write year of date of death: "))
        date_of_death = Date(day, month, year)
        return date_of_death

def add_gender():
    gender = input("Write 1 if person is a women or 2 if person is a man")
    if gender == "1":
        gender = "male"
    elif gender =="2":
        gender = "female"
    return gender

def add_photo_link():
    photo_link = input("Write the url link of image this person: ")
    return photo_link

def add_rating():
    __rating = float(input("Write your own mark of this movie: "))
    if 0 <= __rating <= 10:
        return __rating
    else:
        add_rating()

def add_number_of_movies():
    number_of_movies = int(input("Write the number of appearences: "))
    return number_of_movies

def add_short_description():
    short_description = input("write short description: ")
    return short_description

def add_long_description():
    long_description = input("write long description: ")
    return long_description

def add_title():
    title = input("write title of this movie: ")
    return title

def add_release_date():
    day = int(input("Write day of date of release this movie: "))
    month = int(input("Write day of date of release this movie: "))
    year = int(input("Write day of date of release this movie: "))
    release_date = Date(day, month, year)
    return release_date
    
def create_actor():
        __actor = Actor(add_name(), add_surname(), add_nationality(), add_date_of_birth(),
         add_gender(), add_photo_link(), add_rating(), add_date_of_death())
        return __actor

def create_description():
    __description = MovieDescription(add_title(), add_short_description(), add_long_description())
    return __description

def create_director():
    __director = Director(add_name(), add_surname(), add_nationality(),
     add_date_of_birth(), add_gender(), add_photo_link(), add_rating(), add_number_of_movies())
    click = input("If director is still alive click '1'  ")
    if click == "1":
        day = int(input("Write day of date of death: "))
        month = int(input("Write day of date of death: "))
        year = int(input("Write day of date of death: "))
        Director.set_date_of_death(day, month, year)
    return __director

def create_movie(movies):
    movie = Movie([], create_director(), create_description(), add_release_date(), add_rating())
    click = input("Write no if you want to stop adding new actors to the list: ")
    while click != "no" :
        movie.add_new_actor(create_actor())
    movies.append(movie)
    

def get_account(users):
    __login = input("Write your login: ")
    if __login in users:
        __password = input("Write your password correctly: ")
        if users[__login] != __password:
            print("Not correct data")
            get_account(users)
        else:
            print("Enjoy your account")
    else:
        print("This login doesn't appear in database")

def create_new_account(users):
    login = input("Write your login: ")
    password = input("Write your password: ")
    password2 = input("Confirm your password: ")
    if password ==password2:
        users[login] = password
    else : 
        print("not correct data")

def menu_1(users):
    print("""
    \t\t\tNETFLIX database MENU
    \n
    1 - Create new accout
    2 - Login on your personal account
    0 - Exit

    """)
    click = None
    click = input("What do you choose? Write right number: ")
    if click == "1":
        create_new_account(users)
        menu_1(users)
    elif click == "2":
        get_account(users)
    elif click == "0":
        exit()
    else:
        print("Incorrect choice!")
        menu_1(users)

def menu_2(movies, users):
    print("""
    \t\t\tNETFLIX database MENU
    \n
    1 - Add new movie
    2 - Operate on movies
    0 - Logout

    """)
    click = None
    click = input("What do you choose? Write right number: ")
    if click == "1":
        create_movie(movies)
        menu_2(movies, users)
    elif click == "2":
        a = 0
        for movie in movies:
            a +=1
            print((a), "-", movie.get_description.get_title())
            global value
            click2 = input("\nWhich one do you choose: ")
    elif click == "0":
        menu_1(users)
    else:
        print("Incorrect choice!")
        menu_2(movies, users)

def menu_3(click2, movies):
    print("""
    \t\t\tNETFLIX database MENU
    \n
    1 - Show list of actors
    2 - Show information about director
    3 - Show descriptions about movie
    4 - Get release date
    5 - Write a personal rating of movies
    6 - Change data about movie
    0 - Return

    """)

    click = None
    click = input("What do you choose? Write right number: ")
    if click == "1":
        for index in range(movies[click2-1].get_number_of_actors()):
            actor = movies[click2-1].get_actor(index)
            print("1 - ", actor.get_name(), actor.get_surname() )
    if click == "2":
        print("\t\t\t BASIC INFORMATION ABOUT DIRECTOR:\n")
        director = movies[click2-1].get_director
        print("Name: ",director.get_name())
        print("Surname: ",director.get_surname()),
        print("Age: ",director.get_age()),
        print("Nationality: ",director.get_nationality()),
        print("Gender: ",director.get_gender()),
        print("url Link: ",director.get_photo_link()),
        print("Rating: ",director.get_rating()),
        print("Date of birth: ",director.get_date_of_birth.get_whole_date()),
        print("Date of death: ",director.get_date_of_death.get_whole_date()),
        print("Number of appearences: ",director.get_number_of_movies()),
        print("Efficienty: ",director.get_efficienty(), " movies per annum")
    if click =="3":
        




        for index in range(movies[click2-1].get_number_of_actors()):
            actor = movies[click2-1].get_actor(index)
            print(
                "Name: ",actor.get_name(),
                "Surname: ",actor.get_surname(),
                "Age: ",actor.get_age(),
                "Nationality: ",actor.get_nationality(),
                "Gender: ",actor.get_gender(),
                "url Link: ",actor.get_photo_link(),
                "Rating: ",actor.get_rating(),
            )






def base():
    users = {}
    movies = []
    menu_1(users)
    menu_2(movies)
    menu_3()
    
base()
    



