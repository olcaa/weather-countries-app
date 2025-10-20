from config import Config
import requests

def fetch_weather():
    key = Config.WEATHER_API_KEY
    city = Config.CITY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    response = requests.get(url)
    data = response.json()
    print(data)