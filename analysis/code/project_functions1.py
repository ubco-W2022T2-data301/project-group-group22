import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime, timedelta

def load_and_process(csv_path1, csv_path2):
    clean2017 = pd.read_csv(csv_path1)
    clean2018 = pd.read_csv(csv_path2)
    
    clean2017['Year'] = 2017
    clean2018['Year'] = 2018

    df1 = (
        pd.concat([clean2017,clean2018], ignore_index = True)
        .sort_values(by=['Name'],ignore_index = True)
        
    )
  
    
    #Here we converting SH% from a percentage to a decimal to use in future calculations
    df2 = (
    df1.assign(TOI=df1['TOI'].apply(lambda x:round((datetime.strptime(x, "%M:%S")).minute+(datetime.strptime(x,"%M:%S")).second/60,2)))
        .assign(SH=df1['SH%'].apply(lambda x: round(float(x[:-1])/100, 4)))
        .drop(['SH%'],axis=1)
        .rename(columns={"SH": "SH%"})
        
    )
    
    return df2

    
    
    
    