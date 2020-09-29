# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:12:42 2020

@author: paulunterla
"""

import numpy as np
from dataread_advance import dataread
from plot_advance import plot
from mean_base_pressure import mean_base_pressure

if __name__ == '__main__':
    df = dataread()
    plot(df, 8000, 8200)
    #tm = np.arange(0, 1000, 100)
    #mean_base_pressure(df, tm)
    
    print('end')
    
