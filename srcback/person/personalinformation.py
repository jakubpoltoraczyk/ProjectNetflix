
class Person(object):
    def __init__(self, name, surname, country, age, appearance, gender, photo):
        self.__name = name.capitalize()
        self.__country = country.capitalize()
        self.__age = age
        self.__appearance = appearance
        self.__gender = gender
        self.__photo = photo
        self.__surname = surname.capitalize()
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_country(self):
        return self.__country
    def get_age(self):
        return self.__age
    def get_appearance(self):
        return self.__appearance
    def get_gender(self):
        return self.__gender
    def get_photo(self):
        return self.__photo
    def set_name(self, name):
        if self.__validate_name(name):
            self.__name = name.capitalize()
    def set_surname(self, surname):
        if self.__validate_name(surname):
            self.__name = surname.capitalize()
    def set_country(self, country):
        self.__country = country.capitalize()
    def set_age(self, age):
        if self.__validate_age(age):
            self.__age = age
    def set_appearance(self, appearance):
        self.__appearance = appearance
    def set_gender(self, gender):
        if self.__validate_gender(gender):
            self.__gender = gender
    def set_photo(self, photo):
        self.__photo = photo
    def __validate_name(self, name):
        if name != "":
            return True
        return False
    def __validate_name(self, surname):
        if surname != "":
            return True
        return False
    def __validate_age(self, age):
        if age >0:
            return True
        return False
    def __validate_gender(self, gender):
        if gender in ("male", "female"):
            return True
        return False

def add_person(people):
    name = ""
    age = 0
    gender = "xx"
    surname = ""
    while name == "":
        name = input("Write the name of the person: ")
    while surname == "":
        surname = input("Write the surname of the person: ")
    country= input("Write the country where they were born: ")
    while age <=0:
        try:
            age= int(input("Write the age of the person: "))
        except ValueError:
            print("Give correct value")

    appearance= input("Write all apearances in movies of the person: ")
    while gender not in ["male", "female"]:
        gender= input("Write the gender of the person: ")
    photo= input("Add photo link of the person: ")
    people[len(people)]= Person(name, surname, country, age, appearance, gender, photo)


