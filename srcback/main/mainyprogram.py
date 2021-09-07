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
    if click =="yes":
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
    rating = float(input("Write your own mark of this movie: "))
    if 0 <= rating <= 10:
        return rating
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
    click = input("Write yes if you want to add new actor to the list: ")
    if click == "yes":
        __actor = Actor(add_name(), add_surname(), add_nationality(), add_date_of_birth(), add_gender(), add_photo_link(), add_rating(), add_date_of_death())
        return __actor
        create_actor()

def create_description():
    __description = MovieDescription(add_title(), add_short_description(), add_long_description())
    return __description

def create_director():
    __director = Director(add_name(), add_surname(), add_nationality(), add_date_of_birth(), add_gender(), add_photo_link(), add_rating(), add_number_of_movies(), add_date_of_death())
    return __director

def create_movie(movies):
    movie = Movie([], create_director(), create_description(), add_release_date(), add_rating())
    movie.add_new_actor(create_actor())