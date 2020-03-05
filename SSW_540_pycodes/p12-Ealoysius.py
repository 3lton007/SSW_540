



import urllib.request, urllib.parse, urllib.error
import re
import json
from math import pi, cos, sin, sqrt, asin



def lookup_address(street, city, state, zip):
    params = {
        'street' : street,
        'city' : city,
        'state' : state,
        'zip' : zip,
        'benchmark' : 'Public_AR_Current',
        'format' : 'json'
    }

    params = urllib.parse.urlencode(params)

    url = 'https://geocoding.geo.census.gov/geocoder/locations/address'

    url = url + '?' + params

    try:
        json = urllib.request.urlopen(url).read()
    except ValueError:
        raise ValueError("URL is Invalid")
    
    json = json.decode()
    return json
     

def parse_address_json(json_data):
    try:
        json_data = json.loads(json_data)
        coordinates = json_data['result']['addressMatches'][0]['coordinates']
        return coordinates
    except ValueError:
        raise ValueError("Address not found")


def convert_to_radians(value):
    try:
        return value * pi/180
    except ValueError:
        raise ValueError("An Unexpected Error Occurred!")


def main():
    try:
        street = input("Enter Your House number $ Street name (Eg: 188 Hutton Street)")
        city = input("Enter your city (Eg: Jersey City)")
        state = input("Enter your state (Eg: New Jersey)")
        zip = input("Enter Your zip code (07307)")
    except ValueError:
        raise ValueError("The input is Invalid!")

    if len(street) == 0 or len(city) == 0 or len(state) == 0 or len(zip) == 0:
        print("one of the field is empty")

    user_address_json = lookup_address(state, city, state, zip)
    user_coordsinates = parse_address_json(user_address_json)

    try:
        user_long = float(user_coordinates['x'])
        user_lat = float(user_coordinates['y'])
    except ValueError:
        raise ValueError("An unexpected error occured!")

    print("GOt user Address, Checking for address of White House")



    street = "1600 Pennsylvania Ave NW"
    city = "Washington"
    state = "Dc"
    zip = "20500"

    whitehouse_address_json  = lookup_address(street, city, state, zip)
    whitehouse_coordinates = parse_address_json(whitehouse_address_json)

    try:
        whitehouse_long = float(whitehouse_coordinates['x'])
        whitehouse_lat = float(whitehouse_coordinates['y'])
    except ValueError:
        raise ValueError("An unexpected error occurred!")
    
    print("Distance Calculation")


    user_long_radians = convert_to_radians(user_long)
    user_lat_radians = convert_to_radians(user)

    whitehouse_long = convert_to_radians(whitehouse_long)
    whitehouse_lat = convert_to_radians(whitehouse_lat)

    R = 3956

    lat_1 = whitehouse_lat_radians
    long_1 = whitehouse_long_radians
    lat_2 = user_lat_radians
    long_2 = user_long_radians

    try:
        dlon = long_2 = long_1
        dlat = lat_2 - lat_1

        a = sin(dlat / 2) **2 + cos(lat_1) * cos (lat_2) * sin (dlon/2) ** 2
        c = 2 * asin(min(1,sqrt(a)))

        dist = R * c
    except ValueError:
        raise ValueError("An unexpected error occurre!")


    dist = round(dist)

    print(f" The Distance between your home and the White House is about {dist} miles")

        

main()


    
    





