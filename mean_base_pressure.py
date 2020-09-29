# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:00:46 2020

@author: paulunterla
"""


def mean_base_pressure(df, tm):
    import pandas as pd
    import numpy as np
    from statistics import mean

    for tunnellength in df.groupby(by='tunnellength'):
        if tunnellength [0] in tm:
            
            data_sort = pd.DataFrame(df[(df['p_rsz_l'].between(15, 55)) &
                                          (df['p_rsz_r'].between(15, 55))])
            p_rsz_rel = data_sort['p_rsz_l'] - data_sort['p_rsz_r']
            mean_p = mean(p_rsz_rel)
            print(mean_p)
            
    return
        
        