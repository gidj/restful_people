from typing import List

from storage.models import Person


def _by_gender(people: List[Person]) -> List[Person]:
    def _key(person):
        return person.last_name.lower()

    female = filter(lambda p: p.gender == "female", people)
    male = filter(lambda p: p.gender == "male", people)

    return tuple(sorted(female, key=_key) + sorted(male, key=_key))


def _by_last_name(people: List[Person]) -> List[Person]:
    def _key(person):
        return person.last_name.lower()

    return sorted(people, key=_key)


def _by_birth_date(people: List[Person]) -> List[Person]:
    def _key(person):
        return person.date_of_birth

    return sorted(people, key=_key)
