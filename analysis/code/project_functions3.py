import pandas as pd
import numpy as np
from datetime import datetime

# WIP

# Its expected that path 1 will be the raw 2017 data and path 2 will be raw 2018 data (Data301ProjectData2017 and Data301ProjectData2018)
def load_and_merge3(path1csv, path2csv):
    df1 = pd.read_csv(path1csv)
    df2 = pd.read_csv(path2csv)
    
    missingListFrame1 = list(df1[~(df1['Name'].isin(df2['Name']))].index.values)
    missingListFrame2 = list(df2[~(df2['Name'].isin(df1['Name']))].index.values)
    
    # --- Data Frame 1 Start ---

    df1 = (pd.DataFrame(df1)
            .drop(index=missingListFrame1)
            .sort_values(by='Name', ignore_index=True)
            .reset_index(drop=True)
            .rename(columns={"SH%":"SH"})
        )
    
    df1['TOI'] = (df1['TOI']
                  .apply(lambda x : datetime.strptime(x, '%M:%S'))
                  .apply(lambda x : round((x.minute*60)+x.second, 0))
                )
    
    df1['SH'] = (df1['SH']
                  .apply(lambda x : float(x.strip('%')))
                )
    
    # --- Data Frame 1 End ---
    
    # --- Data Frame 2 Start ---
    
    df2 = (pd.DataFrame(df2)
            .drop(index=missingListFrame2)
            .sort_values(by='Name', ignore_index=True)
            .reset_index(drop=True)
            .rename(columns={'SH%':'SH'})
        )
    
    df2['TOI'] = (df2['TOI']
                  .apply(lambda x : datetime.strptime(x, '%M:%S'))
                  .apply(lambda x : round((x.minute*60)+x.second, 0))
                )
    
    df2['SH'] = (df2['SH']
                  .apply(lambda x : float(x.strip('%')))
                )

    # --- Data Frame 2 End ---
    
    assert df1['Name'].equals(df2['Name']) # Verify both dataframes have the exact same number of players before merging
    
    # --- Data Frame Merging ---
    
    merged = (pd.DataFrame(df1)
              .merge(df2, on='Name', suffixes=['_2017', '_2018'])
              .sort_values(by='Name', ignore_index=True)
              .set_index('Name')
              .reset_index(drop=False)
            )
    
    return merged