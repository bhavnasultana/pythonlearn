import requests
import utils.auth

class Covid_data:
    def fetch_coviddata(self,url,headers,querystring):
        #response = requests.request("GET", url, headers = headers, params = querystring)
        response = requests.get(url, headers = headers , params = querystring)
        jsonResponse = response.json()
        return jsonResponse


x = Covid_data()
y = x.fetch_coviddata("https://covid-19-data.p.rapidapi.com/country", headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': utils.auth.load_rapidapi_key()
    }, querystring = {"name":"belgium"})
print(y)

