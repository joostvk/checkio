# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:28:35 2018

@author: JOOST
"""

def sun_angle(tijdstip):
    hh, mm = map(int,tijdstip.split(":"))
    return round(((hh-6) * 15) + ((mm/60) * 15),2) if (hh >= 6  and (hh <= 17 or tijdstip =='18:00')) else "I don't see the sun!"



import pandas as pd
import quandl


df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close','Adj. Volume']]
df.head()


from datetime import datetime
from datetime import time
x = "12:15"
t1 = datetime.strptime(x, '%H:%M')
t2 = time.strftime(x, '%H:%M')
dir(time)
time.strftime?
dir(dt)


sun_angle("17:59")

tijdstip = '18:15'
hh, mm = map(int,tijdstip.split(":"))
type(hh)


sun_angle("07:00") == 15
sun_angle("18:00") == 93.75
