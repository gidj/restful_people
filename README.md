# Restful People
A mini project to parse records, and access them via a RESTful API

## Running Locally
* The command line `person_parser.py` can be run independently:
```shell
$ python person_parser.py --sort SORT filename
```
* To use the API, the easiest way is to use docker. Issue the following commands and a server will be accessible at localhost:8000
```shell
$ docker build -t restful_people .
$ docker run restful_people
```

