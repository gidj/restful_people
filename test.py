import unittest

from util.parser import FileParser, LineParser


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

        assert person.first_name == self.FIRST_NAME
        assert person.last_name == self.LAST_NAME
        assert person.gender == self.GENDER
        assert person.favorite_color == self.FAVORITE_COLOR
        assert person.date_of_birth == self.DATE_OF_BIRTH
