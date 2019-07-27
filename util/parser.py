import collections
from datetime import datetime
from typing import List, TextIO

Person = collections.namedtuple(
    "Person", "last_name, first_name, gender, favorite_color, date_of_birth"
)


class FileParser(object):
    def __init__(self, data_file: TextIO):
        data_file.seek(0)
        self._raw_lines = tuple(data_file.read().splitlines())

        if self._raw_lines:
            self._line_parser = LineParser.parser_with_delimiter(
                self.delimiter_from_line(self._raw_lines[0])
            )
        else:
            self._line_parser = LineParser()

        self._people = self._get_people_from_raw_lines(self._raw_lines)

    def _get_people_from_raw_lines(self, raw_lines: tuple):
        people = tuple(self._line_parser.parse_line(line) for line in self._raw_lines)
        return people

    @staticmethod
    def delimiter_from_line(line: str) -> str:
        delimiter = " "
        if "," in line:
            delimiter = ","
        elif "|" in line:
            delimiter = "|"
        return delimiter

    @property
    def people(self) -> List[Person]:
        return self._people

    @property
    def people_by_gender(self) -> List[Person]:
        def _key(person):
            return person.last_name.lower()

        female = filter(lambda p: p.gender == "female", self._people)
        male = filter(lambda p: p.gender == "male", self._people)

        _sorted = tuple(sorted(female, key=_key) + sorted(male, key=_key))
        return _sorted

    @property
    def people_by_last_name(self) -> List[Person]:
        def _key(person):
            return person.last_name.lower()

        return sorted(self._people, key=_key)

    @property
    def people_by_birth_date(self) -> List[Person]:
        pass


class LineParseException(Exception):
    pass


class LineParser(object):
    def __init__(self, delimiter=" "):
        self._delimiter = delimiter

    @classmethod
    def parser_with_delimiter(cls, delimiter):
        return cls(delimiter)

    def parse_line(self, line: str) -> Person:
        split_line = line.split(self._delimiter)
        try:
            person = self._line_as_person(split_line)
        except (IndexError, TypeError):
            raise LineParseException("Line is misformatted, or delimiter is incorrect")
        return person

    def _line_as_person(self, line_list: list) -> Person:
        _line_with_date = line_list[:4]
        _line_with_date.append(datetime.strptime(line_list[4], "%m/%d/%Y"))
        person = Person(*_line_with_date)
        return person
