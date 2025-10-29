from services.open_weather import fetch_weather
from services.excel_file import append_to_excel
import time


#CRON
while True:
    weather = fetch_weather()
    append_to_excel(weather)
    print ("Pobrano nowe dane")
    time.sleep(10)
