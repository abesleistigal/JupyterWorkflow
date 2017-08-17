import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
# create a function to only dowload this data if we need to download it, first run..


def get_fremont_data(filename="Fremont.csv", url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data

    Parameters
    ----------
    filename :string (optional)
        loation to save the data
    url: string (optional)
        web location of the data
    force_download: bool (optional)
        if True, force redownload of data

    Returns
    -------
    data: pandas.DataFrame
        The fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv("Fremont.csv", index_col="Date")
    try:
        data.index = pd.to_datetime(data.index, format="%m/%d/%Y %H:%M:%S %p")
    except TypeError:
        data.index = pd.to_datetime(data.index)

    data.columns = ["West", "East"]
    data["Total"] = data["West"] + data["East"]
    return data
