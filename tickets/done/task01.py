class Movie(object):
    def __init__(
        self,
        name,
        movie_short_description = "",
        movie_long_description = ""
    ):
        self.__name = name
        self.__movie_short_description = movie_short_description
        self.__movie_long_description = movie_long_description
    def add_movie_short_description(self):
        self.__movie_short_description = input("Write a short description of this movie: ")
    def add_movie_long_description(self):
        self.__movie_long_description = input("Write a expanded description of this movie: ")
    def get_movie_short_description(self):
        return self.__movie_short_description
    def get_movie_long_description(self):
        return self.__movie_long_description
    def new_object(movies):
        movie_name = input("Give a titel of your last watched movie: ")
        movies[len(movies)] = Movie(movie_name)
        

