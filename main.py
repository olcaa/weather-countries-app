from services.open_weather import fetch_weather
from services.excel_file import append_to_excel
from services.mysql_db import init_database, insert_weather
import time

# init_database()

# CRON
while True:
    weather = fetch_weather()

    append_to_excel(weather)
    insert_weather(weather)

    print("Pobrano nowe dane")
    time.sleep(10)
