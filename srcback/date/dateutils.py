from date import Date


class DateUtils:
    """Class, which contains some utils for date objects in form of static methods

    It's desirable to not create instance of this class, due to it only has some static methods and object of this class will be useless"""

    def __init__(self):
        """Empty constructor, which does nothing"""
        pass

    @staticmethod
    def get_younger(first_date, second_date):
        """Compare two dates and return the younger one

        Args:
            first_date (Date): First date to compare
            second_date (Date): Second date to compare

        Returns:
            If dates are equal return first date, otherwise return the younger one
        """
        if first_date.get_whole_date == second_date.get_whole_date:
            return first_date

        first_value = first_date.get_year()
        second_value = second_date.get_year()
        if first_value != second_value:
            return first_date if first_value > second_value else second_date

        first_value = first_date.get_month()
        second_value = second_date.get_month()
        if first_value != second_value:
            return first_date if first_value > second_value else second_date

        first_value = first_date.get_day()
        second_value = second_date.get_day()
        return first_date if first_value > second_value else second_date

    @staticmethod
    def get_older(first_date, second_date):
        """Compare two dates and return the older one

        Args:
            first_date (Date): First date to compare
            second_date (Date): Second date to compare

        Returns:
            If dates are equal return first date, otherwise return the older one
        """
        younger_date = DateUtils.get_younger(first_date, second_date)
        return first_date if younger_date == second_date else second_date

    @staticmethod
    def get_difference_in_years(first_date, second_date):
        """Provide difference between two dates as number of years

        Args:
            first_date (Date): First date to compare
            second_date (Date): Second date to compare

        Returns:
            Difference in two dates in years as an integer value
        """
        return abs(first_date.get_year() - second_date.get_year())

    @staticmethod
    def are_equal(first_date, second_date):
        """Check if two dates are equal or not

        Args:
            first_date (Date): First date to compare
            second_date (Date): Second date to compare

        Returns:
            True if date are equals, otherwise false
        """
        return (
            True
            if first_date.get_whole_date() == second_date.get_whole_date()
            else False
        )
