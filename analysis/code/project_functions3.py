import pandas as pd
import numpy as np

# WIP

# Its expected that path 1 will be the raw 2017 data and path 2 will be raw 2018 data (Data301ProjectData2017 and Data301ProjectData2018)
def load_and_merge3(path1csv, path2csv):
    df1 = pd.read_csv(path1csv)
    df2 = pd.read_csv(path2csv)
    

    df1 = (df1
        .drop(df1[~df1['Name']
        .isin(df2['Name'])].index)
        .sort_values(by='Name', ignore_index=True)
        .rename(columns={"SH%":"SH"}, inplace=True)
        )
    
    df2 = (df2
        .drop(df2[~df2['Name']
        .isin(df1['Name'])].index)
        .sort_values(by='Name', ignore_index=True)
        .rename(axis=1, columns={'SH%':'SH'}, inplace=True)
        )
    
    merged = (df1
              .merge(df2, on='Name', suffixes=['_2017', '_2018'])
              .sort_values(by='Name', ignore_index=True)
              .set_index('Name')
              .reset_index()
            )
    
    return merged