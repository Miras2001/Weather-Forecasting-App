import requests

API_KEY = "d6b50f97e299ae70f39f5fe80e1520e1"
API_URL = "https://api.openweathermap.org/data/2.5"


def main():
    city = input("Enter a city name: ")
    try:
        current_weather = get_weather(city, "weather")
        forecast = get_weather(city, "forecast")
        display_weather(current_weather, forecast)
    except Exception as e:
        print(f"Error: {e}")


def get_weather(city, endpoint):
    """get weather data from OpenWeather API."""
    url = f"{API_URL}/{endpoint}"
    response = requests.get(url, params={"q": city, "appid": API_KEY, "units": "metric"})
    response.raise_for_status()  
    return response.json()


def display_weather(current, forecast):
    """Display current weather and a 5-day forecast."""
    print(f"\nWeather in {current['name']}:")
    print(f"Temperature: {round(current['main']['temp'])}°C")
    print(f"Condition: {current['weather'][0]['description'].capitalize()}\n")

    print("5-Day Forecast:")
    for item in forecast['list']:
        if "12:00:00" in item['dt_txt']:
            date = item['dt_txt'].split(" ")[0]
            temp = round(item['main']['temp'])
            desc = item['weather'][0]['description'].capitalize()
            print(f"{date}: {temp}°C, {desc}")


if __name__ == "__main__":
    main()
