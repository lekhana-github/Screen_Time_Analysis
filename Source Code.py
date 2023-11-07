import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

# Read the data from the CSV file
# Updated CSV file
data = pd.read_csv('Screentime-App-Details.csv')
print("--------------------------------------- DATA SHEET ----------------------------------------------\n")
print(data)

# Check for null values
null_values = data.isnull().sum()
print("--------------------------------------- NULL VALUES ------------------------------------------------")
print(null_values)

# Replace the nulls with 0
data.fillna(0, inplace = True)
print("---------------------------- DATA SHEET AFTER REPLACING NULL VALUES WITH 0 --------------------------\n")
print(data)
print()

# Display descriptive statistics of the data
descriptive_stats = data.describe()
print("\n---------------------- DESCRIPTIVE STATISTICS OF THE DATA -----------------------")
print(descriptive_stats)
print()

# Analyze the destructive app usage level and display it as a bar chart
print("------- THE BELOW GRAPH SHOWS HOW EXCESSIVE SCREEN TIME ON SOCIAL MEDIA AND VIDEO GAMES CAN BE DESTRUCTIVE ----------------\n")
usage_bar_chart = px.bar(data_frame=data.query('Usage > 90 and App in ["Whatsapp", "Instagram", "PubG"]'),
                         x='Date', y='Usage', title='DESTRUCTIVE APP USAGE LEVEL', color='App')
usage_bar_chart.show()

# Analyze the productive app usage level and display it as a bar chart
print("\n------------ THE BELOW GRAPH SHOWS HOW UTILIZING THE SCREEN TIME ON EDUCATIONAL AND WORK PURPOSE IS PRODUCTIVE ------\n")
notifications_bar_chart = px.bar(data.query('Usage > 50 and App in ["Udemy", "MSExcel"]'),
                                 x='Date', y='Usage', title='PRODUCTIVE APP USAGE LEVEL', color='App')
notifications_bar_chart.show()

# Analyze the amount of usage of the apps and display it as a bar chart
usage_bar_chart = px.bar(data_frame=data, x='Date', y='Usage', title='APP USAGE TIME', color='App')
usage_bar_chart.show()

# Analyze the number of notifications from the apps and display it as a bar chart
notifications_bar_chart = px.bar(data, x='Date', y='Notifications',
                                title='NUMBER OF NOTIFICATIONS FROM THE APP', color='App')
notifications_bar_chart.show()

# Analyze the number of times the apps opened and display it as a bar chart
opened_bar_chart = px.bar(data, x='Date', y='Times opened',
                          title='NUMBER OF TIMES APPS OPENED', color='App')
opened_bar_chart.show()

# Analyze the relationship between the number of notifications and the amount of usage and display it as a scatter chart
scatter_chart = px.scatter(data_frame=data, x='Notifications', y='Usage', trendline='ols',
                           title='RELATIONSHIP BETWEEN THE NUMBER OF NOTIFICATIONS AND THE AMOUNT OF APP USAGE')
scatter_chart.show()
