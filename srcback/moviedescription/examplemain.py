from moviedescription import MovieDescription, new_object


def main():
    movies = {}
    click_01 = None
    click_02 = None
    new_object(movies)
    while click_01 != 0:
        print(
            """
        1 - add new movie
        2 - saw information about movie
        0 - exit
        """
        )
        click_01 = int(input("Write which option you choose: "))
        if click_01 == 1:
            new_object(movies)
        elif click_01 == 2:

            for x in movies:
                print(x + 1, "-", movies[x].get_name())
            click_02 = int(input("Write which one do you choose: "))
            print("Title: ", movies[click_02 - 1].get_name())
            print("Short description: ", movies[click_02 - 1].get_short_description())
            print("Long description: ", movies[click_02 - 1].get_long_description())


main()
