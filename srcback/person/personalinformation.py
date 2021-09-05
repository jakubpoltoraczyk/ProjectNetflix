from sys import path
from os import getcwd
from pathlib import Path

path.append(str(Path(getcwd()).parent.absolute()) + "/date")

import datetime
from dateutils import DateUtils
from date import Date

now = datetime.datetime.now()

class Person(object):
    """Class which give us the most important information about a person"""

    def __init__(
        self,
        name,
        surname,
        nationality,
        date_of_birth,
        gender,
        photo_link,
        date_of_death = Date(now.day, now.month, now.year)
    ):
        """Contains basic information about this person

        Params:
            name : the name of this person writing capital letter
            surname: the surname of person writing capital letter
            nationality : nationality writing capital letter where she/he live
            date_of_birth:  the date of birth of this person
            gender : the gender of this person
            photo_link_link : url link image of this person
            date_of_death:  the date of death of this person
        """
        self.__name = self.__surname = self.__nationality = self.__date_of_birth = self.__gender = self.__photo_link = None
        self.__date_of_death = date_of_death
        self.set_name(name)
        self.set_surname(surname)
        self.set_nationality(nationality)
        self.set_date_of_birth(date_of_birth, date_of_death)
        self.set_date_of_death(date_of_birth, date_of_death)
        self.set_gender(gender)
        self.set_photo_link(photo_link)

    def get_name(self):
        """Provide name

        Returns:
            the name of person"""
        return self.__name

    def get_age(self):
        """Provide age

        Returns:
            the age of person"""
        age = DateUtils.get_difference_in_years(self.__date_of_death, self.__date_of_birth)
        return age

    def get_surname(self):
        """Provide surname

        Returns:
            the surname of person"""
        return self.__surname

    def get_nationality(self):
        """Provide nationality

        Returns:
            the nationality of this person"""
        return self.__nationality

    def get_date_of_birth(self):
        """Provide age

        Returns:
            the date of birth of this person"""
        return Date.get_whole_date(self.__date_of_birth)

    def get_date_of_death(self):
        """Provide age

        Returns:
            the date of death of this person, if he is still alive, return print still alive"""
        if DateUtils.are_equal(self.__date_of_death, Date(now.day, now.month, now.year)):
            return "still alive"
        return Date.get_whole_date(self.__date_of_death)

    def get_gender(self):
        """Provide gender

        Returns:
            gender of this person"""
        return self.__gender

    def get_photo_link(self):
        """Provide photo link

        Returns:
            the url photo link of this person"""
        return self.__photo_link

    def set_name(self, name):
        """Change the name

        Args:
            name : new name which will be set"""
        if self.__validate_name(name):
            self.__name = name.capitalize()

    def set_surname(self, surname):
        """Change the surname

        Args:
            surname : new surname which will be set"""
        if self.__validate_surname(surname):
            self.__surname = surname.capitalize()

    def set_nationality(self, nationality):
        """Change the nationality

        Args:
            nationality : new nationality which will be set"""
        self.__nationality = nationality.capitalize()

    def set_date_of_birth(self, date_of_birth, date_of_death):
        """Change the date of birth
        Args:
            date_of_birth  : new date of birth  which will be set"""
        if self.__validate_date_of_birth_and_death(date_of_birth, date_of_death):
            self.__date_of_birth = date_of_birth

    def set_date_of_death(self, date_of_birth, date_of_death):
        """Change the date of death

        Args:
            date_of_death  : new date of death  which will be set"""
        if self.__validate_date_of_birth_and_death(date_of_birth, date_of_death):
            self.__date_of_death = date_of_death

    def set_gender(self, gender):
        """Change the gender, only allows to use strings : "male", "female"

        Returns:
            gender : new gender which will be set"""
        if self.__validate_gender(gender):
            self.__gender = gender

    def set_photo_link(self, photo_link):
        """Change the photo_link

        Args:
            photo_link : new url photos link which will be set"""
        self.__photo_link = photo_link

    def __validate_name(self, name):
        """Check if name isn't empty

        Returns:
            True if name isn't empty, otherwise false"""
        if name != "":
            return True
        return False

    def __validate_surname(self, surname):
        """Check if surname isn't empty

        Returns:
            True if surname isn't empty, otherwise false"""
        if surname != "":
            return True
        return False

    def __validate_date_of_birth_and_death(self, date_of_birth, date_of_death):
        """Check if date of birth was before date of death(if it was)

        Returns:
            True if date of birth was before date of death, otherwise false"""
        if DateUtils.get_younger(date_of_birth, date_of_death) == date_of_birth:
            return True
        return False

    def __validate_gender(self, gender):
        """Check if gender is male or female

        Returns:
            True if gender is one of male or female, otherwise false"""
        if gender in ("male", "female"):
            return True
        return False


def add_person(people):
    """Create a new object of Person Class.

    Args:
        people: a list of actors and directorss"""
    gender = "xx"
    name = input("Write the name of the person: ")
    surname = input("Write the surname of the person: ")
    nationality = input("Write the nationality where they were born: ")
    day = int(input("Write day of birth: "))
    month = int(input("Write month of birth: "))
    year = int(input("Write year of birth: "))
    date_of_birth = Date(day, month, year)
    while gender not in ["male", "female"]:
        gender = input("Write the gender of the person: ")
    photo_link = input("Add photo_link link of the person: ")
    is_dead = input("Are they dead? Answer using 'yes' or 'no'")
    if is_dead == "yes":
        day = int(input("Write day of death: "))
        month = int(input("Write month of death: "))
        year = int(input("Write year of death: "))
        date_of_death = Date(day, month, year)
        people.append(
            Person(
                name, surname, nationality, date_of_birth, gender, photo_link, date_of_death
            ))
    else:
        people.append(Person(name, surname, nationality, date_of_birth, gender, photo_link))
