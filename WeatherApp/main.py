import requests, json, os
from dotenv import load_dotenv

load_dotenv()

api_Key = os.environ.get('APIKEY')
city = input("Weather in your city: ")

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_Key))
if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = main['temp']
    temperatureToC = (temperature - 32) * 5.0/9.0
    temperatureToC = int(temperatureToC)
    humidity = main['humidity']
    pressure = main['pressure']

    print(f"Temperature:  {temperatureToC}" + "°C")
    print(f"Humidity:  {humidity}" + "%")
    print(f"Pressure:  {pressure}" + "Pa")
else:
    print("You didn't spell your city correct")