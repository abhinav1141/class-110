import plotly.figure_factory as ff
import statistics
import pandas as pd
import random
import csv
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
data=df["temp"].tolist()
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean 
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    std_deviation=statistics.stdev(mean_list)
    print("mean of sampling distribution",mean) 
    print("stddeviation of sampling distribution", std_deviation)
setup()           

