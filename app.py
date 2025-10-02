import requests

api_key = 'f8049f291455a94b037c666a6a576a80'

user_input = input("Enter city: ")

weather_data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_input}&limit=5&appid={api_key}")
weather_= weather_data.json()[]
