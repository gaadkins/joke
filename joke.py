import requests
from pprint import pprint
import json

url = "https://icanhazdadjoke.com/"

payload={}
headers = {
  'Accept': 'application/json'
}

print("The Joke of the day is:\n")

response = requests.request("GET", url, headers=headers, data=payload)

responseJson = response.json()

pprint(responseJson)
