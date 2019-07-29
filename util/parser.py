from typing import List, TextIO

from storage.models import Person


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
        def _key(person):
            return person.date_of_birth

        return sorted(self._people, key=_key)


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
