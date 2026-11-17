"""

Streamlit app for the Island Hopper project.

"""

import streamlit as st

from IslandHopper.data_preparation import airports_clean, airport_labels
from IslandHopper.routes import min_stops_route
from IslandHopper.plots import route_map

st.title("Island Hopper")


@st.cache_data
def load_data():
    return airports_clean()


airports = load_data()


labels = airport_labels(airports)
names = sorted(labels)  # alphabetical order

start_label = st.sidebar.selectbox(
    "Departure airport", names,
    index=names.index("Milan Malpensa International Airport (MXP)"),)
end_label = st.sidebar.selectbox(
    "Arrival airport", names,
    index=names.index("Athens Eleftherios Venizelos International Airport (ATH)"),)

start = labels[start_label]   # back to the ident, used by the route functions
end = labels[end_label]

# Inputs (sidebar)
start = st.sidebar.text_input("Departure airport (ident)", "LIMC")
end = st.sidebar.text_input("Arrival airport (ident)", "LGAV")
max_range = st.sidebar.slider("Maximum range (km)", 500, 17000, 1000, step=100)
customs_time = st.sidebar.number_input("Customs time (hours)", 0.0, 24.0, 2.0)

if st.sidebar.button("Find route"):
    # 1. check that both idents exist in the table
    # 2. search the route (spinner while it runs)
    with st.spinner("Searching..."):
        path = min_stops_route(airports, start, end, max_range, customs_time)

    # 3. if no route: show a warning; otherwise show the stops and the map
    if not path:
        st.warning("No route found.")
    else:
        st.plotly_chart(route_map(airports, path), width="stretch")