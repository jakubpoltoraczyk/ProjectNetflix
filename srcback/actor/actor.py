from sys import path
from os import getcwd
from pathlib import Path

path.append(str(Path(getcwd()).parent.absolute()) + "/person")

from personalinformation import Person, Date, now


class Actor(Person):
    """Class, which represents actor

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
            date_of_death:  the date of death of this person
        """
        super().__init__(
            name, surname, nationality, date_of_birth, gender, photo_link, date_of_death
        )
        self.__rating = rating

    def get_rating(self):
        """Provide rating of acting

        Returns:
            Rating of acting as a number from 0 to 10"""
        return self.__rating

    def set_rating(self, rating):
        """Set rating of the acting

        Args:
            rating(double): New rating as a number from 0 to 10"""
        if 0 <= rating <= 10:
            self.__rating = rating
        else:
            print("Incorrect rating")
