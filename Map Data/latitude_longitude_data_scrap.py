#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 18:28:52 2017

@author: bhumihar
"""

from urllib.request import urlopen
 
from bs4 import BeautifulSoup
import pandas as pd

	#### function to check that particular <div> has 'class' attribute ####
def has_class(tag):
    return tag.has_attr('class')
    
	#### Intilizing and getting html_data and html_body ####
html = urlopen("https://www.mapsofworld.com/lat_long/india-lat-long.html")
html_data = BeautifulSoup(html, 'html.parser')
html_body = html_data.body


	#### Extracting data having <div> value ####
divv = html_body.find_all('div')

count = 0
for i in range(len(divv)) :
    if((has_class(divv[i])) ):
        if('content_container' in divv[i]['class']) :
            count = i

vall = divv[65].find('table').find('tbody')


	#### Extracting Lat and long value ####
lat_long_l = []
tr_data = vall.find_all('tr')
for i in range(len(tr_data)) :
    lat_loc = tr_data[i].find_all('td') ;
    #print(lat_loc[0].get_text())
    #for j in range(len(lat_loc)) :
    loc1 = lat_loc[0].get_text()
    loc1_lat = lat_loc[1].get_text()
    loc1_lon = lat_loc[2].get_text()
    lat_long_l.append({'Location':loc1, 'Latitude':loc1_lat, 'Longitude':loc1_lon})
    loc2 = lat_loc[3].get_text()
    loc2_lat = lat_loc[4].get_text()
    loc2_lon = lat_loc[5].get_text()
    lat_long_l.append({'Location':loc2, 'Latitude':loc2_lat, 'Longitude':loc2_lon})     
        
        
        #### creating Dataframe and append lat_lon data in this#####
lat_lon_data = pd.DataFrame(lat_long_l)

	#### Write Dataframe to csv file #####
file_csv = 'lat_lon.csv'
lat_lon_data.to_csv(file_csv)
