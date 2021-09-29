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
    month = int(input("Write month of date of release this movie: "))
    year = int(input("Write year of date of release this movie: "))
    release_date = Date(day, month, year)
    return release_date
    
def create_actor():
    print("Add basic information about an actor!\n")
    __actor = Actor(add_name(), add_surname(), add_nationality(), add_date_of_birth(),
        add_gender(), add_photo_link(), add_rating())
    click = input("If actor is still alive click '1'  ")
    if click != "1":
        __actor.set_date_of_death(__actor.get_date_of_birth(),add_date_of_death())
    return __actor

def create_description():
    print("Add basic information about movie!\n")
    __description = MovieDescription(add_title(), add_short_description(), add_long_description())
    return __description

def create_director():
    print("Add basic information about the director!\n")
    __director = Director(add_name(), add_surname(), add_nationality(),
     add_date_of_birth(), add_gender(), add_photo_link(), add_rating(), add_number_of_movies())
    click = input("If director is still alive click '1'  ")
    if click != "1":
        __director.set_date_of_death(__director.get_date_of_birth(),add_date_of_death())
    return __director

def create_movie(movies):
    movie = Movie([], create_director(), create_description(), add_release_date(), add_rating())
    click = None
    click = input("Write no if you want to stop adding new actors to the list: ")
    while click != "no" :
        movie.add_new_actor(create_actor())
        click = input("Write no if you want to stop adding new actors to the list: ")
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
        menu_1(users)

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
        print(sorting(movies))
        global click2
        click2 = int(input("\nWhich one do you choose: "))
    elif click == "0":
        menu_1(users)
    else:
        print("Incorrect choice!")
        menu_2(movies, users)

def menu_3(click2, movies, users):
    print("""
    \t\t\tNETFLIX database MENU
    \n
    1 - Show list of actors
    2 - Show information about director
    3 - Show descriptions about movie
    4 - Get release date
    5 - Get a personal rating of movies
    6 - Change data about movie
    0 - Return

    """)

    click = None
    click = input("What do you choose? Write right number: ")
    if click == "1":
        for index in range(movies[click2-1].get_number_of_actors()):
            actor = movies[click2-1].get_actor(index)
            print(index+1, actor.get_name(), actor.get_surname() )
        chose_actor = int(input("About which actor you want to get information: "))
        actor = movies[click2-1].get_actor(chose_actor-1)
        print(
            "\nName: ",actor.get_name(),
            "\nSurname: ",actor.get_surname(),
            "\nAge: ",actor.get_age(),
            "\nNationality: ",actor.get_nationality(),
            "\nGender: ",actor.get_gender(),
            "\nurl Link: ",actor.get_photo_link(),
            "\nRating: ",actor.get_rating(),
            "\nDate of birth: ",actor.get_date_of_birth().get_whole_date()
        )
        try:
            print("\n", actor.get_date_of_death().get_whole_date())
        except Exception as e:
            print(e)
        menu_3(click2, movies, users)
    elif click == "2":
        print("\t\t\t BASIC INFORMATION ABOUT DIRECTOR:\n")
        director = movies[click2-1].get_director()
        print("\nName: ",director.get_name())
        print("\nSurname: ",director.get_surname()),
        print("\nAge: ",director.get_age()),
        print("\nNationality: ",director.get_nationality()),
        print("\nGender: ",director.get_gender()),
        print("\nurl Link: ",director.get_photo_link()),
        print("\nRating: ",director.get_rating()),
        print("\nDate of birth: ",director.get_date_of_birth().get_whole_date()),
        try:
                print(director.get_date_of_death().get_whole_date())
        except Exception as e:
            print(e)
        print("\nNumber of appearences: ",director.get_number_of_movies()),
        print("\nEfficienty: ",director.get_efficienty(), " movies per annum")
        menu_3(click2, movies, users)
    elif click =="3":
        print("""SHORT AND LONG DESCRIPTION OF MOVIE""")
        print("\nshort: ", movies[click2-1].get_description().get_short_description() )
        print("\nlong: ", movies[click2-1].get_description().get_long_description() )
        menu_3(click2, movies, users)
    elif click =="4":
        print("RELEASE DATE: ", movies[click2-1].get_release_date().get_whole_date())
        menu_3(click2, movies, users)
    elif click =="5":
        print("PERSONAL RATING: ", movies[click2-1].get_rating())
        menu_3(click2, movies, users)
    elif click =="6":
        menu_4(click2, movies, users)
        menu_3(click2, movies, users)
    elif click == "0":
        menu_2(movies, users)
    else:
        print("Incorrect choice!")
        menu_3(click2, movies, users)



