"""

Find the airports reachable from a given airport within the plane's maximum range.


"""

from IslandHopper.dist import haversine_array


def reachable_airports(airports, start_ident, max_range, customs_time):
    """
    Parameters:
    - airports: table from airports_clean()
    - start_ident: ident of the departure airport
    - max_range: maximum distance of a single flight (km)
    - customs_time: hours lost when the arrival country is different

    Returns:
    - table with one row per reachable airport: ident, distance_km, flight_time
    """
    # 1. Row of the departure airport (same as in the dist.py test)
    start = airports[airports["ident"] == start_ident].iloc[0]

    # 2. Distances from the departure airport to ALL airports (one single call)
    distances = haversine_array(start["latitude_deg"], start["longitude_deg"],
                                airports["latitude_deg"], airports["longitude_deg"])

    # 3. Keep only the airports within range, excluding the departure airport
    mask = (distances <= max_range) & (airports["ident"] != start_ident)
    neighbors = airports[mask].copy()
    neighbors["distance_km"] = distances[mask]

    # 4. Flight time in hours: distance / 500, plus customs if the country changes
    neighbors["flight_time"] = neighbors["distance_km"] / 500 + (customs_time * (neighbors["iso_country"] != start["iso_country"]))

    return neighbors[["ident", "distance_km", "flight_time"]]