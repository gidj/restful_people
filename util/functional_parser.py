from typing import TextIO, Tuple

from storage.models import Person


def file_to_person(file: TextIO) -> Tuple[Person]:
    lines = _file_lines(file)
    pass


def _file_lines(file: TextIO) -> Tuple:
    file.seek(0)
    return tuple(file.read().splitlines())


def _parser_from_delimiter(delimiter: str):
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
