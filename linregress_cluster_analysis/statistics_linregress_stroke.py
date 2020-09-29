# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:43:06 2020

@author: paulunterla
"""


import pandas as pd
import statistics

#median, percentages < resp. > LIP for all significant sub-strokes

linregress_stroke = pd.read_csv('linregress_stroke_cluster_all_2.csv')

linregress_stroke = linregress_stroke[linregress_stroke.slope != 0]
linregress_stroke1 = linregress_stroke[linregress_stroke.rvalue < -0.1]
linregress_stroke2 = linregress_stroke[linregress_stroke.rvalue > 0.1]
linregress_stroke = pd.concat([linregress_stroke1, linregress_stroke2],
                              ignore_index = True)
linregress_stroke = linregress_stroke[linregress_stroke.stderr < 5]

median_slope = statistics.median(linregress_stroke['slope'])
print(median_slope)

percent_slopes_smaller_LIP = len(linregress_stroke[linregress_stroke.slope < 1]) / len(linregress_stroke) * 100
percent_slopes_greater_LIP = len(linregress_stroke[linregress_stroke.slope > 1]) / len(linregress_stroke) * 100

print(percent_slopes_greater_LIP, '% greater than LIP')
print(percent_slopes_smaller_LIP, '% smaller than LIP')
print('sum = ', percent_slopes_greater_LIP + percent_slopes_smaller_LIP, '%')


#median, percentages < resp. > LIP for all significant sub-strokes

linregress_stroke = pd.read_csv('linregress_stroke_cluster_735_1120.csv')

linregress_stroke = linregress_stroke[linregress_stroke.slope != 0]
linregress_stroke1 = linregress_stroke[linregress_stroke.rvalue < -0.1]
linregress_stroke2 = linregress_stroke[linregress_stroke.rvalue > 0.1]
linregress_stroke = pd.concat([linregress_stroke1, linregress_stroke2],
                              ignore_index = True)
linregress_stroke = linregress_stroke[linregress_stroke.stderr < 5]

median_slope = statistics.median(linregress_stroke['slope'])
print(median_slope)

percent_slopes_smaller_LIP_2 = len(linregress_stroke[linregress_stroke.slope < 1]) / len(linregress_stroke) * 100
percent_slopes_greater_LIP_2 = len(linregress_stroke[linregress_stroke.slope > 1]) / len(linregress_stroke) * 100

print(percent_slopes_greater_LIP_2, '% greater than LIP between TM 735-1120')
print(percent_slopes_smaller_LIP_2, '% smaller than LIP between TM 735-1120')
print('sum = ', percent_slopes_greater_LIP_2 + percent_slopes_smaller_LIP_2, '%')

