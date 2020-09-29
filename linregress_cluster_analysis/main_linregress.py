#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:07:16 2020

@author: paulunterla
"""

'''
linear regression of pressure in right roofsupporting cylinder (x) vs pressure in
left roofsupporting cylinder (y) for every cluster (optics clustering) in
desired strokes.
if slope bigger 1, then pressure increase in left cylinder bigger
if slope smaller 1, then pressure increase in right cylinder bigger
if slope = 1, then isotropic pressure increase 
'''

from Dataread_linregress import dataread
from linregress_per_stroke import linregress
#from linregress_per_stroke import linregress_2
from hist_plot import plot_hist
from plot_distr_TM import plot_distr
from linregress_stroke_cluster import cluster_stroke


if __name__ == '__main__':
    
    data = dataread()
    #linregress_stroke = linregress(data)
    linregress_stroke, labels_cluster = cluster_stroke(data)
    
    #plot_distr(linregress_stroke, 0, 2811, 0, 5000)
    #plot_distr(linregress_stroke, 2811, 3989, 5000, 10000)
    #plot_distr(linregress_stroke, 3989, 6191, 10000, 15077)



    
    #plot_hist(linregress_stroke)
    #plot_distr(linregress_stroke, 0, 1848, 0, 3000)
    #plot_distr(linregress_stroke, 1848, 3651, 3000, 6000)
    #plot_distr(linregress_stroke, 3651, 5458, 6000, 9000)
    #plot_distr(linregress_stroke, 5458, 7278, 9000, 12000)
    #plot_distr(linregress_stroke, 7278, 9105, 12000, 15077)
    
    
    print("end")
    
    #plot_distr(linregress_stroke, 0, 1095, 0, 3000)
    #plot_distr(linregress_stroke, 1095, 1544, 3000, 6000)
    #plot_distr(linregress_stroke, 1544, 1918, 6000, 9000)
    #plot_distr(linregress_stroke, 1918, 2511, 9000, 12000)
    #plot_distr(linregress_stroke, 2511, 3343, 12000, 15077)