import plotly.figure_factory as ff
import statistics
import pandas as pd
import random
import csv
df=pd.read_csv("data.csv")
data=df["temp"].tolist()
datset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    datset.append(value)

mean=statistics.mean(datset)
std_deviation=statistics.stdev(datset)
print("mean",mean)
print("stddev",std_deviation)