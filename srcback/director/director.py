from sys import path
from os import getcwd
from pathlib import Path

path.append(str(Path(getcwd()).parent.absolute()) + "/person")

from personalinformation import Person


class Director(Person):
    """Class, which represents director
    This is derived class, which inherits from Person base class"""

    def __init__(
        self,
        name,
        surname,
        nationality,
        date_of_birth,
        gender,
        photo_link,
        rating,
        efficienty,
        date_of_death = Date(now.day, now.month, now.year),
        movie=[],
    ):
        """Contains basic information about actor
        Params:
            name : the name of this person writing capital letter
            surname: the surname of person writing capital letter
            nationality : nationality writing capital letter where she/he live
            date_of_birth:  the date of birth of this person
            gender : the gender of this person
            photo_link_link : url link image of this person
            rating(float): rating of acting
            efficienty(float): the average value of directed films in one year
            date_of_death:  the date of death of this person
            movie: List of movies
        """
        super().__init__(name, surname, nationality, date_of_birth, gender, photo_link, date_of_death)
        rating = efficienty = None
        self.set_rating(rating)
        self.set_efficienty(efficienty)
        self.set_movie(movie)

    def get_rating(self):
        """Provide rating of director
        Returns:
            Rating of director as a number from 0 to 10"""
        return self.__rating

    def get_efficienty(self):
        """Provide value of efficienty
        Returns:
            The average value of directed films in one year"""
        return self.__efficienty

    def get_movie(self):
        """Provide movies directed by this director
        Returns:
            List of movies"""
        return self.__movie

    def set_rating(self, rating):
        """Set rating of the acting
        Args:
            rating(float): New rating as a number from 0 to 10"""
        if 0 <= rating <= 10:
            self.__rating = rating
        else:
            print("Incorrect rating")

    def set_efficienty(self, efficienty):
        """Set value of efficienty
        Args:
            efficienty(float): New value of efficienty"""
        efficienty = float(len(self.get_movie()) / super().get_age())

    def set_movie(self, movie):
        """Set movies directed by this director
        Args:
            movie: List of movies"""
        for x in movies:
            print(x + 1, "-", movies[x].get_title())
        click = int(input("Which one did this director direct? "))
        movie.append(movies[x])