def menu_4(click2, movies, users):
    print("""
    \t\t\tCHANGING DATA
    1 - Change information about actors
    2 - Change information about director
    3 - Change description
    4 - Change release date
    5 - Change your rating
    6 - Add next actor
    0 - return
    """)
    click = None
    click = input("What do you choose? Write right number: ")
    if click =="1":
        print("""Writing a number decide which actor do you want to operate on: """)
        for index in range(movies[click2-1].get_number_of_actors()):
            actor = movies[int(click2)-1].get_actor(index)
            print(index, actor.get_name(), actor.get_surname() )
        menu_5(click2, movies, users, actor)

    elif click =="2":
        print("Click ENTER if you want not to change sth!")
        name = input("New name: ")
        if name !="":
            movies[click2-1].get_director().set_name(name)
        surname = input("New surname: ")
        if surname !="":
            movies[click2-1].get_director().set_surname(surname)
        nationality = input("New nationality: ")
        if nationality !="":
            movies[click2-1].get_director().set_nationality(nationality)
        day = input("New day of date of birth: ")
        month = input("New month of date of birth: ")
        year = input("New year of date of birth: ")
        if year !="" and day !="" and  month!="":
            date_of_birth = Date(int(day), int(month), int(year))
        movies[click2-1].get_director().set_date_of_birth(date_of_birth, movies[click2-1].get_director().get_date_of_death())
        day = input("New day of date of death: ")
        month = input("New month of date of death: ")
        year = input("New year of date of death: ")
        if year !="" and day !="" and  month!="":
            date_of_death = Date(int(day), int(month), int(year))
        movies[click2-1].get_director().set_date_of_death(movies[click2-1].get_director().get_date_of_birth(), date_of_death)
        gender = input("New gender: ") 
        if gender !="":
            movies[click2-1].get_director().set_gender(gender)
        photo_link = input("New photo link: ") 
        if photo_link !="":
            movies[click2-1].get_director().set_photo_link(photo_link)
        rating = input("New rating: ")
        if rating !="":
            movies[click2-1].get_director().set_rating(float(rating))
        number_of_movies = input("New name: ")
        if number_of_movies !="":
            movies[click2-1].get_director().set_number_of_movies(int(number_of_movies))

        menu_4(click2, movies, users)

    elif click =="3":
        print("Click ENTER if you want not to change sth!")
        title = input("New name: ")
        if title !="":
            movies[click2-1].get_description().set_title(title)
        short_description = input("New surname: ")
        if short_description !="":
            movies[click2-1].get_description().set_short_description(short_description)
        long_description = input("New surname: ")
        if long_description !="":
            movies[click2-1].get_description().set_long_description(long_description)
        menu_4(click2, movies, users)


    elif click =="4":
        print("Click enter if you don't want to change it")
        day = input("New day of date of release: ")
        if day !="":
            month = input("New month of date of release: ")
        if month !="":
            year = input("New year of date of release: ")
        if year !="":
            release_date = Date(int(day), int(month), int(year))
        movies[click2-1].update_release_date(release_date)
        menu_4(click2, movies, users)

    elif click == "5":
        print("Click enter if you don't want to change it")
        rating = input("Write new rating: ")
        if rating != "":
            movies[click2-1].change_rating(int(rating))
        menu_4(click2, movies, users)
    
    elif click =="6":
        movies[click2-1].add_new_actor(create_actor())
        menu_4(click2, movies, users)

    elif click == "0":
        menu_3(click2, movies, users)
    else:
        print("Incorrect choice!")
        menu_4(click2, movies, users)

def menu_5(click2, movies, users, actor):
    print("Click ENTER if you want not to change sth!")
    a = int(input(""))
    actor = movies[int(click2)-1].get_actor(a-1)
    name = input("New name: ")
    if name !="":
        actor.set_name(name)
    surname = input("New surname: ")
    if surname !="":
        actor.set_surname(surname)
    nationality = input("New nationality: ")
    if nationality !="":
        actor.set_nationality(nationality)
    day = input("New day of date of birth: ")
    month = input("New month of date of birth: ")
    year = input("New year of date of birth: ")
    if year !="" and day !="" and  month!="":
        date_of_birth = Date(int(day), int(month), int(year))
        try:
            actor.set_date_of_birth(date_of_birth, actor.get_date_of_death())
        except:
            actor.set_date_of_birth(date_of_birth, Date(now.day, now.month, now.year))
    else:
        pass
    day = input("New day of date of death: ")
    month = input("New month of date of death: ")
    year = input("New year of date of death: ")
    if year !="" and day !="" and  month!="":
        date_of_death = Date(int(day), int(month), int(year))
        actor.set_date_of_death(actor.get_date_of_birth(), date_of_death)
        
    else:
        pass
    gender = input("New gender: ") 
    if gender !="":
        actor.set_gender(gender)
    photo_link = input("New photo link: ") 
    if photo_link !="":
        actor.set_photo_link(photo_link)
    rating = input("New rating: ")
    if rating !="":
        actor.set_rating(float(rating))
    menu_4(click2, movies, users)

            

def sorting(movies):
    tab1 = []
    tab2 = []
    sort_movie = {}
    for x in movies:
        tab1.append(x.get_description().get_title())
        tab2.append(x.get_rating())
    for x in range(0, len(tab1)):
        for x in range(0,len(tab1)-1):
            if tab2[x]<tab2[x+1]:
                b = tab2[x+1]
                tab2[x+1] = tab2[x]
                tab2[x] = b
                b = tab1[x+1]
                tab1[x+1] = tab1[x]
                tab1[x] = b
                b = movies[x+1]
                movies[x+1] = movies[x]
                movies[x] = b
    for x in range(0, len(tab1)):
        sort_movie[x+1] = (tab1[x],tab2[x])
    return sort_movie

    


def base():
    users = {}
    movies = []
    global click2
    click2 = None
    menu_1(users)
    menu_2(movies, users)
    menu_3(click2, movies, users)
    menu_4(click2, movies, users)
    
base()
    



