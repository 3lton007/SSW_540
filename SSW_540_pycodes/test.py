import urllib
import json
import sys
from math import radians, cos, sin, asin, sqrt


def getPosition(url):
    loc = []
    destOpen = urllib.urlopen(url)
    data = destOpen.read()
    destJson = json.loads(str(data))
    if destJson["status"] != 'OK':
        print("Failed to retrive. Exiting the program")
        sys.exit()
    destLat = destJson["results"][0]["geometry"]["location"]["lat"]
    destLon = destJson["results"][0]["geometry"]["location"]["lng"]
    loc.append(destLon)
    loc.append(destLat)
    return loc


def getDistance(destLoc, sourceLoc):
    lon1 = sourceLoc[0] * (3.14 / 180)
    lon2 = destLoc[0] * (3.14 / 180)
    lat1 = sourceLoc[1] * (3.14 / 180)
    lat2 = destLoc[1] * (3.14 / 180)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(min(1, sqrt(a)))
    kms = 6367 * c
    miles = (kms * 5) / 8
    return miles


serviceUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
location = input('Enter the location : ')
if len(location) < 1:
    print("Invalid destination")
    sys.exit()
url = serviceUrl + urllib.parse.urlencode({'sensor': 'false', 'address': location})
sourceUrl = serviceUrl + urllib.urlencode({'sensor': 'false', 'address': ' Hoboken, NJ'})
destLoc = getPosition(url)
sourceLoc = getPosition(sourceUrl)

dist = getDistance(destLoc, sourceLoc)
print('Distance between Hoboken, NJ and ', location, ' is about :', int(dist), "miles.")


