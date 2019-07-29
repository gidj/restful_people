# Restful People
A mini project to parse records, and access them via a RESTful API

## Running Locally
* The command line `person_parser.py` can be run independently:
```shell
$ python person_parser.py --sort birth_date|gender|last_name sample_data.txt
```
* To use the API, the easiest way is to use docker. Issue the following commands and a server will be accessible at localhost:8000
```shell
$ docker build -t restful_people .
$ docker run -p 8000:8000 restful_people
```
* You can now test the api using the `sample_request.py` file, if you have the `requests` package installed.

