import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(merged):
    merged = pd.read_csv('../data/processed/merged.csv')
    
    df_2017 = (
        merged[['Name', 'Rk_2017', 'G_2017', 'A_2017', 'P_2017']]
        .assign(Points=lambda x: x.G_2017 + x.A_2017)
        .sort_values('Points', ascending=False)
        .reset_index(drop=True)
        .loc[:, ['Name', 'Rk_2017', 'Points']]
        .rename(columns={'Rk_2017': 'Ranking 2017'})
    )

    
    df_2018 = (
        merged[['Name', 'Rk_2018', 'G_2018', 'A_2018', 'P_2018']]
        .assign(Points=lambda x: x.G_2018 + x.A_2018)
        .sort_values('Points', ascending=False)
        .reset_index(drop=True)
        .loc[:, ['Name', 'Rk_2018', 'Points']]
        .rename(columns={'Rk_2018': 'Ranking 2018'})
    )

    
    df = pd.concat([df_2017, df_2018], axis=1)

    return df