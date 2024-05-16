# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:17:38 2023

@author: ADMIN
"""
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd


def VIF(X):
# VIF dataframe 
    vif_data = pd.DataFrame() 
    vif_data["feature"] = X.columns 
  
# calculating VIF for each feature 
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))] 
    print(vif_data)