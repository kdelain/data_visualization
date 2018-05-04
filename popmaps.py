# -*- coding: utf-8 -*-
"""
Plot some map data using the choropleth mode of plotly
"""

# Not needed for this
import numpy as np

# for reading in CSV data
import pandas as pd

# for plotting the data using plotly (see https://plot.ly for more information)
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True)

# Read in the Power Consumption CSV file
pwr_df = pd.read_csv('2014_World_Power_Consumption')

# You will need to know the data column names. If using Jupyter or another
# interactive IDE you can do pwr_df.head() to get the data headers prior
# to this coding this next step. Or just look at the CSV file.

# Set up the dictionary. Preferred method for choropleth is using dict()
# Check https://plot.ly/python/reference/#choropleth for locationmode and
# other parameters such as allowed colorscales
data = dict(type = 'choropleth',
            locations = pwr_df['Country'],       #Map locations defined in CSV file
            locationmode = "country names",  
            colorscale= 'Portland',
            text= pwr_df['Text'],                #Mouseover text
            z=pwr_df['Power Consumption KWH'],   #values to be plotted
            colorbar = {'title':'KWH'})      #Title of the color bar

# Set up the layout. https://plot.ly/python/reference/#choropleth for more info
layout = dict(
    title = '2014 World Power Consumption',  # Title of the whole plot
    geo = dict(
        showframe = False,
        projection = {'type':'Mercator'}     # See link for more options
    )
)
    
# Make the figure and plot it 
choromap = go.Figure(data = [data],layout = layout)
plot(choromap,validate=False)