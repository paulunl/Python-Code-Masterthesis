# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:22:05 2020

@author: paulunterla
"""

def dataread():
    import pandas as pd
    import psycopg2

    conn = psycopg2.connect(user = "postgres", password="40tacana92", host = "localhost", port = "5432",
                        database = "TBM_data")

    sql = "select id, date, stroke_nr, p_rsz_l, p_rsz_r from tbmdata_p_revised where stroke_nr between 1254 and 1260 and drift_rate = 0 and drift_power = 0 and penetration = 0 order by id asc;"

    data = pd.read_sql_query(sql, conn)
    conn = None
    print('data read')
    return data