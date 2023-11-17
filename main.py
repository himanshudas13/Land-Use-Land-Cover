import pandas as pd
import datetime
import numpy as np

from calculations import data_set_separate,find_ann_sum,compute_r

dataset = pd.read_csv("Book1.csv")
dataset['date'] = pd.to_datetime(dataset['date'], infer_datetime_format=True, errors='coerce')
dataset=data_set_separate(dataset)

sum_data = []
first_row = dataset.head(1)
last_row = dataset.tail(1)

# tasks to do: to replace the 1970 to 1984 thing in for loop into year in 1st row and year in last row
# problem faced: many dates are reported as NaN by pandas dataframe reader

for year in range(1970, 1984):
    rfy= find_ann_sum(dataset, year)
    cur_row = [year, rfy]
    sum_data.append(cur_row)


df=pd.DataFrame(sum_data,columns=["Year","Rainfall"])

compute_r(df)

df.to_csv('R-factor.csv', index=False)

