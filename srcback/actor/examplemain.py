from actor import Actor, Person
from date import Date

def main():
    actor = Actor("Piotr", "Kowalski", "Poland", Date(10,11,1980), "male", "some_link", 6.6)
    actor.set_rating(float(input("Write new rating: ")))
    print("Name:", actor.get_name(), actor.get_surname())
    print("Age:", actor.get_age())
    print("Rating:", actor.get_rating())


main()
