# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:23:26 2023

@author: ADMIN
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def CORR_ALL(x):
    met = ['pearson', 'spearman', 'kendall']
    for i in met:
        corr = x.dropna().corr(method=i)
        plt.figure(figsize=(20, 10), dpi=200)
        sns.heatmap(corr, annot=True, cmap='Blues')
        plt.title(i, fontsize=12)
        plt.show()
#%%
def CORR_HIGH(x, thresh=.5):
    met = ['pearson', 'spearman', 'kendall']
    high_corr=[]
    for i in met:
        corr = x.dropna().corr(method=i)
        corr = corr.unstack().sort_values(ascending=False)
        corr = pd.DataFrame(corr, columns=[i])
        corr = corr[((-1 < corr[i]) & (corr[i] <= -thresh)) | ((1 > corr[i]) & (corr[i] >= thresh))]
        high_corr.append([i, corr])
        #plt.figure(figsize=(36, 6), dpi=200)
        #sns.heatmap(corr, annot=True, cmap='Blues')
        #plt.title(i, fontsize=12)
        #plt.show()
    return high_corr