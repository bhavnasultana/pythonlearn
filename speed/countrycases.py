import requests
import time
import utils.auth
url = "https://covid-19-data.p.rapidapi.com/country"
country = open("countries.text", "r")
no_of_rows = sum(1 for line in open("countries.text"))
output_country = open("output.txt", "w")
for i in range(no_of_rows):
    r = (country.readline()).rstrip()
    querystring = {"name":r}
    print(querystring)

    headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': utils.auth.load_rapidapi_key()
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonResponse = response.json()

    for x in jsonResponse:
        for key, value in x.items():
            if key == "country":
                output_country.write('%s,' %value)

            elif key == "confirmed":
                output_country.write('%s,' %value)

            elif key == "deaths":
                output_country.write('%s\n' % value)
    time.sleep(2)


country.close()
output_country.close()
