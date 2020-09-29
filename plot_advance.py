# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:43:49 2020

@author: paulunterla
"""

def plot(df, tm_min, tm_max):
    import matplotlib.pyplot as plt
    import numpy as np
    
    df.loc[df['p_rsz_l'] < 0, 'p_rsz_l'] = 0
    df.loc[df['p_rsz_r'] < 0, 'p_rsz_r'] = 0    
    p_rsc_r = df['p_rsz_r']
    p_rsc_r_mean = p_rsc_r.rolling(5).median()
    p_rsc_l = df['p_rsz_l']
    p_rsc_l_mean = p_rsc_l.rolling(5).median()
    tm = df['tunnellength']
    stroke_nr = df['stroke_nr']
    path_rsc_l = df['path_rsz_l']
    p_max = max(max(df['p_rsz_r']), max(df['p_rsz_l'])) + 5
    p_min = min(min(df['p_rsz_r']), min(df['p_rsz_l']))
    path_min = min(df['path_rsz_l'])
    path_max = max(df['path_rsz_l']) + 5
    stroke_nr_max = max(df['stroke_nr'])
    stroke_nr_min = min(df['stroke_nr'])
    
    fig, ax = plt.subplots(1, 1, figsize = (10, 5), dpi=600)
    
    #ax.set_title('advance_data')
    #ax.scatter(tm, p_rsc_r, c='black', alpha=0.05, s=4)
    #ax.scatter(tm, p_rsc_l, c='grey', alpha=0.05, s=0.5)
    ax.plot(tm, p_rsc_r_mean, linewidth=1, label='P_RSC_right', color='black')
    ax.plot(tm, p_rsc_l_mean, linewidth=1, label='P_RSC_left', color='grey')
    ax.set_xlabel('tunnel meter [m]')
    ax.set_ylabel('pressure [bar]')
    ax.set_xticks(np.arange(tm_min, tm_max+1, 50))
    ax.set_xticks(np.arange(tm_min, tm_max+1, 25), minor=True)
    ax.set_yticks(np.arange(0, p_max, 20))
    ax.set_yticks(np.arange(0, p_max, 10), minor=True)
    ax.set_xlim(tm_min, tm_max)
    ax.set_ylim(0, p_max)
    ax.grid(alpha=0.5)
    #ax.grid(which='minor', alpha=0.5, linestyle='--')
    #ax.axhline(y=20, color='black', linestyle='--', linewidth=0.8,
    #           label='base_pressure')
    
    '''
    ax1 = ax.twinx()
    ax1.plot(tm, path_rsc_l, linewidth=1, label='path_RSC_left', color='black',
             linestyle='dotted', alpha=0.8)
    ax1.set_ylabel('path RSC_left [mm]')
    #ax1.axhline(y=120, color='black', linestyle='-.', linewidth=1,
                #label='< 120 mm = overcutting')
    ax1.set_ylim(path_min, path_max)
    ax1.set_yticks(np.arange(0, path_max, 20))
    ax1.set_yticks(np.arange(0, 121, 10), minor=True)
    #ax1 = ax.twiny()
    #ax1.set_xticks(np.arange(stroke_nr_min, stroke_nr_max, 2))
    #ax1.set_xticks(np.arange(stroke_nr_min, stroke_nr_max, 1), minor=True)
    '''
    ax.legend(loc='upper right')
    #ax1.legend(loc='upper right')
    
    fig.tight_layout()
    plt.savefig(''f'{tm_min}_'f'{tm_max}_rev_non_neg1.png', bbox_inches = 'tight')
    print('fig_plotted')
    return

