from moviedescription import MovieDescription, new_object


def main():
    movies = {}
    click_01 = None
    click_02 = None
    click_03 = None
    new_object(movies)
    while click_01 != 0:
        print(
            """
        1 - add new movie
        2 - saw information about movie
        3 - change information about movie
        0 - exit
        """
        )
        click_01 = int(input("Write which option you choose: "))
        if click_01 == 1:
            new_object(movies)
        elif click_01 == 2:

            for x in movies:
                print(x + 1, "-", movies[x].get_title())
            click_02 = int(input("Write which one do you choose: "))
            print("Title: ", movies[click_02 - 1].get_title())
            print("Short description: ", movies[click_02 - 1].get_short_description())
            print("Long description: ", movies[click_02 - 1].get_long_description())
        elif click_01 == 3:
            for x in movies:
                print(x + 1, "-", movies[x].get_title())
            click_02 = int(input("Write the number of movie which you want to update: "))
            print("""
            1 - change the title
            2 - change short information
            3 - change long information""")
            click_03 = int(input("Write which aspect you want to change: "))
            if click_03 ==1:
                title = input("Write new title: ")
                movies[click_02-1].set_title(title)
            if click_03 ==2:
                short_description = input("Write new short description: ")
                movies[click_02-1].short_description(short_description)
            if click_03 ==3:
                long_description = input("Write new long description: ")
                movies[click_02-1].set_long_description(long_description)
                

main()
