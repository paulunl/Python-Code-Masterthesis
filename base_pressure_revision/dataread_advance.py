# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:22:35 2020

@author: paulunterla
"""


def dataread():
    import pandas as pd
    import psycopg2

    # connect to database and input data TM 0-15000 by selection
    conn = psycopg2.connect(user = "postgres", password='40tacana92', host = "localhost", port = "5432",
                        database = "TBM_data")

    sql = "select tbmdata_p_revised.* from tbmdata_p_revised where tunnellength between 8000 and 8200 and drift_rate != 0 and drift_power != 0 and penetration != 0 order by id asc;"

    df = pd.read_sql_query(sql, conn)
    conn = None

    print('data_read')
    
    return df

