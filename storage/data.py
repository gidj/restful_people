from typing import List

from storage.models import Person


class DataService(object):
    def __init__(self):
        self._storage = set()

    def insert(self, person: Person) -> None:
        self._storage.add(person)

    def get_all(self) -> List[Person]:
        return tuple(self._storage)
