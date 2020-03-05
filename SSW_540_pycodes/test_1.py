
"""
Author: Matt Tarantino
Description: This application will prompt the user to enter their home address
and using a geocoding service, will retrieve their lat and long. Then it will do
the same for the address of The White House. Once the application has both coordinate
sets, it will perform a calculation to determine the distance (in miles) between
the two addresses. It will finally return this distance to the user after rounding
to the nearest mile.
"""

#import required libraries
import urllib.request, urllib.parse, urllib.error
import re
import ssl
import json
from math import pi, sin, cos, sqrt, asin

#ignore SSL certificate errors


#method that takes the input parameters and make an http request to get back
#the json reponse. If your connection is offline, the request will fail and the
#program will properly catch the error and exit.
def lookup_address(street, city, state, zip):
    #get the params ready for encoding
    params = {
        'street' : street,
        'city' : city,
        'state' : state,
        'zip' : zip,
        'benchmark' : 'Public_AR_Current',
        'format' : 'json'
    }

    #encode the params
    params = urllib.parse.urlencode(params)

    url = 'https://geocoding.geo.census.gov/geocoder/locations/address'

    #append the params to the URL
    url = url + '?' + params

    try:
        #make the request and catch if an error occurs
        json = urllib.request.urlopen(url).read()
    except:
        print('An error occurred while looking up the address! Please check your internet connection and try again.')
        exit()

    #decode the response and return the json back
    json = json.decode()
    return json

#takes the json response from lookup_address and attempts to parse out the
#coordinates from the json. It first converts it to actual json (from a string)
#and then parses the nested results. If the response doesn't match this structure
#then it is likely because it could not find a result, thus the structure will
#throw an error and the method will catch the error and return a message back
#to the user and the program will exit.
def parse_address_json(json_data):
    try:
        json_data = json.loads(json_data)
        coordinates = json_data['result']['addressMatches'][0]['coordinates']
        return coordinates
    except:
        print('The address could not be found! Please check the address and try again.')
        exit()

#this method converts an individual value to radians
def convert_to_radians(value):
    try:
        return value * pi / 180
    except:
        print('An unexpected error occurred! Please try again.')
        exit()

#prompts the user for their address in small chunks, and saves them to individual
#variables. Includes error handling
try:
    street = input('Enter your house number and street name (123 Smith Street): ')
    city = input('Enter your city (Cranford): ')
    state = input('Enter your state (New Jersey): ')
    zip = input('Enter your zip code (07016): ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()

#verifies that they filled out all fields. If they didn't then the program will
#let them know and exit.
if len(street) == 0 or len(city) == 0 or len(state) == 0 or len(zip) == 0:
    print('One or more of your inputs was blank. All fields are required. Please try again!')
    exit()
else:
    print('Great! Looking up your address...')

#calls the lookup_address method with their inputs, and stores the result in user_address_json.
#then it passes that to the parse_address_json method and stores the result in user_coordinates.
#the methods already include error checking, so the program will only continue if all was successful.
user_address_json = lookup_address(street, city, state, zip)
user_coordinates = parse_address_json(user_address_json)

#then parses out the individual x and y coordinates and converts them to a float.
#No errors should occur here, but a generic except is included for safe measure.
try:
    user_lon = float(user_coordinates['x'])
    user_lat = float(user_coordinates['y'])
except:
    print('An unexpected error occurred! Please try again.')
    exit()

print('We found your address! Looking up the address of The White House...')

street = "1600 Pennsylvania Ave NW"
city = "Washington"
state = "DC"
zip = "20500"

#repeats the same process as the user address, however the white house address is
#hard coded.
white_house_address_json = lookup_address(street, city, state, zip)
white_house_coordinates = parse_address_json(white_house_address_json)

#then parses out the individual x and y coordinates and converts them to a float.
#No errors should occur here, but a generic except is included for safe measure.
try:
    white_house_lon = float(white_house_coordinates['x'])
    white_house_lat = float(white_house_coordinates['y'])
except:
    print('An unexpected error occurred! Please try again.')
    exit()

print('The White House address found. Calculating the distance between them...')

#converts the coordinates to radians using the convert_to_radians to method defined above.
#saves the results to new variables.
user_lon_radians = convert_to_radians(user_lon)
user_lat_radians = convert_to_radians(user_lat)
white_house_lon_radians = convert_to_radians(white_house_lon)
white_house_lat_radians = convert_to_radians(white_house_lat)

# approximate radius of earth in mi
R = 3956

#assigns the radian variables to new variables for easier understanding in the calculation
lat1 = white_house_lat_radians
lon1 = white_house_lon_radians
lat2 = user_lat_radians
lon2 = user_lon_radians

#wrap the math in a try/except incase anything goes wrong. These calculations were
#provided by the assignment reference material.
try:
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(min(1, sqrt(a)))

    distance = R * c
except:
    print('An unexpected error occurred! Please try again.')
    exit()

#round to the nearest mile.
distance = round(distance)

#return the result to the user.
print(f'The distance between your home and The White House is about {distance} miles.')
