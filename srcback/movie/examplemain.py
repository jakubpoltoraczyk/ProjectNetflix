from sys import path
from os import getcwd
from pathlib import Path

path.append(str(Path(getcwd()).parent.absolute()) + "/actor")
path.append(str(Path(getcwd()).parent.absolute()) + "/director")
path.append(str(Path(getcwd()).parent.absolute()) + "/moviedescription")

from actor import Actor
from director import Director
from moviedescription import MovieDescription
from date import Date
from movie import Movie

def display_every_actor_dataset(movie):
    for index in range(movie.get_number_of_actors()):
        actor = movie.get_actor(index)
        print(actor.get_name(), actor.get_surname(), actor.get_age(), actor.get_nationality(), actor.get_gender(), actor.get_photo_link(), actor.get_rating())


def main():
    actors = [
        Actor(
            "Jan", "Kowalski", "Polska", Date(10, 12, 1978), "male", "some-link.pl", 6.5),
        Actor(
            "Joanna", "Wiosenna", "Polska", Date(12, 5, 1991), "female", "some-link.com", 7.0,),
        Actor(
            "John", "Kitchen", "USA", Date(10,9,1951), "male", "johnjohn-kitchen.com", 4.1, Date(30,12,2009)
        )]

    movie = Movie(actors)

    print("At the beginning:")
    display_every_actor_dataset(movie)
    
    movie.remove_actor(1)
    
    print("\nAt the end:")
    display_every_actor_dataset(movie)

main()