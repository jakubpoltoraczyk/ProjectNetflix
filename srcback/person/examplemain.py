from personalinformation import Person, add_person, now


def main():
    people = []
    add_person(people)
    for x in people:
        print(x.get_gender())
        print(x.get_name())
    name = input("Write new name: ")
    people[0].set_name(name)
    print(people[0].get_name())
    print(people[0].get_age())
    #print(people[0].get_date_of_death(date_of_death))


main()
