#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:14:16 2020

@author: paulunterla
"""

def plot_distr(df_linregress, start, end, TMmin, TMmax):
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import matplotlib as mpl

    tunnellength = df_linregress.loc[start:end]['tunnellength']
    slope = df_linregress.loc[start:end]['slope']
    p_rsz_r = df_linregress.loc[start:end]['p_rsc_r']
    p_rsz_r_mean = p_rsz_r.rolling(3).median()
    p_rsz_l = df_linregress.loc[start:end]['p_rsc_l']
    p_rsz_l_mean = p_rsz_l.rolling(3).median()
    #tunnellength_1 = tunnellength.rolling(5).median()
    slope_mean = slope.rolling(1).median()
    #cmap = plt.get_cmap('seismic')
    #norm = mpl.colors.Normalize(vmin=-3, vmax=5)

    fig, ax1 = plt.subplots(1, 1, figsize=(20, 5), dpi=600)
    #ax1, ax2 = ax.flatten()
    #ax1.scatter(tunnellength, slope, alpha=0.3, s=10, c='grey')
    
    ax1.plot([],[],linewidth=5, label='slope < 1', color='black')
    ax1.plot([],[],linewidth=5, label='slope > 1', color='darkgray')
    ax1.fill_between(tunnellength, slope_mean, 1, where=(slope_mean > 1),
                     facecolor='darkgray')
    ax1.fill_between(tunnellength, slope_mean, 1, where=(slope_mean < 1),
                     facecolor='black')
    ax1.set_yticks(np.arange(-4, 6, 1))
    ax1.set_ylim(-3, 5)
    ax1.set_xlim(TMmin, TMmax)
    ax1.grid(alpha=0.5)
    ax1.set_ylabel('slope')
    ax1.set_xlabel('tunnelmeter [m]')
    ax1.set_title('slope (P_RSC_r vs. P_RSC_l) vs. TM')
    ax1_1 = ax1.twinx()
    ax1_1.set_yticks(np.arange(-4, 6, 1))
    ax1_1.set_ylim(-3, 5)
    ax1.axhline(y=1, color='black', linestyle='--', linewidth=1, label='LIP')
    ax1.legend(fontsize='small')
    #ax.plot(tunnellength, slope, linewidth=0.1)
    '''
    ax2.scatter(tunnellength, p_rsz_r, c='grey', s=5, alpha=0.15, linewidths=0)
    ax2.plot(tunnellength, p_rsz_r_mean, linewidth=1, c='grey', label='P_RSC_r')
    ax2.set_yticks(np.arange(0, 401, 100))
    ax2.grid(alpha=0.5)
    ax2.set_ylim(0, 400)
    ax2.set_xlim(TMmin, TMmax)
    ax2.set_xlabel('Tunnelmeter [m]')
    ax2.set_ylabel('Pressure [bar]')
    ax2.legend(loc='upper right', fontsize='small')
    #ax2.set_title('P_RSC_right and left vs. TM')
    ax2_1 = ax2.twinx()
    ax2_1.scatter(tunnellength, p_rsz_l, c='black', s=5, alpha=0.15, linewidths=0)
    ax2_1.plot(tunnellength, p_rsz_l_mean, linewidth=1, c='black', label='P_RSC_l')
    ax2_1.set_yticks(np.arange(0, 401, 100))
    ax2_1.set_ylim(0, 400)
    ax2_1.set_xlim(TMmin, TMmax)
    ax2_1.legend(loc='upper left', fontsize='small')
    '''
    plt.savefig(f'{TMmin}_{TMmax}_slope_distr_TM_735-1120.png',
                bbox_inches = 'tight', dpi=600)
    plt.savefig(f'{TMmin}_{TMmax}_slope_distr_TM_735-1120.pdf',
                bbox_inches = 'tight', dpi=600)
    return


'''
def plot_hist_TM(df_linregress):
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import matplotlib as mpl

    tunnellength = df_linregress.loc[:1000]['tunnellength']
    slope = df_linregress.loc[:1000]['slope']
    #tunnellength_1 = tunnellength.rolling(5).median()
    #slope_1 = slope.rolling(5).median()
    cmap = plt.get_cmap('seismic')
    norm = mpl.colors.Normalize(vmin=-3, vmax=5)

    fig, ax = plt.subplots(2, 1, figsize=(15, 5))
    ax.scatter(tunnellength, slope, edgecolor='black', alpha=0.7, s=50, c=slope, cmap=cmap, norm=norm)
    ax.set_yticks(np.arange(-4, 6, 1))
    ax.set_ylim(-3, 5)
    ax.grid(alpha=0.5)
    #ax.plot(tunnellength, slope, linewidth=0.1)

    return


def plot_hist_TM(df_linregress):
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import matplotlib as mpl

    tunnellength = df_linregress.loc[:2500]['tunnellength']
    slope = df_linregress.loc[:2500]['slope']
    p_rsz_r = df_linregress.loc[:2500]['p_rsz_r']
    p_rsz_l = df_linregress.loc[:2500]['p_rsz_l']
    #tunnellength_1 = tunnellength.rolling(5).median()
    #slope_1 = slope.rolling(5).median()
    cmap = plt.get_cmap('seismic')
    norm = mpl.colors.Normalize(vmin=-3, vmax=5)

    fig, ax = plt.subplots(2, 1, figsize=(15, 5))
    ax1, ax2 = ax.flatten()
    ax1.scatter(tunnellength, slope, edgecolor='black', alpha=0.7, s=15, c=slope, cmap=cmap, norm=norm)
    ax1.set_yticks(np.arange(-4, 6, 1))
    ax1.set_ylim(-3, 5)
    ax1.set_xlim(0, 2500)
    ax1.grid(alpha=0.5)
    #ax.plot(tunnellength, slope, linewidth=0.1)
    #ax2.scatter(tunnellength, p_rsz_r, c='red', s=5, alpha=0.7, edgecolor='grey')
    ax2.plot(tunnellength, p_rsz_r, linewidth=0.5, c='red')
    ax2.set_yticks(np.arange(0, 401, 100))
    ax2.grid(alpha=0.5)
    ax2.set_ylim(0, 400)
    ax2.set_xlim(0, 2500)
    ax2_1 = ax2.twinx()
    #ax2_1.scatter(tunnellength, p_rsz_l, c='blue', s=5, alpha=0.7, edgecolor='grey')
    ax2_1.plot(tunnellength, p_rsz_l, linewidth=0.5, c='blue')
    ax2_1.set_yticks(np.arange(0, 401, 100))
    ax2.set_ylim(0, 400)
    ax2_1.set_xlim(0, 2500)
    return
    
'''