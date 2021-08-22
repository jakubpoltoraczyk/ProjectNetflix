class Movie(object):
    movies = {}
    def __init__(
        self,
        name,
        movie_short_description  ,
        movie_long_description  
    ):
        self.__name = name
        self.__movie_short_description = movie_short_description
        self.__movie_long_description = movie_long_description
    @property
    def get_movie_short_description(self):
        return self.__movie_short_description
    @property
    def get_movie_long_description(self):
        return self.__movie_long_description
    @property
    def get_movie_name(self):
        return self.__name
    def new_object():
        movie_name = input("Give a titel of your last watched movie: ")
        movie_short_description = input("Write a short description of this movie: ")
        movie_long_description = input("Write a expanded description of this movie: ")
        Movie.movies[len(Movie.movies)] = Movie(movie_name, movie_short_description, movie_long_description)

def main():
    click_01 = None
    click_02 = None
    Movie.new_object()
    while click_01 != 0:
        print("""
        1 - add new movie
        2 - saw information about movie
        0 - exit
        """)
        click_01 = int(input("Write which option you choose: "))
        if click_01 == 1:
            Movie.new_object()
        elif click_01 ==2:

            for x in Movie.movies:
                print(x+1, "-", Movie.movies[x].get_movie_name)
            click_02 = int(input("Write which one do you choose: "))
            print("Titel: ", Movie.movies[click_02-1].get_movie_name)
            print("Short description: ", Movie.movies[click_02-1].get_movie_short_description)
            print("Long description: ", Movie.movies[click_02-1].get_movie_long_description)
    
        

main()