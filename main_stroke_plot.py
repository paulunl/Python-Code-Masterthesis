# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:23:19 2020

@author: paulunterla
"""

from Dataread_stroke_plot import dataread
from stroke_plot import strokeplot
from dbscan_cluster import strokeplot_dbscan
from optics_cluster import strokeplot_optics
from optics_cluster_rel import strokeplot_optics_rel
from optics_date import strokeplot_optics_date
from visualization import visualization_optics
from optics_cluster_nocbar import strokeplot_optics_nocbar
import numpy as np

if __name__ == '__main__':
    
    strokes = np.arange(1259, 1261, 1)
    
    data = dataread()
    strokeplot(data, strokes)
    #strokeplot_dbscan(data, strokes)
    #strokeplot_optics(data, strokes)
    #strokeplot_optics_rel(data, strokes)
    #strokeplot_optics_date(data, strokes)
    #visualization_optics(data, strokes)
    #strokeplot_optics_nocbar(data, strokes)
    
    
    print("end")                                                                    
