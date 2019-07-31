from typing import Callable, TextIO, Tuple

from storage.models import Person


def file_to_people(file: TextIO) -> Tuple[Person]:
    lines = _file_lines(file)
    parsed_lines = map(_parse_line, lines)
    return tuple(map(Person._make, parsed_lines))


def _file_lines(file: TextIO) -> Tuple[str]:
    file.seek(0)
    return tuple(file.read().splitlines())


def _parser_from_delimiter(delimiter: str) -> Callable[[str], Tuple[str]]:
    def f(line: str) -> Tuple[str]:
        return tuple(line.split(delimiter))

    return f


def _delimiter_from_line(line: str) -> str:
    delimiter = " "
    if "," in line:
        delimiter = ","
    elif "|" in line:
        delimiter = "|"
    return delimiter


def _parse_line(line: str) -> Tuple[str]:
    delimiter = _delimiter_from_line(line)
    parser = _parser_from_delimiter(delimiter)
    return parser(line)
