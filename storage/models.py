import collections
from datetime import datetime


class Person(
    collections.namedtuple(
        "Person", "last_name, first_name, gender, favorite_color, date_of_birth"
    )
):
    DATE_FORMAT = "%m/%d/%Y"

    def __new__(cls, last_name, first_name, gender, favorite_color, date_of_birth):
        _formatted_date = datetime.strptime(date_of_birth, cls.DATE_FORMAT)
        return super().__new__(
            cls, last_name, first_name, gender, favorite_color, _formatted_date
        )

    @property
    def date_of_birth_formatted(self):
        return datetime.strftime(self.date_of_birth, self.DATE_FORMAT)

    @classmethod
    def make(cls, iterable):
        return cls(*iterable)

    def __str__(self):
        return "last_name={}, first_name={}, gender={}, favorite_color={}, date_of_birth={}".format(
            self.last_name,
            self.first_name,
            self.gender,
            self.favorite_color,
            self.date_of_birth_formatted,
        )
