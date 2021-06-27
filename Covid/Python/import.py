# Imports
import pandas as pd
from sqlalchemy import create_engine

# Instantiate sqlachemy.create_engine object
engine = create_engine(
    'postgresql://admin:secret@localhost:5433/covid')

# Create an iterable that will read "chunksize=1000" rows
# at a time from the CSV file
for df in pd.read_csv("/home/gins/Learning/Data_Science/Learning/DataScience/Covid/Python/covid-data.csv",  chunksize=1000):
    df.to_sql(
        'covid_dataset',
        engine,
        index=False,
        if_exists='append'  # if the table already exists, append this data
    )
