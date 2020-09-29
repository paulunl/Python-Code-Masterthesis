#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:31:49 2020

@author: paulunterla
"""

def plot_hist(linregress_stroke):
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.neighbors import KernelDensity
    from sklearn.model_selection import GridSearchCV
    import pandas as pd

    linregress_stroke = linregress_stroke[linregress_stroke.slope != 0]
    linregress_stroke1 = linregress_stroke[linregress_stroke.rvalue < -0.1]
    linregress_stroke2 = linregress_stroke[linregress_stroke.rvalue > 0.1]
    linregress_stroke = pd.concat([linregress_stroke1, linregress_stroke2],
                                  ignore_index = True)
    linregress_stroke = linregress_stroke[linregress_stroke.stderr < 5]
    slope = np.nan_to_num(linregress_stroke['slope']) #convert NaN to 0


    
    grid = GridSearchCV(KernelDensity(),
                        {'bandwidth': slope}, cv=100)
    
    x_grid = np.linspace(-25, 25, 6191) # range of slope value and total number of strokes
    
    density = KernelDensity(kernel='gaussian', bandwidth=0.08).fit(slope.reshape(-1,1)) # fit the Kernel Density model on the data
    density_score = density.score_samples(x_grid.reshape(-1,1)) # evaluate the log density model on the data
    
    kde = grid.estimator # kernel density estimation
    pdf = np.exp(density_score) # probability density function
    
    fig, ax = plt.subplots(dpi=600)
    ax.plot(x_grid, pdf, linewidth=2, alpha=0.8, color='black')
    ax.hist(slope, 500, fc='darkgray', histtype='stepfilled', alpha=1, density=1, ec='black')
    #ax.legend(loc='upper left')
    ax.set_xticks(np.arange(-4, 6, 1))
    ax.set_xlim(-4, 5)
    ax.set_xlabel('slope')
    ax.set_ylabel('normalized density')
    ax.set_title('slope distribution where corcoef <-0.1; >0.1')
    ax.grid()
    ax.axvline(x=1, color='black', linestyle='-', linewidth=1, label='LIP')
    ax.text(1.1, 0.71, ''f'LIP')
    fig.tight_layout()
    plt.savefig('C:\Studium\Masterthesis_2\BBT_Daten\Pyhton\lineregress_stroke\plots_slope_hist\hist_slope_cluster5.png', dpi=600)
    plt.savefig('C:\Studium\Masterthesis_2\BBT_Daten\Pyhton\lineregress_stroke\plots_slope_hist\hist_slope_cluster5.pdf', dpi=600)

    print('fig_plotted')
    return