from flask import Flask, make_response, request

from storage.data import DataService
from util.parser import LineParseException, LineParser
from util.sorting import sort_people_by

app = Flask(__name__)
storage = DataService()


@app.route("/records", methods=["POST"])
def records():
    data_line = request.form.get("data")
    delimiter = LineParser.delimiter_from_line(data_line)
    parser = LineParser.parser_with_delimiter(delimiter)

    try:
        person = parser.parse_line(data_line)
    except LineParseException:
        return make_response({"error": "malformed request"}, 403)

    storage.insert(person)
    return make_response({"status": "OK"}, 201)


@app.route("/records/<string:sort_element>", methods=["GET"])
def records_sorted(sort_element: str):
    people = storage.get_all()
    sorted_people = sort_people_by(sort_element, people)
    response_data = tuple(map(lambda x: x._asdict(), sorted_people))
    response_body = {"people": response_data}
    return make_response(response_body, 200)


if __name__ == "__main__":
    app.run("0.0.0.0")
