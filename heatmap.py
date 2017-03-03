# -*- coding: cp1252 -*-
import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import codecs
from plotly import tools
import plotly.figure_factory as FF



# -*- coding: utf-8 -*-

#look for data file

degree_sign= u'\N{DEGREE SIGN}'
timelist = list()
avglist = list()
stdlist = list()
meansum=0
avgentry=0
traces = []
annots = []
z_text = []
annotations = []


with open("C:\\PythonPrograms\\ambient.txt") as f:
    data = f.read()
    data = data.splitlines()
    for i in range (0,len(data)):
        #data[i]=data[i].split("\t") use for old data
        data[i]=data[i].split(",")
        timelist.append(data[i][0])
        for j in range (0,len(data[i])):
            meansum = meansum + float(data[i][j])
            avgentry = meansum/len(data[i])
        avglist.append(avgentry)  
    f.close()


x = ['A', 'B', 'C', 'D']
y = ['Z', 'Y', 'X', 'W']


for l in range(0,len(data)):

    datalist = [data[l][i-4:i] for i in range(len(data[l]), 0, -4)]
    for n, row in enumerate(datalist):
        for m, val in enumerate(row):
            var = datalist[n][m]
            annotations.append(
                dict(
                    text=str(val),
                    x=x[m], y=y[n],
                    xref='x1', yref='y1',
                    font=dict(color='black'), #change font colour if its different
                    showarrow=False)
            )
    colorscale = [[0, '#ffff00'],[0.25, '#ffa250'],[0.5, '#ffa500'], [0.75, '#ffa750'],[1, '#ff0000']]  # custom colorscale
    trace = go.Heatmap(x=x, y=y, z=datalist, colorscale=colorscale,showscale=False)
    traces.append(trace)
    annots.append(annotations)
    l = l+1


## Plot an individual heatmap of one row in a full map
##fig = go.Figure(data=[trace])
##fig['layout'].update(
##    title="the sKan Heatmap",
##    annotations=annotations,
##    xaxis=dict(ticks='', side='top'),
##    # ticksuffix is a workaround to add a bit of padding
##    yaxis=dict(ticks='', ticksuffix='  '),
##    width=800,
##    height=800,
##    autosize=False)

#py.plot(fig, filename='the sKan Heatmap', height=750)


trace1 = traces[0]
trace2 = traces[1]
trace3 = traces[2]
trace4 = traces[3]
trace5 = traces[4]
trace6 = traces[5]
trace7 = traces[6]
trace8 = traces[7]
trace9 = traces[8]
trace10 = traces[9]
trace11 = traces[10]
trace12 = traces[11]
trace13 = traces[12]
trace14 = traces[13]
trace15 = traces[14]
trace16 = traces[15]

fig = tools.make_subplots(rows=1, cols=16, subplot_titles=('Time:'+ str(data[0][0])+' secs', 'Time:'+ str(data[1][0])+' secs',
                                                          'Time:'+ str(data[2][0])+' secs', 'Time:'+ str(data[3][0])+' secs',
                                                          'Time:'+ str(data[4][0])+' secs', 'Time:'+ str(data[5][0])+' secs',
                                                          'Time:'+ str(data[6][0])+' secs', 'Time:'+ str(data[7][0])+' secs',
                                                          'Time:'+ str(data[8][0])+' secs', 'Time:'+ str(data[9][0])+' secs',
                                                          'Time:'+ str(data[10][0])+' secs', 'Time:'+ str(data[11][0])+' secs',
                                                          'Time:'+ str(data[12][0])+' secs', 'Time:'+ str(data[13][0])+' secs',
                                                           'Time:'+ str(data[14][0])+' secs', 'Time:'+ str(data[15][0])+' secs'))
fig.append_trace(trace1, 1, 1,)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)
fig.append_trace(trace4, 1, 4)
fig.append_trace(trace5, 1, 5)
fig.append_trace(trace6, 1, 6)
fig.append_trace(trace7, 1, 7)
fig.append_trace(trace8, 1, 8)
fig.append_trace(trace9, 1, 9)
fig.append_trace(trace10, 1, 10)
fig.append_trace(trace11, 1, 11)
fig.append_trace(trace12, 1, 12)
fig.append_trace(trace13, 1, 13)
fig.append_trace(trace14, 1, 14)
fig.append_trace(trace15, 1, 15)
fig.append_trace(trace16, 1, 16)


fig['layout'].update(height=500, width=3200, title='Multiple Subplots')

plot_url = py.plot(fig, filename='make-subplots-multiple-with-title')

#https://plot.ly/python/annotated_heatmap/#new-to-plotly
##If we have seperate figures then ensure each one has a title and its own correct annotations
##If we do one mega heatmap display, make sure you can see the time and position of each colour
##


### Find your api_key here: https://plot.ly/settings/api


#ADD LEGEND

#Issue with below code is it attempts to make a 16x16 grid made of ones not of 4x4s
##z = data[:16]
###z_text = np.around(z, decimals=2) # Only show rounded value (full value on hover)
##zdata = data[:16]
##fig = FF.create_annotated_heatmap(z, annotation_text=str(zdata), colorscale=[[0, '#ffff00'],[0.5, '#ffa500'], [1, '#ff0000']], hoverinfo='z')
##
### Make text size smaller
##for i in range(len(fig.layout.annotations)):
##    fig.layout.annotations[i].font.size = 8
##    
##py.plot(fig, filename='annotated_heatmap_numpy')
##
