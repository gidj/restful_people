import requests

data = {"data": "Adams,Adam,male,red,4/7/2000"}

r = requests.post("http://0.0.0.0:8000/records", data=data)
r = requests.get("http://0.0.0.0:8000/records/gender")
