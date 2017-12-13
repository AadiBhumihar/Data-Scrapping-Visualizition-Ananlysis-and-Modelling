#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:07:43 2017

@author: bhumihar
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

# Downloaded from http://biogeo.ucdavis.edu/data/gadm2/shp/DEU_adm.zip
fname = '/IND_adm0.shp'

m = Basemap(projection='mill',
            llcrnrlon=-10. ,llcrnrlat=-60,
            urcrnrlon=180. ,urcrnrlat=80.)
m.readshapefile("/home/bhumihar/shpf/IND_adm0","IND_adm0")


