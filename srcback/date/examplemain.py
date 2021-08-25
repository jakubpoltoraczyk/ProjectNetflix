from date import Date
from dateutils import DateUtils


def main():
    first_date = Date(4, 6, 2020)
    second_date = Date(11, 8, 2018)

    print("At the beginning:")
    print("First date:", first_date.get_whole_date())
    print("Second_date:", second_date.get_whole_date())

    value = int(input("\nSet new year of first date: "))
    first_date.set_year(value)

    value = int(input("Set new day of second date: "))
    second_date.set_day(value)

    print("\nAt the end:")
    print("First date:", first_date.get_whole_date())
    print("Second_date:", second_date.get_whole_date())

    print(
        "\nYounger date:",
        DateUtils.get_younger(first_date, second_date).get_whole_date(),
    )
    print("Older date:", DateUtils.get_older(first_date, second_date).get_whole_date())
    print(
        "Difference between dates:",
        DateUtils.get_difference_in_years(first_date, second_date),
        "year(s)",
    )


main()
