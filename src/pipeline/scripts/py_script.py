import pandas as pd 
from pandas import DataFrame

def ingest_data() -> DataFrame:
    """Function that returns a DF"""
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100000)
    print(df.head())
    print(df.count())
    return df







