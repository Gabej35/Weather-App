import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric" # metric for Celsius

    try:
        response = requests.get(complete_url)
        response.raise_for_status() # an exception for HTTP error
        data = response.json()

        if data["cod"] == 200: # checks if the response was successful
            main_data = data["main"]
            weather_data = data["weather"][0]

            temperature = main_data["temp"]
            feels_like = main_data["feels_like"]
            humidity = main_data["humidity"]
            weather_description = weather_data["description"]

            print(f"Weather in {city_name.capitalize()}:")
            print(f"  Temperature: {temperature}\u00B0C (Feels like: {feels_like}\u00B0C)")
            print(f"  Humidity: {humidity}%")
            print(f"  Description: {weather_description.capitalize()}")

        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

    except KeyError:
        print("Error: Could not parse weather data. Check city name or API response.")

if __name__ == "__main__":
    API_KEY = "API_KEY" # Not going to leave my API key out for you :p
    city = input("Enter city name: ")
    get_weather(city, API_KEY)


