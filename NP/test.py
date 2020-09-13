import pandas as pd
import plotly as py
import plotly.graph_objs as go

iris = pd.read_csv(r"./NP/iris.csv")
iris = iris.rename(columns={iris.columns[0]:"Index"})

x1 = go.Scatter(x=iris["Petal.Width"], y=iris["Petal.Length"], mode="markers", name="Petal")
x2 = go.Scatter(x=iris["Sepal.Width"], y=iris["Sepal.Length"], mode="markers", name="Sepal")
layout=go.Layout(title="Iris", xaxis=dict(title="Width"), yaxis=dict(title="Length"), legend=dict(x=1, y=.5, font=dict(color="black", size=18)))
data = [x1, x2]
fig = go.Figure(data=data, layout=layout)
py.offline.iplot(fig, filename="aaa.html")

x3 = go.Bar(x=iris.index, y=iris["Petal.Width"], name="Petal.Width", opacity=.9, marker=dict(color=["red", "blue", "green"]*50))
layout2=go.Layout(title="Iris", xaxis=dict(title="index"), yaxis=dict(title="Petal.Width"), legend=dict(x=1, y=.5, font=dict(color="black", size=18)))
fig2 = go.Figure(data=[x3], layout=layout2)
py.offline.iplot(fig2, filename="bbb.html")