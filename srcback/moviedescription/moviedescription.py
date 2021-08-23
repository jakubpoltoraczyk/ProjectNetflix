class MovieDescription(object):
    """Class which give us the most important information about watched movie"""

    def __init__(self, title, short_description, long_description):
        """Contains three basic arguments about movie
        Params:
            title : name of seen movie
            short description : a short summary of movie
            long description : a long summary of movie"""
        self.__title = title
        self.__short_description = short_description
        self.__long_description = long_description

    def set_title(self, title):
        """Change a title
        Args:
            title : new title which will be set"""
        self.__title = title

    def set_long_description(self, long_description):
        """Change a long description
        Args:
            long_description : new long description which will be set"""
        self.__long_description = long_description

    def set_short_description(self, short_description):
        """Change a short description
        Args:
            short_description : new short description which will be set"""
        self.__short_description = short_description

    def get_short_description(self):
        """Provide short description
        Returns:
            a short summary of movie"""
        return self.__short_description

    def get_long_description(self):
        """Provide long description
        Returns:
            a summary of movie in few sentences"""
        return self.__long_description

    def get_title(self):
        """Provide a title
        Returns:
            a title of this movie"""
        return self.__title


def new_object(movies):
    """Create a new object of MovieDescription Class. Used after watching new film."""
    title = input("Give a title of your last watched movie: ")
    short_description = input("Write a short description of this movie: ")
    long_description = input("Write a expanded description of this movie: ")
    movies[len(movies)] = MovieDescription(title, short_description, long_description)
