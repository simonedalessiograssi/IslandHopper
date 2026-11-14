# IslandHopper

Using airport data from OurAirports, it computes whether a small plane
with a limited range can fly from Milan Malpensa to Sydney, with how many
stops and how much time.

## Data

**Source:** OurAirports, airports dataset (`airports.csv`), available at
https://ourairports.com/data/. Check the terms of use on the same page.


## Project structure

```
island-hopper/
├── app.py                      # Streamlit app: inputs, results and map
├── island_hopper/              # Project code
│   ├── __init__.py
│   ├── data_preparation.py     # Loading, filtering and cleaning of the dataset
│   ├── geo.py                  # Distance between airports
│   ├── graph.py                # Flight network for a given range and customs time
│   ├── routes.py               # Minimum stops, minimum time, farthest airport
│   └── plots.py                # Map of the route
├── data/                       # Dataset (in .gitignore for now)
├── .gitignore
├── requirements.txt
└── README.md
```