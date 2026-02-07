import requests

API_KEY = "YOUR_API_KEY"   # put your OpenWeather API key here
CITY = "Tashkent"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
else:
    print("Error fetching weather data")


# task2
import requests
import random

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.themoviedb.org/3/discover/movie"

# Genre name → genre ID
genres = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "romance": 10749,
    "sci-fi": 878
}

user_genre = input("Enter a genre (action, comedy, drama, horror, romance, sci-fi): ").lower()

if user_genre not in genres:
    print("Genre not supported")
else:
    params = {
        "api_key": API_KEY,
        "with_genres": genres[user_genre],
        "language": "en-US"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        movies = data["results"]

        if movies:
            movie = random.choice(movies)
            print("\n🎬 Movie Recommendation:")
            print("Title:", movie["title"])
            print("Release date:", movie["release_date"])
            print("Overview:", movie["overview"])
        else:
            print("No movies found for this genre.")
    else:
        print("Error fetching movie data")
