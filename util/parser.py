from typing import List, TextIO

from storage.models import Person
from util.sorting import _by_birth_date, _by_gender, _by_last_name


class FileParser(object):
    def __init__(self, data_file: TextIO):
        data_file.seek(0)
        self._raw_lines = tuple(data_file.read().splitlines())

        if self._raw_lines:
            self._line_parser = LineParser.parser_with_delimiter(
                LineParser.delimiter_from_line(self._raw_lines[0])
            )
        else:
            self._line_parser = LineParser()

        self._people = self._get_people_from_raw_lines(self._raw_lines)

    def _get_people_from_raw_lines(self, raw_lines: tuple):
        people = tuple(self._line_parser.parse_line(line) for line in self._raw_lines)
        return people

    @property
    def people(self) -> List[Person]:
        return self._people

    @property
    def people_by_gender(self) -> List[Person]:
        return _by_gender(self._people)

    @property
    def people_by_last_name(self) -> List[Person]:
        return _by_last_name(self._people)

    @property
    def people_by_birth_date(self) -> List[Person]:
        return _by_birth_date(self._people)


class LineParseException(Exception):
    pass


class LineParser(object):
    def __init__(self, delimiter=" "):
        self._delimiter = delimiter

    @classmethod
    def parser_with_delimiter(cls, delimiter):
        return cls(delimiter)

    @staticmethod
    def delimiter_from_line(line: str) -> str:
        delimiter = " "
        if "," in line:
            delimiter = ","
        elif "|" in line:
            delimiter = "|"
        return delimiter

    def parse_line(self, line: str) -> Person:
        split_line = line.split(self._delimiter)
        try:
            person = self._line_as_person(split_line)
        except (IndexError, TypeError):
            raise LineParseException("Line is misformatted, or delimiter is incorrect")
        return person

    def _line_as_person(self, line_list: list) -> Person:
        person = Person(*line_list)
        return person
