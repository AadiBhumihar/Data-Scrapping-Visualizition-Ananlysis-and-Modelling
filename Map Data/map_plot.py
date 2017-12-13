#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:25:11 2017

@author: bhumihar
"""


import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap

import numpy as np
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

m = Basemap(projection='mill',
            llcrnrlon=-180. ,llcrnrlat=-60,
            urcrnrlon=180. ,urcrnrlat=80.)

cities = ['London', 'New York', 'Madrid', 'Cairo', 'Moscow',
          'Delhi', 'Dakar']
lat = [51.507778, 40.716667, 40.4, 30.058, 55.751667,
       28.61, 14.692778]
lon = [-0.128056, -74, -3.683333, 31.229, 37.617778,
       77.23, -17.446667]

x, y = m(lon, lat)

m.drawcoastlines()
m.fillcontinents()
m.drawcountries(linewidth=2)
# draw states boundaries (America only)
#m.drawstates()

plt.plot(x, y, 'b.')

for city, xc, yc in zip(cities, x, y):
# draw the city name in a yellow (shaded) box
  plt.text(xc+250000, yc-150000, city,bbox=dict(facecolor='yellow', alpha=0.5))
