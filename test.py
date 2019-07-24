import io
import random
import unittest

from util.parser import FileParser, LineParseException, LineParser


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

    def test_coma_file(self):
        parser = FileParser(self._build_test_file(","))
        print(parser._raw_lines)

    def test_file_generation(self):
        print(self._build_test_file(","))


class TestLineParser(unittest.TestCase):
    LAST_NAME = "LastName"
    FIRST_NAME = "FirstName"
    GENDER = "Gender"
    FAVORITE_COLOR = "FavoriteColor"
    DATE_OF_BIRTH = "DateOfBirth"

    TEST = (LAST_NAME, FIRST_NAME, GENDER, FAVORITE_COLOR, DATE_OF_BIRTH)

    def test_commma_line(self):
        test_line = ",".join(self.TEST)
        line_parser = LineParser.parser_with_delimiter(",")
        person = line_parser.parse_line(test_line)

        assert person.first_name == self.FIRST_NAME
        assert person.last_name == self.LAST_NAME
        assert person.gender == self.GENDER
        assert person.favorite_color == self.FAVORITE_COLOR
        assert person.date_of_birth == self.DATE_OF_BIRTH

    def test_space_line(self):
        test_line = " ".join(self.TEST)
        line_parser = LineParser.parser_with_delimiter(" ")
        person = line_parser.parse_line(test_line)

        assert person.first_name == self.FIRST_NAME
        assert person.last_name == self.LAST_NAME
        assert person.gender == self.GENDER
        assert person.favorite_color == self.FAVORITE_COLOR
        assert person.date_of_birth == self.DATE_OF_BIRTH

    def test_pipe_line(self):
        test_line = "|".join(self.TEST)
        line_parser = LineParser.parser_with_delimiter("|")
        person = line_parser.parse_line(test_line)

        self.assertEqual(person.first_name, self.FIRST_NAME)
        self.assertEqual(person.last_name, self.LAST_NAME)
        self.assertEqual(person.gender, self.GENDER)
        self.assertEqual(person.favorite_color, self.FAVORITE_COLOR)
        self.assertEqual(person.date_of_birth, self.DATE_OF_BIRTH)

    def test_incorrect_delimiter_throws_exception(self):
        test_line = " ".join(self.TEST)
        line_parser = LineParser.parser_with_delimiter("|")

        with self.assertRaises(LineParseException):
            person = line_parser.parse_line(test_line)
