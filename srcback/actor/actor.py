from sys import path
from os import getcwd
from pathlib import Path

path.append(str(Path(getcwd()).parent.absolute()) + "/person")

from personalinformation import Person


class Actor(Person):
    """Class, which represents actor

    This is derived class, which inherits from Person base class"""

    def __init__(self, name, surname, nationality, age, gender, photo_link, rating):
        """Contains basic information about actor

        Params:
            name : the name of this person writing capital letter
            surname: the surname of person writing capital letter
            nationality : nationality writing capital letter where she/he live
            age(int) : the age of this person
            gender : the gender of this person
            photo_link_link : url link image of this person
            rating(double): rating of acting
        """
        super().__init__(name, surname, nationality, age, gender, photo_link)
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
