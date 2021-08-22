from date import Date


def main():
    first_date = Date(10, 12, 2010)
    second_date = Date(15, 10, 2018)

    print("First date day:", first_date.get_day())
    print("Second date year:", second_date.get_year())

    day = int(input("Set new first date day:"))
    year = int(input("Set new second date year:"))
    first_date.set_day(day)
    second_date.set_year(year)

    print("First date day:", first_date.get_day())
    print("Second date year:", second_date.get_year())

    print("Whole first date:", first_date.get_whole_date())
    print("Whole second date:", second_date.get_whole_date())


main()
