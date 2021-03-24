import requests
import urllib
from GPSPhoto import gpsphoto

API_KEY = ""


def get_coordinates(filepath):
    try:
        data = gpsphoto.getGPSData(filepath)

        long = str(data['Longitude'])
        lat = str(data['Latitude'])
        coords = lat + "," + long
        params = {
            'latlng': coords,
            'key': API_KEY,
            'language': 'ru'
        }
        maps_params = coords
        url_maps = 'https://www.google.com/maps/search/?api=1&query='
        url_maps_full = url_maps + maps_params

        url_params = urllib.parse.urlencode(params)
        google_GeoCode_Url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        url = google_GeoCode_Url + url_params
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'OK':
            result = data['results'][0]
            location = result['formatted_address']
            print(location)
            print(url_maps_full)
        else:
            print("Произошла ошибка", data['status'])
    except:
            print("Файл не содержит координат.")



get_coordinates('C:\HW\photo1.jpg')
