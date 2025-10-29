from config import Config
from datetime import datetime
from utils.functions import convert_to_celsius as c
import requests

def fetch_weather():
    key = Config.WEATHER_API_KEY
    city = Config.CITY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    response = requests.get(url)
    data = response.json()
    weather = {
        "temp" : c(data.get("main").get("temp")),
        "feels_like" : c(data.get("main").get("feels_like")),
        "pressure" : data.get("main").get("pressure"),
        "humidity" : data.get("main").get("humidity"),
        "wind_speed" : data.get("wind").get("speed"),
        "place" : data.get("name").get("name"),
        "timestamp" : datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    }
    return weather