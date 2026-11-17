"""Plot the routes and airports on a map."""

import pandas as pd
import plotly.graph_objects as go


def route_map(airports, path):
    """
    Draw the route on a globe.

    Parameters:
    - airports: table from airports_clean()
    - path: list of airport idents, from start to end (output of the route functions)

    Returns:
    - a Plotly figure
    """
    # 1. Rows of the airports in the route, IN THE ORDER of the path
    route = airports.set_index("ident").loc[path]

    # 2. Text to show on hover: name and code (iata_code can be missing: use ident then)
    labels = [
        f"{row['name']} ({row['iata_code'] if pd.notnull(row['iata_code']) else ident})"
        for ident, row in route.iterrows()
    ]

    # 3. One trace with the line and the markers
    fig = go.Figure(go.Scattergeo(
        lat=route["latitude_deg"].tolist(),
        lon=route["longitude_deg"].tolist(),
        mode="lines+markers",
        text=labels,
        hoverinfo="text",
    ))

    # 4. Look of the map: globe centred on the route, land and countries visible
    fig.update_geos(
        projection_type="orthographic",
        showland=True,
        showcountries=True,
        projection_rotation=dict(lon=route["longitude_deg"].mean(),
                                 lat=route["latitude_deg"].mean()),
    )

    return fig