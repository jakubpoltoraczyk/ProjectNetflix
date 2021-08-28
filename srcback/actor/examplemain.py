from actor import Actor

def main():
    actor = Actor("Piotr", "Kowalski", "Poland", 54, "male", "some_link", 6.5)
    actor.set_rating(float(input("Write new rating:")))
    print("Name:", actor.get_name(), actor.get_surname())
    print("Age:", actor.get_age())
    print("Rating:", actor.get_rating())

main()