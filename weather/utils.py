import requests

def get_weather(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min&timezone=America%2FSao_Paulo"
    response = requests.get(url)
    data = response.json()
    day = data.get("daily").get("time")[2]
    max_t, min_t = data.get("daily").get("temperature_2m_max")[2], data.get("daily").get("temperature_2m_min")[2]
    return day, max_t, min_t
