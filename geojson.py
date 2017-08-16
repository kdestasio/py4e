import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'    # The web address of the API

while True:
    address = input('Enter location: ')    # Ask the user to input an address
    if len(address) < 1: break    # If the entered line is blank, break

    url = serviceurl + urllib.parse.urlencode(    # Make a url by concatenating the API url and the url form of the address
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)    # Get a handle for the url
    data = uh.read().decode().   # call the read method to pull the entire document & decode (from probably UTF-8)
    print('Retrieved', len(data), 'characters').

    try:
        js = json.loads(data).   # Parse the data as string data
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':    # Check for failures - if js is false, if status key is missing, or status is not equal to "OK"
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"].   # Walking down the tree of keys to look for
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

# Code: http://www.py4e.com/code3/geojson.py