import math

def get_foodtrucks(latitude, longitude):
    ret_list = []

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
