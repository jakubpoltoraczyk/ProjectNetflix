class MovieDescription(object):
    def __init__(self, name, short_description, long_description):
        self.__name = name
        self.__short_description = short_description
        self.__long_description = long_description

    def get_short_description(self):
        return self.__short_description

    def get_long_description(self):
        return self.__long_description

    def get_name(self):
        return self.__name


def new_object(movies):
    name = input("Give a title of your last watched movie: ")
    short_description = input("Write a short description of this movie: ")
    long_description = input("Write a expanded description of this movie: ")
    movies[len(movies)] = MovieDescription(name, short_description, long_description)
