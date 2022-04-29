import math
import csv

DATA = []
# Load Food Truck Data
with open('data/ft_data.csv', mode='r') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    for line in reader:
        # Filter for Food Tucks with approved status
        # later on, might be able to expand this to filter the data set more.
        # e.g., a function to handle filtering the data set
        if line['Status'] == 'APPROVED':
            DATA.append(line)


def get_foodtrucks(latitude, longitude):
    """
    Sorts the trucks by destination from specified latitude and longitude
    Returns the 5 closest food trucks as a list of dictionaries.
    """
    for truck in DATA:
        truck["distance"] = distance((latitude, longitude), (float(truck['Latitude']), float(truck['Longitude'])))
    sorted_trucks = sorted(DATA, key=lambda i: i['distance'])
    return  sorted_trucks[0:5]


def distance(origin, destination):
    """
    Used distance function from: 'https://gist.github.com/rochacbruno/2883505'
    input is latitude and longitude pairs for starting point and destination.
    Returns the distance in miles
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 3959  # mi

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    # I won't lie. I'm not a mathemetician and would have to do quite a bit of research to understand this
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d