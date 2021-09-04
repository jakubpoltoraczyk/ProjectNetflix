class Movie:
    """Class, which represents movie object with some basic information"""

    def __init__(self, actors):
        """Create new movie object

        Params:
            actors (list): List of actors, which appeared in the movie
            director (Director): Director of the movie
            description (MovieDescription): Description of the movie
            release_date (Date): Date of release the movie
            rating (int): Rating of the movie
        """
        self.__actors = actors
        #self.__director = director
        #self.__descrption = description
        #self.__release_date = release_date
        #self.__rating = rating

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
