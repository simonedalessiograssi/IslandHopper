'''

Calculate the distance between two airports using the Haversine formula.

'''

import numpy as np
from math import radians, sin, cos, sqrt, asin

def haversine_single(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)

    """
    

    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km


def haversine_array(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between a point 
    and an array of points on the earth (specified in decimal degrees)

    """
    # convert decimal degrees to radians 
    lat1, lon1 = np.radians(lat1), np.radians(lon1)
    lat2, lon2 = np.radians(lat2), np.radians(lon2)

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 

    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km

if __name__ == "__main__":
    from data_preparation import airports_clean

    airports = airports_clean()
    mxp = airports[airports["ident"] == "LIMC"].iloc[0]

    distances = haversine_array(mxp["latitude_deg"], mxp["longitude_deg"],
                                     airports["latitude_deg"], airports["longitude_deg"])

    print(len(distances), len(airports))
    print(distances[airports["ident"] == "LIMC"])
    print(distances[airports["ident"] == "YSSY"])
    print((distances <= 3000).sum() - 1)
