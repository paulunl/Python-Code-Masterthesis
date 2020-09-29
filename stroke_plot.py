#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:10:09 2020

@author: paulunterla
"""
'''
def hubplot_georg(data):
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    strokes = np.arange(1, 101, 1)
    cmap = plt.get_cmap('plasma')
    #norm = mpl.colors.Normalize(vmin=0,vmax=400)
    sm = plt.cm.ScalarMappable(cmap=cmap)
    sm.set_array([])
    for stroke in data.groupby(by='stroke_nr'):
        if stroke[0] in strokes:
            fig, ax = plt.subplots(figsize=(8, 6.5))
            ax.scatter(stroke[1]['p_rsz_r'],
                       stroke[1]['p_rsz_l'],
                       c=stroke[1]['date'], edgecolor='black', alpha=0.5, cmap=cmap)
            ax.grid(alpha=0.5)
            ax.set_xlabel('Pressure RSC right [bar]')
            ax.set_ylabel('Pressure RSC left [bar]')
            ax.set_title(f'Hub # {stroke[0]}')
            plt.colorbar(sm)
            plt.tight_layout()
            plt.savefig('strokes'f'/{stroke[0]}.jpg')
            plt.close()
            print(f'stroke {stroke[0]} plotted')
        else:
            print('desired strokes not in dataframe')

    return
'''

def strokeplot(data, strokes):
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from datetime import datetime
    
    data.loc[data['p_rsz_l'] < 0, 'p_rsz_l'] = 0
    data.loc[data['p_rsz_r'] < 0, 'p_rsz_r'] = 0
    cmap = plt.get_cmap('binary')

    xlocator = mdates.AutoDateLocator()
    xformatter = mdates.ConciseDateFormatter(xlocator)
    hours = mdates.HourLocator(interval = 1)
    h_fmt = mdates.DateFormatter('%H:%M')
    
    for stroke in data.groupby(by='stroke_nr'):
        if stroke[0] in strokes:
            xmin = min(stroke[1]['date'])
            xmax = max(stroke[1]['date'])
            ymax = max(max(stroke[1]['p_rsz_r']), max(stroke[1]['p_rsz_l'])) + 5
            ymin = min(min(stroke[1]['p_rsz_r']), min(stroke[1]['p_rsz_l']))
            xmin_cbar = xmin.strftime('%H:%M')
            xmax_cbar = xmax.strftime('%H:%M')
            linestyle = ['--']

            fig = plt.figure(figsize=(10, 10))
            ax1 = plt.axes([0.1, 0.51, 0.45, 0.45])
            ax1.scatter(stroke[1]['p_rsz_r'], stroke[1]['p_rsz_l'],
                        c=stroke[1]['date'], s=100, cmap=cmap
                        )
            ax1.grid(alpha=0.5, color='black')
            ax1.set_axisbelow(True)
            ax1.set_xlabel('Pressure RSC right [bar]')
            ax1.set_ylabel('Pressure RSC left [bar]')
            ax1.set_title(f'stroke # {stroke[0]}')
            ax1.set_xlim([0, ymax])
            ax1.set_ylim([0, ymax])
            #ax1.set_facecolor('lightgray')
            ax3 = plt.axes([0.6, 0.51, 0.02, 0.45])
            #ax3.yaxis_date('%d.%m.%Y %H:%M:%S')
            #ax3.set_yticks([xmin, xmax])
            #ax3.yaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            cbar = mpl.colorbar.ColorbarBase(ax3, cmap=cmap, ticks=(0, 1))
            #mpl.colorbar.Colorbar(ax3, cmap)
            #cbar.ax.yaxis_date('%Y-%M-%D %H:%M:%S')
            #mpl.colorbar.ColorbarBase.set_ticks(xmin, xmax, update_ticks=True)
            cbar.ax.set_yticklabels([xmin_cbar, xmax_cbar])
            #cbar.ax.set_yticks(xmin, xmax)
            #cbar.ax.yaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            ax2 = plt.axes([0.1, 0.05, 0.45, 0.39])
            ax2.scatter(stroke[1]['date'], stroke[1]['p_rsz_r'], color='black',
                        s=5, label='p_rsc_r')
            #ax2.plot(stroke[1]['date'], stroke[1]['p_rsz_r'], color='black',
                     #lw=3, label='p_rsc_r')
            ax2_1 = ax2.twinx()
            ax2.scatter(stroke[1]['date'], stroke[1]['p_rsz_l'], color='grey',
                        s=5, label='p_rsc_l')
            #ax2_1.plot(stroke[1]['date'], stroke[1]['p_rsz_l'], color='grey',
                       #lw=3, label='p_rsc_l')
            ax2.set_ylabel('Pressure RSC [bar]')
            ax2.set_xlim([xmin, xmax])
            ax2.set_ylim([0, ymax])
            ax2.grid(alpha=0.5, color='black')
            ax2.set_axisbelow(True)
            #ax2_1.set_ylabel('Pressure RSC left [bar]')
            ax2_1.set_ylim([0, ymax])
            ax2.xaxis.set_major_locator(hours)  
            ax2.xaxis.set_major_formatter(h_fmt)
            ax2.legend(loc='lower right', fontsize='medium')
            #ax2_1.legend(loc='lower left', fontsize='medium')
            #ax2.set_facecolor('lightgray')
            #fig.legend(loc='best')
            
            
            
            ''' slope, intercept = np.polyfit(np.array(stroke[1]['p_rsz_r']),
                              np.array(stroke[1]['p_rsz_l']), deg=1)
            
            a, b = np.polyfit(ymax - 5, ymin, deg=1)
            
            f = lambda x: slope*x + intercept
            x = np.array(stroke[1]['p_rsz_r'])
            ax1.plot(x, f(x), c='black', linewidth=1, alpha=0.8)
            '''
            
            #fig.autofmt_xdate()
            plt.savefig('strokes/p_rev_non_neg'f'/{stroke[0]}_non_neg.png',
                        bbox_inches = 'tight', dpi=600)
            plt.savefig('strokes/p_rev_non_neg'f'/{stroke[0]}_non_neg.pdf',
                        bbox_inches = 'tight', dpi=600)
            plt.close()
            print(f'stroke {stroke[0]} plotted')
        else:
            print('desired strokes not in dataframe')

    return


