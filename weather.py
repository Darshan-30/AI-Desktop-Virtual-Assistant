import requests
import speak

def Weather():
    api_key = "api_key"  # Replace with your OpenWeatherMap API key
    city = "Bengaluru"  # Replace with the city name you want weather info for

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


    try:
       
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        weather_data = response.json()

        if weather_data.get("main"):
            temperature = weather_data["main"]["temp"]
            weather_description = weather_data["weather"][0]["description"]
            weather_report = f"The current temperature is {temperature}°C with {weather_description}."
            speak.speak(weather_report)
            return weather_report
        else:
            speak.speak("I couldn't retrieve the weather information. Please try again.")
            return "I couldn't retrieve the weather information."

    except requests.exceptions.RequestException as e:
        speak.speak("There was an error connecting to the weather service.")
        return "There was an error connecting to the weather service."
