#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:11:01 2017

@author: bhumihar
"""

import pandas as pd
import numpy as np
from matplotlib import pylab as plt
import matplotlib as mpl

immigrants_df = pd.read_csv('arrests.csv')
#print(immigrants_df.head())

immigrants_df['Sector'].fillna('All', inplace=True)
immigrants_df_m = immigrants_df[(immigrants_df.Sector=='All')].values

immigrants_df_m = np.delete(immigrants_df_m, [1,2], axis=1)
year_c = np.array(np.arange(2000,2017))

all_immigrant = np.array([immigrants_df_m[:,0]])
mex_immigrant = np.array([immigrants_df_m[:,0]])
l1 = np.array([immigrants_df_m[:,1]])
l2 = np.array([immigrants_df_m[:,2]])
all_immigrant = np.concatenate((all_immigrant.T, l1.T), axis=1)
mex_immigrant = np.concatenate((mex_immigrant.T, l2.T), axis=1)
for val in range(2,len(year_c)+1) :
    i = 2*val-1;
    j = 2*val
    l1 = np.array([immigrants_df_m[:,i]])
    l2 = np.array([immigrants_df_m[:,j]])
    all_immigrant = np.concatenate((all_immigrant, l1.T), axis=1)
    mex_immigrant = np.concatenate((mex_immigrant, l2.T), axis=1)

s_list = ['b','g','r','cd']
legend_list = []
mpl.use('GTKAgg')
for i in range(4):
    legend_list = legend_list + [str(mex_immigrant[i,0])]
    plt.plot(year_c,np.log(mex_immigrant[i,1:].astype(int)),s_list[i],label=str(mex_immigrant[i,0]))
    plt.grid(True)
        # give plot a title
    plt.title('Number of Ilegal Iimigrants in Last 16 Years(in Log Scale)')
        # make axis labels
    plt.xlabel('Year')
    plt.ylabel('Number of Ilegal Iimigrants')
    # set axis limits
    plt.xlim(2000,2016)
    plt.ylim(6, 16)

print(legend_list)
# make legend
plt.legend(loc='upper left')
# show the plot on the screen
plt.show()