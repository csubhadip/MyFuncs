# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:56:06 2023

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

#.....

def corr_map(data):
    for i in ['pearson', 'spearman', 'kendall']:
        corr = data.dropna().corr(method = i)
        plt.figure(figsize=(20, 10), dpi=200)
        sns.heatmap(corr, annot=True, cmap='Blues')
        plt.title(i, fontsize=12)
        plt.show()
#.....

# Two-Sample Z Test
def TwoSampZ(X1, X2, sigma1, sigma2, N1, N2, tail):
  '''
  takes mean, standard deviation, number of observations of the two samples 
  and returns p-value calculated for 2-sampled Z-Test.
  If tail=1 it gives one tailed p-val
  If tail is anything else it gives 2 tailed p-value
  '''
  from numpy import sqrt, abs, round
  from scipy.stats import norm
  ovr_sigma = sqrt(sigma1**2/N1 + sigma2**2/N2)
  #print(ovr_sigma)
  z = (X1 - X2)/ovr_sigma
  #print(z)
  if tail==1:
      if z < 0:
          pval = norm.cdf(z)
      else:
          pval = 1 - norm.cdf(z)
  elif tail==2:
      pval = 2*(1 - norm.cdf(abs(z)))
  else:
      print('Enter 1 for one-tailed test or 2 for two-tailed test')
      
  return round(pval, 3)
#
def TwoSampT(X1, X2, sd1, sd2, n1, n2, tail):
  '''
  takes mean, standard deviation, and number of observations and returns p-value calculated for 2-sample T-Test
  '''
  from numpy import sqrt, abs, round
  from scipy.stats import t as t_dist
  ovr_sd = sqrt(sd1**2/n1 + sd2**2/n2)
  t = (X1 - X2)/ovr_sd
  df = n1+n2-2
  if tail==1:
      if t < 0:
          pval = t_dist.cdf(t, df)
      else:
          pval = 1 - t_dist.cdf(t, df)
  elif tail==2:
      pval = 2*(1 - t_dist.cdf(abs(t), df))
  else:
      print('Enter 1 for one-tailed test or 2 for two-tailed test')
      
  return round(pval, 3)
#
def Bivariate_cont_cat(data, cont, cat, category, tail):
  #creating 2 samples
  x1 = data[cont][data[cat]==category][:]
  x2 = data[cont][(data[cat]!=category)][:]
  
  #calculating descriptives
  n1, n2 = x1.shape[0], x2.shape[0]
  m1, m2 = x1.mean(), x2.mean()
  from statistics import stdev, pstdev
  std1, std2 = stdev(x1), stdev(x2)
  pstd1, pstd2 = pstdev(x1), pstdev(x2)
  #calculating p-values
  t_p_val = TwoSampT(m1, m2, std1, std2, n1, n2, tail)
  z_p_val = TwoSampZ(m1, m2, pstd1, pstd2, n1, n2, tail)

  #table
  table = pd.pivot_table(data=data, values=cont, columns=cat, aggfunc = np.mean)

  #plotting
  plt.figure(figsize = (15,6), dpi=140)
  
  #barplot
  plt.subplot(1,2,1)
  sns.barplot(y=[m1, m2], x = [str(category),'not {}'.format(category)])
  plt.ylabel('mean {}'.format(cont))
  plt.xlabel(cat)
  plt.title('tail = {} \nt-test p-value = {} \n z-test p-value = {}\n {}'.format(tail, t_p_val,
                                                                z_p_val,
                                                                table))
  
  # boxplot
  plt.subplot(1,2,2)
  sns.boxplot(x=cat, y=cont, data=data)
  plt.title('categorical boxplot')
  plt.show()
























    