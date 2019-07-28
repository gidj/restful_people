from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run("0.0.0.0")


@app.route("/records", methods=["POST"])
def records():
    return "Posting to records"


@app.route("/records/<string:sort_key>", methods=["GET"])
def records_sorted(sort_key: str):
    return "Getting records, sorted by '{}'".format(sort_key)
