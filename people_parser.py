import argparse
import sys

from util.parser import FileParser, Person

sort_options = set(["gender", "birth_date", "last_name"])

command_parser = argparse.ArgumentParser(
    description="Parse a file of data representing people"
)

command_parser.add_argument(
    "--sort", dest="sort", help="Element of a person's data to sort by"
)
command_parser.add_argument("data_file", type=str, help="Path to the data file")


if __name__ == "__main__":
    args = command_parser.parse_args(sys.argv[1:])

    if not args.data_file:
        raise argparse.ArgumentError()

    with open(args.data_file, "r") as f:
        file_parser = FileParser(f)

        if args.sort in sort_options:
            people = getattr(file_parser, "people_by_" + args.sort)
        else:
            people = file_parser.people

    people_strings = map(str, people)

    sys.stdout.write("\n".join(people_strings))
