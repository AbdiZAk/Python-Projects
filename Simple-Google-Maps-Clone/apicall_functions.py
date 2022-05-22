import requests
from dotenv import load_dotenv
import os


def config():
    load_dotenv()


load_dotenv()

google_api_key = os.getenv("google_api_key")


def googleGeocode(google_api_key, location):
    headers = {'Api-Key': google_api_key}
    params = {'location': location}
    response = requests.get('https://api.ist256.com/google/geocode', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    # If there is no data in the results then the input is invalid
    if data['results'] == []:
        return 'error'
    else:
        latlon = data['results'][0]['geometry']['location']
        return latlon


def get_weather_data(weather_key, lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/onecall?'
    query_string = {
        "lat": lat,
        "lon": lon,
        "exclude": "minutely,hourly",
        'units': "imperial",
        "appid": weather_key

    }
    response = requests.get(url, params=query_string)
    response.raise_for_status()
    response = response.json()
    return response


def googlePlacesSearch(google_api_key, lat, lng, place_type, keyword=None):
    headers = {'Api-Key': google_api_key}
    params = {'lat': lat, 'lng': lng, 'type': place_type}
    if keyword != None:
        params['keyword'] = keyword
    response = requests.get('https://api.ist256.com/google/places/search', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    if data['results'] == []:
        return 'error'
    else:
        return data['results']


# data = googlePlacesSearch(google_api_key, '25.761681', '-80.191788', "airport", "airport")

def googlePlacesDetails(google_api_key, place_id):
    headers = {'Api-Key': google_api_key}
    params = {'placeid': place_id}
    response = requests.get('https://api.ist256.com/google/places/details', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return data['result']


def get_geo_address(search):
    url = 'https://nominatim.openstreetmap.org/search'  # base URL without paramters after the "?"
    options = {'q': search, 'format': 'json'}
    response = requests.get(url, params=options)
    geodata = response.json()
    coords = {'lat': float(geodata[0]['lat']), 'lng': float(geodata[0]['lon'])}
    return coords


def key_phrase(text):
    endpoint = os.getenv('endpoint')
    subscription_key = os.getenv("subscription_key")
    url = f'{endpoint}text/analytics/v3.0/keyphrases'
    header = {'Ocp-Apim-Subscription-Key': subscription_key}
    payload = {"documents": [
        {"id": "3", "text": text}
    ]
    }
    response = requests.post(url, headers=header, json=payload)
    response.raise_for_status()
    phrases = response.json()
    return phrases


