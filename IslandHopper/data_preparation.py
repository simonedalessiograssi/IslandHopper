'''

Preparation of the data for the IslandHopper project. This script handles the loading, 
cleaning, and transformation of raw data into a format suitable for analysis and modeling.

'''

import pandas as pd

input_file = "data/airports.csv"

# Only large and medium airports are considered for the analysis.
airports_types_allowed = ["large_airport", "medium_airport"]

# Columns to keep from the original dataset.
useful_columns = [
    "ident",          # airport id. (used instead of iata_code because some airports don't have it)
    "name",           # airport name
    "type",           # large_airport / medium_airport
    "latitude_deg",   # for calculating distances
    "longitude_deg",  # same as the previous one
    "iso_country",    # for customs (country change)
    "municipality",   # city, for displaying results
    "iata_code",      # 3-letter code (e.g., MXP, SYD) 
]


def airports_clean(path= input_file):
    """Loads the CSV file and returns the cleaned DataFrame."""

    # "NA" in the dataset is a real value (Namibia, for example), so we need to change the default
    # behavior of pandas for treating it.
    # without changing the default behavior, the "NA" values would be converted to NaN, which is not what we want.
    df = pd.read_csv(path, keep_default_na=False, na_values=[""])

    # Keep only the airports of the types we are interested in
    df = df[df["type"].isin(airports_types_allowed)]

    # Keep only the columns we are interested in
    df = df[useful_columns]

    # Drop rows without coordinates or country: they are not needed for the calculation
    df = df.dropna(subset=["latitude_deg", "longitude_deg", "iso_country"])

    # Remove entries containing "duplicate" in the name
    df = df[~df["name"].str.contains("duplicate", case=False, na=False)]

    # Reset the index to be from 0 to N-1
    df = df.reset_index(drop=True)

    return df

def airport_labels(airports):
    """Return a dict {label: ident}, e.g. 'Milan Malpensa International Airport (MXP)': 'LIMC'."""
    codes = airports["iata_code"].fillna(airports["ident"])
    labels = airports["name"] + " (" + codes + ")"
    return dict(zip(labels, airports["ident"]))

if __name__ == "__main__":
    airports = airports_clean()
    print(airports.shape)
    print(airports.head())
    