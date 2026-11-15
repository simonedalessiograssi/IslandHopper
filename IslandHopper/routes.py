
"""

Find the best route between two airports (fewest stops).

"""




from IslandHopper.graph import reachable_airports


def min_stops_route(airports, start_ident, end_ident, max_range, customs_time):
    """
    Find the route with the fewest flights (hence the fewest stops).

    Returns:
    - list of airport idents from start to end, or None if the end
      airport cannot be reached
    """
    # If the start and end airports are the same, return a list with just that airport
    if start_ident == end_ident:
        return [start_ident]
    # For each visited airport: the airport we arrived from
    came_from = {start_ident: None}

    # Airports to explore at the current level
    frontier = [start_ident]

    while frontier:
        next_frontier = []

        for current in frontier:
            neighbors = reachable_airports(airports, current, max_range, customs_time)

            for neighbor in neighbors["ident"]:
                # 1. skip the airports already visited
                # 2. register where we came from
                # 3. add the airport to next_frontier
                # 4. if it is the destination, stop and return the route
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    next_frontier.append(neighbor)

                    if neighbor == end_ident:
                        return build_path(came_from, end_ident)

        frontier = next_frontier

    return None  # nothing left to explore: the destination is not reachable


def build_path(came_from, end_ident):
    """Rebuild the route from the start to end_ident, walking came_from backwards."""
    path = [end_ident]
    while came_from[path[-1]] is not None:
        path.append(came_from[path[-1]])
    return list(reversed(path))