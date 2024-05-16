# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:48:19 2023

@author: ADMIN
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t as t_dist
#................

def UVA_numeric(data, var_group):
  ''' 
  Univariate_Analysis_numeric
  takes a group of variables (INTEGER and FLOAT) and plot/print all the descriptives and properties along with KDE.

  Runs a loop: calculate all the descriptives of i(th) variable and plot/print it
  '''

  #size = len(var_group)
  #plt.figure(figsize = (7*size, 3), dpi = 100)
  
  #looping for each variable
  for j,i in enumerate(var_group):
    
    # calculating descriptives of variable
    mini = data[i].min()
    maxi = data[i].max()
    ran = data[i].max()-data[i].min()
    mean = data[i].mean()
    median = data[i].median()
    st_dev = data[i].std()
    skew = data[i].skew()
    kurt = data[i].kurtosis()

    # calculating points of standard deviation
    points = mean-st_dev, mean+st_dev

    #Plotting the variable with every information
    #plt.subplot(1, size, j+1)
    sns.kdeplot(x=data[i], fill=True)
    sns.lineplot(x=points, y=[0,0], color = 'black', label = "std_dev")
    sns.scatterplot(x=[mini,maxi], y=[0,0], color = 'orange', label = "min/max")
    sns.scatterplot(x=[mean], y=[0], color = 'red', label = "mean")
    sns.scatterplot(x=[median], y=[0], color = 'blue', label = "median")
    plt.xlabel('{}'.format(i), fontsize = 20)
    plt.ylabel('density')
    plt.title('within 1 std_dev = {}; kurtosis = {};\nskew = {}; range = {}\nmean = {}; median = {}'.format((round(points[0],2),round(points[1],2)),
                                                                                                   round(kurt,2),
                                                                                                   round(skew,2),
                                                                                                   (round(mini,2),round(maxi,2),round(ran,2)),
                                                                                                   round(mean,2),
                                                                                                   round(median,2)))
    plt.show()
    #.....
    
def Normality(data, var_group):
    ''' 
    Univariate_Analysis_numeric
    takes a group of variables (INTEGER and FLOAT) and plot/print all the descriptives and properties along with KDE.

    Runs a loop: calculate all the descriptives of i(th) variable and plot/print it
    '''
    plt.figure(figsize = (10, 10), dpi = 200)
      
    #looping for each variable
    for j,i in enumerate(var_group):
        # calculating descriptives of variable
        mean = data[i].mean()
        median = data[i].median()
        mode = data[i].mode()
        skew = data[i].skew()
        kurt = data[i].kurtosis()
        ks = stats.kstest(data[i], cdf='norm')
        sw = stats.shapiro(data[i])

        #Plotting the variable with every information
        sm.qqplot(data=data[i], xlabel='Theoretical Quatiles', ylabel = i, line='q')
        plt.title('Kolmogorov-Smirnov = {}; \nShapiro-Wilk = {};\nkurtosis = {}; skew = {}; \nmean = {}; median = {}: mode = {}'.format(
                                                                                                       ks, 
                                                                                                       sw, 
                                                                                                       round(kurt,2),
                                                                                                       round(skew,2),
                                                                                                       round(mean,2),
                                                                                                       round(median,2),                                                                                                   round(mean,2),
                                                                                                       round(mode,2)
                                                                                                       )
            )

#.......

def UVA_category(data, var_group):

  '''
  Univariate_Analysis_categorical
  takes a group of variables (category) and plot/print all the value_counts and barplot.
  '''
  # setting figure_size
  plt.figure(figsize = (10, 10), dpi = 200)

  # for every variable
  for j,i in enumerate(var_group):
    norm_count = data[i].value_counts(normalize = True)
    n_uni = data[i].nunique()

  #Plotting the variable with every information
    sns.barplot(x=norm_count.index , y=norm_count, 
                order = norm_count.index, palette='Pastel1')
    plt.ylabel('Fraction/Percentage', fontsize = 20)
    plt.xlabel('{}'.format(i), fontsize = 20)
    plt.title('n_uniques = {} \n Percentage \n {};'.format(n_uni,norm_count*100))
    
#.........

def resid_plot(y_true, y_pred):
    resid = pd.DataFrame(np.array(y_true) - np.array(y_pred),
                         columns=['error'])
    n = y_true.shape[0]
    x_ax = range(0, n)
    k = [0 for i in x_ax]
    y_ax = resid.error
    plt.figure(figsize=(10, 6), dpi=120, facecolor='w', edgecolor='b')
    plt.scatter(x_ax, y_ax, label = 'residuals')
    plt.plot(x_ax, k , color = 'red', label = 'regression line' )
    plt.xlabel('fitted points ')
    plt.ylabel('residuals')
    plt.title('Residual plot')
    #plt.ylim(-4000, 4000)
    plt.legend()
    plt.show()
    
    
