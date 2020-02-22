import requests
import json

location = "YOUR_LOCATION"
rapidapikey = "YOUR_KEY"

nexmoapikey = "YOUR_APIKEY"
nexmoapisecret = "YOUR_APISECRET"
phonenumber = "YOUR_PHONENUMBER"

def checkWeather(location):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"callback":"test","q":location}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': rapidapikey
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response

def sendSMS():
    API_ENDPOINT = "https://rest.nexmo.com/sms/json"

    data = {
        "api_key" : nexmoapikey,
        "api_secret" : nexmoapisecret,
        "to" : phonenumber,
        "from" : "NEXMO",
        "text" : "Weather warning!! Stay alert, stay safe",
    }
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data)
    print(r.text)


response = checkWeather(location)
#response = '{"coord":{"lon":73.86,"lat":18.52},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":306.37,"feels_like":304.88,"temp_min":306.37,"temp_max":306.37,"pressure":1013,"humidity":18,"sea_level":1013,"grnd_level":942},"wind":{"speed":0.72,"deg":105},"clouds":{"all":0},"dt":1582363522,"sys":{"country":"IN","sunrise":1582334937,"sunset":1582376863},"timezone":19800,"id":1259229,"name":"Pune","cod":200}'

response_json = json.loads(response)
windspeed = response_json['wind']['speed']
temperature = response_json['main']['temp']

#check for the weather condition if extreme then send the SMS
if windspeed > 0 or temperature > 250:
    sendSMS()

