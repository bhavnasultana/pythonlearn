import requests
import json

import utils.auth

rapidapi_key = utils.auth.load_rapidapi_key()

url = "https://covid-19-data.p.rapidapi.com/country"
country = open("countries.text", "r")
r = country.readline()
querystring = {"name":r}
print(querystring)
headers = {
    'x-rapidapi-host': 'covid-19-data.p.rapidapi.com',
    'x-rapidapi-key': rapidapi_key
    }

response = requests.request('GET', url, headers=headers, params=querystring)









