import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
t=np.linspace(0,2*np.pi,50)
z=np.sin(t)
data = [go.Scatter(
    x = t,
    y = z,
)]

layout = go.Layout(
        xaxis=dict(
            title='Eje X',),
        yaxis=dict(
            title='Eje Y',)
    )
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig,filename='grafica.html',config={'displayModeBar': False})