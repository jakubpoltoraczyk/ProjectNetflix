class Person(object):
    """Class which give us the most important information about a person"""

    def __init__(self, name, surname, nationality, age, gender, photo_link):
        """Contains basic information about this person

        Params:
            name : the name of this person writing capital letter
            surname: the surname of person writing capital letter
            nationality : nationality writing capital letter where she/he live
            age(int) : the age of this person
            gender : the gender of this person
            photo_link_link : url link image of this person
        """
        self.__name = name.capitalize()
        self.__surname = surname.capitalize()
        self.__nationality = nationality.capitalize()
        self.__age = age
        self.__gender = gender
        self.__photo_link = photo_link

    def get_name(self):
        """Provide name

        Returns:
            the name of person"""
        return self.__name

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

    def get_age(self):
        """Provide age

        Returns:
            the age of this person"""
        return self.__age

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
            self.__name = surname.capitalize()

    def set_nationality(self, nationality):
        """Change the nationality

        Args:
            nationality : new nationality which will be set"""
        self.__nationality = nationality.capitalize()

    def set_age(self, age):
        """Change the age

        Args:
            age : new age which will be set"""
        if self.__validate_age(age):
            self.__age = age

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

    def __validate_age(self, age):
        """Check if age value is bigger than 0

        Returns:
            True if age > 0, otherwise false"""
        if 120 > age > 0:
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
    name = ""
    age = 0
    gender = "xx"
    surname = ""
    while name == "":
        name = input("Write the name of the person: ")
    while surname == "":
        surname = input("Write the surname of the person: ")
    nationality = input("Write the nationality where they were born: ")
    while age <= 0:
        try:
            age = int(input("Write the age of the person: "))
        except ValueError:
            print("Give correct value")

    while gender not in ["male", "female"]:
        gender = input("Write the gender of the person: ")
    photo_link = input("Add photo_link link of the person: ")
    people.append(Person(name, surname, nationality, age, gender, photo_link))
