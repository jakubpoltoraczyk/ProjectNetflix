class Date:
    """Class, which represents date in format: 'DD.MM.YYYY'"""

    __enum_days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    """ Enumeration dictionary for appropriate number of days in every month

    The key is a month as an integer, the value is number of days in specified month"""

    def __init__(self, day, month, year):
        """Construct new Date object

        Params:
            day (int): Number to set as a day
            month (int): Number to set as a month
            year (int): Number to set as a year"""
        self.__day = self.__month = self.__year = None
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)

    def set_day(self, day):
        """Set new day

        Args:
            day (int): New day, which will be set"""
        if self.__validate_day(day):
            self.__day = day
        else:
            # todo: Replace print with exception
            print("Incorrect day number")

    def set_month(self, month):
        """Set new month

        Args:
            month (int): New month, which will be set"""
        if self.__validate_month(month):
            self.__month = month
        else:
            # todo: Replace print with exception
            print("Incorrect month number")

    def set_year(self, year):
        """Set new year

        Args:
            year (int): New year, which will be set"""
        if self.__validate_year(year):
            self.__year = year
        else:
            # todo: Replace print with exception
            print("Incorrect year number")

    def get_day(self):
        """Provide day

        Returns:
            Day as a number appropriate to current month"""
        return self.__day

    def get_month(self):
        """Provide month

        Returns:
            Month as a number from 1 to 12"""
        return self.__month

    def get_year(self):
        """Provide year

        Returns:
            Year as a number from 2000 to 2022"""
        return self.__year

    def get_whole_date(self):
        """Provide a date as a string in format: 'DD.MM.YYYY'

        Returns:
            Date as a string"""
        whole_date = ("0" if self.__day < 10 else "")
        whole_date += str(self.__day) + "."
        whole_date += ("0" if self.__month < 10 else "")
        whole_date += str(self.__month) + "."
        whole_date += str(self.__year)
        return whole_date

    def __validate_day(self, day):
        """Check if given day is correct for current selected month"""
        if 1 <= day <= self.__enum_days_in_month.get(self.__month):
            return True
        return False

    def __validate_month(self, month):
        """Check if month is a number between 1 to 12

        Returns:
            True if month number is correct, otherwise false"""
        if 1 <= month <= 12:
            return True
        return False

    def __validate_year(self, year):
        """Check if year is a number between 2000 to 2022

        Returns:
            True if year number is correct, otherwise false"""
        if 2000 <= year <= 2022:
            return True
        return False
