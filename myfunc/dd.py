# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:15:04 2024

@author: ADMIN
"""
import pandas as pd
import numpy as np
import statistics

# %% Supporting functions


def is_blank(series):
    # counting the number of blanks in a series
    for i in series:
        cnt = 0
        if len(str(i).strip()) == 0:
            cnt = cnt + 1
    return cnt


def is_str_na(series):
    # counting the number of string NAs in a series
    for i in series:
        cnt = 0
        if str(i).strip() in ["NA", "na", "Na", "nA", "N/a", "N/A", "n/A", "n/a", "N-A", "n-a", "N-a", "n-A", "N.A", "N.a", "n.A", "n.a"]:
            cnt = cnt + 1
    return cnt


def descriptive(series):
    # counting the number of string NAs in a series
    if (str(series.dtypes) == "object") | (str(series.dtypes) == "datetime64[ns]"):
        lst = []
        for k in series:
            j = len(str(k))
            lst.append(j)
        min_ = min(lst)
        max_ = max(lst)
        range_ = max_ - min_
        mean_ = "NA"
        median_ = "NA"
        mode_ = statistics.mode(lst)
        q1_ = "NA"
        q3_ = "NA"
        std_ = "NA"
        cov_ = "NA"
    else:
        min_ = series.min()
        max_ = series.max()
        range_ = max_ - min_
        mean_ = series.mean()
        median_ = statistics.median(series.dropna(axis=0))
        mode_ = statistics.mode(series)
        q1_ = np.quantile(series.dropna(axis=0), [0.25])[0]
        q3_ = np.quantile(series.dropna(axis=0), [0.75])[0]
        std_ = np.std(series)
        cov_ = round(std_ * 100 / mean_)
    return min_, max_, range_, mean_, median_, mode_, q1_, q3_, std_, cov_


# %% Data Dictionary


def data_dict(df, excel="yes"):
    # Create a data dictionary for the data frame
    # excel = 'yes' or 'no'
    col_ = df.columns
    df_dataDict = {}
    for i in col_:
        df_dataDict[i] = {
            "Type": str(df.dtypes[i]),
            "Rows": len(df[i]),
            "Count": df[i].count(),
            "Null": df[i].isnull().sum(),
            "Blank": is_blank(df[i]),
            "NAs": is_str_na(df[i]),
            "NUnique": df[i].nunique(),
            "Min": descriptive(df[i])[0],
            "Max": descriptive(df[i])[1],
            "Range": descriptive(df[i])[2],
            "Mean": descriptive(df[i])[3],
            "Median": descriptive(df[i])[4],
            "Mode": descriptive(df[i])[5],
            "Q1": descriptive(df[i])[6],
            "Q3": descriptive(df[i])[7],
            "StD": descriptive(df[i])[8],
            "Coeff_Var": descriptive(df[i])[9],
            "Sample": list(pd.Series(df[i].dropna(axis=0).unique()).sample(min(5, df[i].nunique()))),
        }
    df_DD = pd.DataFrame(df_dataDict).T
    if excel == "yes":
        df_DD.to_excel("Data_Dictionary.xlsx", sheet_name="DD", index_label="Variables")

    return df_DD
