# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:54:49 2020

@author: paulunterla
"""

def strokeplot_optics(data, strokes):
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from datetime import datetime
    from sklearn.cluster import OPTICS, cluster_optics_dbscan
    from sklearn.preprocessing import StandardScaler, normalize
    from pandas.plotting import register_matplotlib_converters
    import matplotlib.patheffects as pe
    register_matplotlib_converters()
    
    data.loc[data['p_rsz_l'] < 0, 'p_rsz_l'] = 0
    data.loc[data['p_rsz_r'] < 0, 'p_rsz_r'] = 0
    cmap = plt.get_cmap('binary')
    xlocator = mdates.AutoDateLocator()
    xformatter = mdates.ConciseDateFormatter(xlocator)
    scaler = StandardScaler()
    hours = mdates.HourLocator(interval = 1)
    h_fmt = mdates.DateFormatter('%H:%M')
    
    for stroke in data.groupby(by='stroke_nr'):
        if stroke[0] in strokes:
            
            ''' OPTICS clustering ''' 
            # step 1: preprocessing the Data
            X_unsc = pd.DataFrame(stroke[1][['p_rsz_r', 'p_rsz_l', 'date']])
            # converting datetime to int64
            X_unsc['date_conv'] = X_unsc['date'].astype('int64') // 10**9
            X_unsc = X_unsc.drop(['date'], axis=1)
            # scaling the Data
            X_scaled = scaler.fit_transform(X_unsc)
            # converting numpy array into a pandas DataFrame
            X_scaled = pd.DataFrame(X_scaled)
            # renaming the columns
            X_scaled.columns = X_unsc.columns
            
            # step 2: building the clustering model
            optics_model = OPTICS(min_samples = 25, xi = 0.19,
                                  min_cluster_size = 300)
            # training the model
            optics_model.fit(X_scaled)
    
            # step 3: storing the results of the training
            labels = optics_model.labels_
            # count size of clusters
            counts = np.bincount(labels[labels >= 0])
            # define biggest cluster
            biggest_cluster = np.argsort(-counts)[:1]
            # create new column with cluster numbers
            X_unsc['cluster'] = labels
            # reconvert date
            X_unsc['date'] = pd.to_datetime(X_unsc['date_conv'], unit='s')
            # filter for biggest cluster
            X_bc = X_unsc[X_unsc.cluster.isin(biggest_cluster)]
            
            
            ''' visualizing the results '''
            
            xmin = min(X_bc['date'])
            xmax = max(X_bc['date'])
            ymax = max(max(X_bc['p_rsz_r']), max(X_bc['p_rsz_l'])) + 5
            ymin = min(min(X_bc['p_rsz_r']), min(X_bc['p_rsz_l']))
            xmin_cbar = xmin.strftime('%H:%M')
            xmax_cbar = xmax.strftime('%H:%M')
            fig = plt.figure(figsize=(10, 10))
            ax1 = plt.axes([0.1, 0.51, 0.45, 0.45])
            ax1.scatter(X_bc['p_rsz_r'], X_bc['p_rsz_l'], c = X_bc['date'],
                        s=100, cmap=cmap)
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
            #ax2.scatter(X_bc['date'], X_bc['p_rsz_r'], s=20, facecolors='none',
                        #label='p_rsc_r', edgecolors='black', linewidths=0.3)
            
            ax2.plot(X_bc['date'], X_bc['p_rsz_r'], color='black', lw=3, label='p_rsc_r')
            ax2_1 = ax2.twinx()
            #ax2_1.scatter(X_bc['date'], X_bc['p_rsz_l'],
                           #s=15, label='p_rsc_l', color='grey')
            ax2.plot(X_bc['date'], X_bc['p_rsz_l'], color='grey', lw=3, label='p_rsc_l')
            ax2.set_ylabel('Pressure RSC [bar]')
            ax2.set_xlim([xmin, xmax])
            ax2.set_ylim([0, ymax])
            ax2.grid(alpha=0.5, color='black')
            #ax2.grid(alpha=0.5, which='minor', linestyle='--', color='black')
            ax2.set_axisbelow(True)
            #ax2_1.set_ylabel('Pressure RSC left [bar]')
            ax2_1.set_ylim([0, ymax])
            ax2.xaxis.set_major_locator(hours)
            #ax2.xaxis.set_minor_locator(minutes)  
            ax2.xaxis.set_major_formatter(h_fmt)
            ax2.legend(loc='lower right', fontsize='medium')
            #ax2_1.legend(loc='lower left', fontsize='medium')
            #ax2.set_facecolor('lightgray')
            #fig.legend(loc='best')
            
            
            
            slope, intercept = np.polyfit(np.array(X_bc['p_rsz_r']),
                              np.array(X_bc['p_rsz_l']), deg=1)
            
            #a, b = np.polyfit(ymax - 5, ymin, deg=1)
            
            f = lambda x: slope*x + intercept
            x = np.array(X_bc['p_rsz_r'])
            ax1.plot(x, f(x), c='black', linestyle='solid', linewidth=1.5,
                     path_effects=[pe.Stroke(linewidth=2.5,foreground='white'),
                                   pe.Normal()])
            slope = round(slope, 2)
            ax1.text(23, 260, ''f'slope = {slope}')
            
            #fig.autofmt_xdate()
            plt.savefig('OPTICS_cluster'f'/{stroke[0]}_OPTICS_non_neg.png',
                        bbox_inches = 'tight', dpi=600)
            plt.savefig('OPTICS_cluster'f'/{stroke[0]}_OPTICS_non_neg.pdf',
                        bbox_inches = 'tight', dpi=600)
            plt.close()
            print(f'stroke {stroke[0]}_OPTICS plotted')
        else:
            print('desired strokes not in dataframe')

    return

