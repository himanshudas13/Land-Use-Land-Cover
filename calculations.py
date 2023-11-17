
import pandas as pd
import datetime
import numpy as np


def data_set_separate(dataset):
    dataframe = dataset.copy()
    dataframe["Year"] = dataframe['date'].dt.year
    dataframe["Month"] = dataframe['date'].dt.month
    dataframe["Date_no"] = dataframe['date'].dt.day
    # dataframe["Hour"] = dataframe['DateTime'].dt.hour
    return dataframe

def find_ann_sum(dataset, year):
    dataframe = dataset.copy()
    dataframe = dataframe[dataframe["Year"] == year]
    sum_result = np.sum(dataframe['rainfall'])
    return sum_result


def compute_r(df):
    df["Annual R-Factor"] = 1.2 * (df["Rainfall"]) + 0.8