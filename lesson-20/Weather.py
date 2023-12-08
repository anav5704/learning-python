from pprint import pprint
import requests
import os


def getWeather():
    print("\n +++ Current Weather Conditions +++")
    
    city = input("\n Enter a City name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?appid=d65fa1b1e17b2096eef9ee9a53fcb75e&q={city}&units=metric"

    data = requests.get(url).json()

    print(f'\nCurrent weather for {data["name"]}:')
    print(f'\n{data["weather"][0]["description"].capitalize()} and feels like {data["main"]["feels_like"]:.1f}°\n')
    
getWeather()
