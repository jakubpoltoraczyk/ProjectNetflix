from sys import path
from os import getcwd
from pathlib import Path

path.append(str(Path(getcwd()).parent.absolute()) + "/person")
from personalinformation import Person, add_person
path.append(str(Path(getcwd()).parent.absolute()) + "/date")
from date import Date
path.append(str(Path(getcwd()).parent.absolute()) + "/movieandseries")
from baseformovieandseries import Base_movie_and_series, add_movie


def main():
    people = []
    add_movie(people)

main()