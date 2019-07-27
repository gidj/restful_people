import io
import random
import unittest
from datetime import datetime

from util.parser import FileParser, LineParseException, LineParser, Person


class TestFileParser(unittest.TestCase):
    PERSON_1 = ("Adams", "Adam", "male", "red", "4/7/2000")
    PERSON_2 = ("Stewart", "Patrick", "male", "cyan", "2/17/1970")
    PERSON_3 = ("Zipperman", "Petunia", "female", "blue", "12/27/1990")

    def _build_test_file(self, delimiter: str):
        data = [self.PERSON_1, self.PERSON_2, self.PERSON_3]
        random.shuffle(data)
        lines = list(map(delimiter.join, data))
        file_data = "\n".join(lines)
        return io.StringIO(file_data)

    def test_people_by_gender(self):
        test_file = self._build_test_file(",")
        file_parser = FileParser(test_file)
        people_list = file_parser.people_by_gender
        self.assertEqual(people_list[0].last_name, self.PERSON_3[0])
        self.assertEqual(people_list[1].last_name, self.PERSON_1[0])
        self.assertEqual(people_list[2].last_name, self.PERSON_2[0])

    def test_people_by_last_name(self):
        test_file = self._build_test_file(",")
        file_parser = FileParser(test_file)
        people_list = file_parser.people_by_last_name
        self.assertEqual(people_list[0].last_name, self.PERSON_1[0])
        self.assertEqual(people_list[1].last_name, self.PERSON_2[0])
        self.assertEqual(people_list[2].last_name, self.PERSON_3[0])

    def test_people_by_birth_date(self):
        test_file = self._build_test_file(",")
        file_parser = FileParser(test_file)
        people_list = file_parser.people_by_birth_date
        self.assertEqual(people_list[0].last_name, self.PERSON_2[0])
        self.assertEqual(people_list[1].last_name, self.PERSON_3[0])
        self.assertEqual(people_list[2].last_name, self.PERSON_1[0])


class TestLineParser(unittest.TestCase):
    LAST_NAME = "LastName"
    FIRST_NAME = "FirstName"
    GENDER = "Gender"
    FAVORITE_COLOR = "FavoriteColor"
    DATE_OF_BIRTH = "9/5/2000"

    TEST = (LAST_NAME, FIRST_NAME, GENDER, FAVORITE_COLOR, DATE_OF_BIRTH)

    def _verify_person_object(self, person: Person):
        self.assertEqual(person.first_name, self.FIRST_NAME)
        self.assertEqual(person.last_name, self.LAST_NAME)
        self.assertEqual(person.gender, self.GENDER)
        self.assertEqual(person.favorite_color, self.FAVORITE_COLOR)
        self.assertEqual(
            person.date_of_birth, datetime.strptime(self.DATE_OF_BIRTH, "%m/%d/%Y")
        )

    def test_commma_line(self):
        test_line = ",".join(self.TEST)
        line_parser = LineParser.parser_with_delimiter(",")
        person = line_parser.parse_line(test_line)
        self._verify_person_object(person)

    def test_space_line(self):
        test_line = " ".join(self.TEST)
        line_parser = LineParser.parser_with_delimiter(" ")
        person = line_parser.parse_line(test_line)
        self._verify_person_object(person)

    def test_pipe_line(self):
        test_line = "|".join(self.TEST)
        line_parser = LineParser.parser_with_delimiter("|")
        person = line_parser.parse_line(test_line)
        self._verify_person_object(person)

    def test_incorrect_delimiter_throws_exception(self):
        test_line = " ".join(self.TEST)
        line_parser = LineParser.parser_with_delimiter("|")

        with self.assertRaises(LineParseException):
            person = line_parser.parse_line(test_line)
