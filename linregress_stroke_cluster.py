# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:03:09 2020

@author: Brockybalboa
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:54:49 2020

@author: paulunterla
"""

def cluster_stroke(data):
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from datetime import datetime
    import scipy.stats as sc
    from sklearn.cluster import OPTICS, cluster_optics_dbscan
    from sklearn.preprocessing import StandardScaler, normalize
    from pandas.plotting import register_matplotlib_converters
    register_matplotlib_converters()
    
    data.loc[data['p_rsz_l'] < 0, 'p_rsz_l'] = 0
    data.loc[data['p_rsz_r'] < 0, 'p_rsz_r'] = 0
    strokes = np.arange(0, 9106, 1) # list of desired strokes
    scaler = StandardScaler()
    l_slope = []
    l_intercept =[]
    l_rvalue = []
    l_pvalue = []
    l_stderr = []
    l_stroke_nr = []
    l_label_nr = []
    l_stroke = []
    l_n_clusters = []
    l_tunnellength = []
    l_p_rsc_l = []
    l_p_rsc_r = []
    
    for stroke in data.groupby(by='stroke_nr'):
        #if len(stroke[1]) > 10000 or len(stroke[1]) < 400:
            #strokes + 1
        if len(stroke[1]) < 360:
            strokes + 1
            print(f'stroke {stroke[0]} skipped')
        elif stroke[0] in strokes:
            
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
            optics_model = OPTICS(min_samples = 25, xi = 0.15,
                                  min_cluster_size = 300)
            # training the model
            optics_model.fit(X_scaled)
    
            # step 3: storing the results of the training
            labels = optics_model.labels_
            
            # count number of clusters >= 0, label -1 --> outliers
            n_clusters = len(set(labels))- (1 if -1 in labels else 0)
            l_n_clusters.append(n_clusters)
            l_stroke.append(stroke[0])
            
            # create new column with cluster numbers
            X_unsc['labels'] = labels
            # reconvert date
            X_unsc['date'] = pd.to_datetime(X_unsc['date_conv'], unit='s')
            # drop rows where label = -1 (outliers)
            X_unsc = X_unsc[X_unsc.labels != -1]
        
            
            #print(f'stroke {stroke[0]} clustering done')
            
                            
            for label in X_unsc.groupby(by='labels'):
                if label[0] in labels:
                    slope, intercept, rvalue, pvalue, stderr = sc.linregress(
                        label[1]['p_rsz_r'], label[1]['p_rsz_l'])
                    
                    l_slope.append(slope)
                    l_intercept.append(intercept)
                    l_rvalue.append(rvalue)
                    l_pvalue.append(pvalue)
                    l_stderr.append(stderr)
                    l_stroke_nr.append(stroke[0])
                    l_label_nr.append(label[0])
                    l_tunnellength.append(stroke[1]['tunnellength'].mean())
                    l_p_rsc_r.append(stroke[1]['p_rsz_r'].mean())
                    l_p_rsc_l.append(stroke[1]['p_rsz_l'].mean())
                
                else:
                    print('desired label not in stroke')
                
            
            #print(f'cluster {label[0]} linregress done')
            print(f'stroke {stroke[0]} done')
    
        else:
           print('desired strokes not in dataframe')

    linregress_stroke_cluster = pd.DataFrame({'slope':l_slope,
                                      'stroke_nr':l_stroke_nr,
                                      'intercept':l_intercept,
                                      'rvalue':l_rvalue,
                                      'pvalue':l_pvalue,
                                      'stderr':l_stderr,
                                      'label_nr':l_label_nr,
                                      'tunnellength':l_tunnellength,
                                      'p_rsc_l':l_p_rsc_l,
                                      'p_rsc_r':l_p_rsc_r})
    
    labels_stroke = pd.DataFrame({'stroke_nr':l_stroke,
                                  'n_clusters':l_n_clusters})
    
    linregress_stroke_cluster.to_csv(r'C:\Studium\Masterthesis_2\BBT_Daten\Pyhton\lineregress_stroke\linregress_stroke_cluster_360.csv',
        sep = '\t', encoding = 'utf-8')

    labels_stroke.to_csv(r'C:\Studium\Masterthesis_2\BBT_Daten\Pyhton\lineregress_stroke\labels_stroke_360.csv',
        sep = '\t', encoding = 'utf-8')
    
    return linregress_stroke_cluster, labels_stroke
