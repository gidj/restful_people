from typing import Callable, Tuple

from storage.models import Person

BIRTH_DATE = "birthdate"
GENDER = "gender"
LAST_NAME = "last_name"


def _by_gender(people: Tuple[Person]) -> Tuple[Person]:
    def _key(person):
        return person.last_name.lower()

    female = filter(lambda p: p.gender == "female", people)
    male = filter(lambda p: p.gender == "male", people)

    return tuple(sorted(female, key=_key) + sorted(male, key=_key))


def _by_last_name(people: Tuple[Person]) -> Tuple[Person]:
    def _key(person):
        return person.last_name.lower()

    return sorted(people, key=_key)


def _by_birth_date(people: Tuple[Person]) -> Tuple[Person]:
    def _key(person):
        return person.date_of_birth

    return sorted(people, key=_key)


class SortingElementNotFoundException(Exception):
    pass


def sort_people_by(sort_element: str, people: Tuple[Person]):
    return people_sorter(sort_element)(people)


def people_sorter(sort_element: str) -> Callable[[Tuple[Person]], Tuple[Person]]:
    _sort_dict = {
        BIRTH_DATE: _by_birth_date,
        GENDER: _by_gender,
        LAST_NAME: _by_last_name,
    }

    try:
        _sort_function = _sort_dict[sort_element]
    except KeyError:
        raise SortingElementNotFoundException()

    return _sort_function
