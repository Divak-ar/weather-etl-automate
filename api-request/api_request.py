import requests
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("api_key")

api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Chicago"

def fetch_data():
    print("Getting the weather data from the weather stack api : ")
    try: 
        response = requests.get(api_url)
        response.raise_for_status()
        print("API Request Processed Successfully ")
        return response.json()
    
    except requests.exceptions.RequestException as e: 
        print(f"An error occurred: {e}")
        raise

fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-08-22 15:13', 'localtime_epoch': 1755875580, 'utc_offset': '-4.0'}, 'current': {'observation_time': '07:13 PM', 'temperature': 28, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '06:13 AM', 'sunset': '07:44 PM', 'moonrise': '05:19 AM', 'moonset': '07:39 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 2}, 'air_quality': {'co': '418.1', 'no2': '49.21', 'o3': '90', 'so2': '4.995', 'pm2_5': '13.69', 'pm10': '14.06', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 4, 'wind_degree': 14, 'wind_dir': 'NNE', 'pressure': 1018, 'precip': 0, 'humidity': 28, 'cloudcover': 0, 'feelslike': 27, 'uv_index': 6, 'visibility': 16, 'is_day': 'yes'}}
