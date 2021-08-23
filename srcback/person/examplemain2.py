from personalinformation import Person, add_person


def main():
    people = {}
    add_person(people)
    for x in people:
        print(people[x].get_gender())
        print(people[x].get_name())
    name = input("Write new name: ")
    age = int(input("Write new value of age"))
    people[0].set_name(name)
    people[0].set_age(age)
    print(people[0].get_name())
    print(people[0].get_age())

main()