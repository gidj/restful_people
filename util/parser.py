class FileParser(object):
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    GENDER = "gender"
    FAVORITE_COLOR = "favorite_color"
    DATE_OF_BIRTH = "date_of_birth"

    def __init__(self, filename):
        self._data = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                self._data.append(self.parse_line(line))

    def parse_line(self, line: str) -> dict:
        split_line = line.split(self._line_delimit_charater(line))
        data_dict = self._line_list_to_dict(split_line)
        return data_dict

    def _line_list_to_dict(self, line_list: list) -> dict:
        data = {}
        data[self.LAST_NAME] = line_list[0]
        data[self.FIRST_NAME] = line_list[1]
        data[self.GENDER] = line_list[2]
        data[self.FAVORITE_COLOR] = line_list[3]
        data[self.DATE_OF_BIRTH] = line_list[4]
        return data

    def _line_delimit_charater(line: str) -> str:
        delimiter = ' '
        if ',' in line:
            delimiter = ','
        elif '|' in line:
            delimiter = '|'
        return delimiter
