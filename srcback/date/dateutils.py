from date import Date

class DateUtils:
    """Class, which contains some utils for date objects in form of static methods

    It's desirable to not create instance of this class, due to it only has some static methods and object of this class will be useless"""

    def __init__(self):
        """Empty constructor, which does nothing"""
        pass
    
    @staticmethod
    def get_younger(first_date, second_date):
        """ Compare two dates and return the younger one

        Args:
            first_date (Date): first date to compare
            second_date (Date): second date to compare
        
        Returns:
            If date are equal return first date, otherwise return the younger one
        """
        if first_date.get_whole_date == second_date.get_whole_date:
            return first_date

        first_value = first_date.get_year()
        second_value = second_date.get_year()
        if first_value != second_value:
            return (first_date if first_value > second_value else second_date)

        first_value = first_date.get_month()
        second_value = second_date.get_month()
        if first_value != second_value:
            return (first_date if first_value > second_value else second_date)

        first_value = first_date.get_day()
        second_value = second_date.get_day()
        return (first_date if first_value > second_value else second_date)
