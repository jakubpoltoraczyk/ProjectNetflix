from date import Date
from dateutils import DateUtils
from director import Director
import datetime

now = datetime.datetime.now()


class Movie:
    """Class, which represents movie object with some basic information"""

    def __init__(self, actors, director, description, release_date, rating):
        """Create new movie object

        Params:
            actors (list): List of actors, which appeared in the movie
            director (Director): Director of the movie
            description (MovieDescription): Description of the movie
            release_date (Date): Date of release the movie
            rating (int): Rating of the movie
        """
        self.__actors = actors
        self.__director = director
        self.__description = description
        self.__release_date = release_date
        self.__rating = rating

    def get_number_of_actors(self):
        """Provide number of actors at the list of actors

        Returns:
            Number of actors at the list of actors
        """
        return len(self.__actors)

    def get_actor(self, index):
        """Provide actor at the selected position from the list of actors

        Params:
            index (int): Actor position at the list of actors
        
        Returns:
            actors[index]: One element from list of Actors objects, which holds information about actor
        """
        if 0 <= index < len(self.__actors):
            return self.__actors[index]
        else:
            print("Incorrect index number:", index)

    def add_new_actor(self, actor):
        """Add new actor to the list of actors

        Params:
            actor (Actor): New actor, which will be added
        """
        self.__actors.append(actor)

    def remove_actor(self, index):
        """Remove actor at the selected position from the list of actors

        Params:
            index (int): Actor position at the list of actors
        """
        if 0 <= index < len(self.__actors):
            self.__actors.pop(index)
        else:
            print("Incorrect index number:", index)

    def get_director(self):
        """Provide a director
        Returns:

            director : Instance of Director class, which holds information about movie director"""
        return self.__director

    def change_director(self, director):
        """Change the main director of movie
        Args:

            director : instance of Director class, give personal data about new director
        """
        self.__director = director

    def get_description(self):
        """Provide a description
        Returns:

            description : object of moviedescription class, contains title and description of movie"""
        return self.__description

    def change_description(self, description):
        """Change description of movie
        Args:

            description : object of moviedescription class, contains title and description of movie"""
        self.__description = description

    def get_release_date(self):
        """Provide a date of movie premiere
        Returns:

            A date of premiere"""
        return self.__release_date

    def update_release_date(self, release_date):
        """Update a release date
        Args:

            release_date: object of Date class, contains a date of premiere"""
        self.__release_date = release_date

    def get_insist_age(self):
        """Provide an age of movie
        Returns:

            age of movie"""
        return DateUtils.get_difference_in_years(
            Date(now.day, now.month, now.year), self.get_release_date
        )

    def get_rating(self):
        """Provide a rating of movie
        Returns:

            a rating of movie"""
        return self.__rating

    def change_rating(self, rating):
        """Change rating of movie
        Args:

            rating(int): rating of movie"""
        if self.__validate_rating(rating):
            self.__rating = rating
        else:
            print("incorrect value")
        

    def __validate_rating(self, rating):
        """Check if rating is a number between 0 and 10
        Returns:

            True if yes, otherwise False"""
        if 0 <= rating <= 10:
            return True
        return False
