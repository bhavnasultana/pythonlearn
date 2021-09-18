import requests
import utils.auth


class CovidData:

    def __init__(self):
        self.headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': utils.auth.load_rapidapi_key()
        }
        self.url = "https://covid-19-data.p.rapidapi.com/country"


    def fetch_coviddata(self,country):
        #response = requests.request("GET", url, headers = headers, params = querystring)
        response = requests.get(self.url, headers=self.headers , params = {"name":country})
        jsonResponse = response.json()
        return jsonResponse


x = CovidData()
y = x.fetch_coviddata("belgium")
print(y)

