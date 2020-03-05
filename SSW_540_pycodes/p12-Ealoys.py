"""

To calculate distance between the users location and white house
using Json and Gecoding API
@eltonlaoys
"""

import urllib.request, urllib.parse, urllib.error
import json
from math import pi, sin, cos, sqrt, asin


def lookup_address(street, city, state, zip):
    """ Input parameters and a json request """ 
    params = {
        'street' : street,
        'city' : city,
        'state' : state,
        'zip' : zip,
        'benchmark' : 'Public_AR_Current',
        'format' : 'json'
    }

    """ Appending the URL and making an json request """
    params = urllib.parse.urlencode(params)

    url = 'https://geocoding.geo.census.gov/geocoder/locations/address'

 
    url = url + '?' + params

    try:
        
        json = urllib.request.urlopen(url).read()
    except ValueError:
        raise ValueError('Adress error occured!')
        

  
    json = json.decode()
    return json


def parse_address_json(json_data):
    """ takes the json response from lookup address \
        Converts it to actual json from a string and parse the results """
    try:
        json_data = json.loads(json_data)
        coordinates = json_data['result']['addressMatches'][0]['coordinates']
        return coordinates
    except ValueError:
        raise ValueError('Adress not found!')
        


def convert_to_radians(value):
    """ Convert values to radians """
    try:
        return value * pi / 180
    except ValueError:
        raise ValueError('An unexpected error occurred!')


def main():
    """ Takes input user address """
    try:
        street = input('Enter your house number and street name (188 Hutton Street): ')
        city = input('Enter your city (Jersey City): ')
        state = input('Enter your state (New Jersey): ')
        zip = input('Enter your zip code (07307): ')
    except ValueError:
        raise('This input is invalid! Please try again.')
        


    if len(street) == 0 or len(city) == 0 or len(state) == 0 or len(zip) == 0:
        print("One of the field is missing!")


    """ calls lookup address and stores the results in user_address_json """
    user_address_json = lookup_address(street, city, state, zip)
    user_coordinates = parse_address_json(user_address_json)

    """ Converting longitudes and latitudes to float """
    try:
        user_lon = float(user_coordinates['x'])
        user_lat = float(user_coordinates['y'])
    except ValueError:
        raise ValueError('An unexpected error occurred!')
        

    print('User address Fetched!')

    street = "1600 Pennsylvania Ave NW"
    city = "Washington"
    state = "DC"
    zip = "20500"

    """ Same goes for white house address as user address request """
    white_house_address_json = lookup_address(street, city, state, zip)
    white_house_coordinates = parse_address_json(white_house_address_json)

    try:
        white_house_lon = float(white_house_coordinates['x'])
        white_house_lat = float(white_house_coordinates['y'])
    except ValueError:
        ValueError('An unexpected error occurred!')
        

    print('The White House address Fetched!')
    print("Distance calculated!")

    """ converts the coords to radians """
    user_lon_radians = convert_to_radians(user_lon)
    user_lat_radians = convert_to_radians(user_lat)
    white_house_lon_radians = convert_to_radians(white_house_lon)
    white_house_lat_radians = convert_to_radians(white_house_lat)

    R = 3956 #radius of earth in miles

    lat1 = white_house_lat_radians
    lon1 = white_house_lon_radians
    lat2 = user_lat_radians
    lon2 = user_lon_radians


    try:
        dlon = lon2 - lon1 #distance between 2 longitudes and latitudes
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(min(1, sqrt(a)))

        distance = R * c
    except ValueError:
        raise ValueError('An unexpected error occurred!')
        


    distance = round(distance) #round to nearest mile

    """ Printing Result """
    print(f'The distance between your home and The White House is about {distance} miles.')

main()
