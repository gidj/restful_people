import unittest

from util.parser import Person

from .data import DataService


class TestDataService(unittest.TestCase):
    PERSON_1 = ("Adams", "Adam", "male", "red", "4/7/2000")
    PERSON_2 = ("Stewart", "Patrick", "male", "cyan", "2/17/1970")

    def test_insert_one_record(self):
        service = DataService()
        person = Person(*self.PERSON_1)

        service.insert(person)

        people = service.get_all()
        stored_person = people[0]

        self.assertEqual(len(people), 1)
        self.assertEqual(person, stored_person)

    def test_insert_two_records(self):
        service = DataService()
        person_1 = Person(*self.PERSON_1)
        person_2 = Person(*self.PERSON_2)

        people_before = (person_1, person_2)

        service.insert(person_1)
        service.insert(person_2)

        people_after = service.get_all()

        self.assertEqual(len(people_after), 2)
        for person in people_before:
            self.assertIn(person, people_after)

    def test_inserting_same_person_does_not_duplicate(self):
        service = DataService()
        person = Person(*self.PERSON_1)

        service.insert(person)
        service.insert(person)

        people_after = service.get_all()
        stored_person = people_after[0]

        self.assertEqual(len(people_after), 1)
        self.assertEqual(person, stored_person)

