#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:03:58 2020

@author: paulunterla
"""
def dataread():
    import pandas as pd
    import psycopg2

    # connect to database and input data TM 0-15000 by selection
    conn = psycopg2.connect(user = "postgres", password='40tacana92', host = "localhost", port = "5432",
                        database = "TBM_data")

    sql = "select id, stroke_nr, p_rsz_l, p_rsz_r, tunnellength, date from tbmdata_p_revised where drift_rate = 0 and drift_power = 0 and penetration = 0 and stroke_nr between 0 and 9105 order by id asc;"

    data = pd.read_sql_query(sql, conn)
    conn = None

    print('Daten eingelesen')
    
    return data

