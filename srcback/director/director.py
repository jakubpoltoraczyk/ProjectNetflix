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
        number_of_movies,
        date_of_death=Date(now.day, now.month, now.year),
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
        """
        super().__init__(
            name, surname, nationality, date_of_birth, gender, photo_link, date_of_death
        )
        rating = efficienty = None
        self.set_rating(rating)
        self.set_efficienty(efficienty)
        self.set_number_of_movies(number_of_movies)

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

    def get_number_of_movies(self):
        """Provide number of movies directed by director

        Returns:
            Number of movies directed by director"""
        return self.__number_of_movies
        
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
        efficienty = float(self.__number_of_movies / super().get_age())

    def set_number_of_movies(self, number_of_movies):
        """Set new number of movies which this director has directed

        Args:
            movies(int): New value od movies"""
        self.__number_of_movies = number_of_movies
