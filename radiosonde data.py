# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 07:36:13 2024

@author: USER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir("C:\\Users\\USER\\Documents\\intro3")
# Load radiosonde data
data = pd.read_csv('radiosonde_data.csv')

# Data preprocessing
# Assuming 'Temperature', 'Pressure', 'Humidity' columns are present
# Handle missing values, outliers, etc.

# Calculate Dew Point Temperature
def dew_point_temperature(temperature, humidity):
    A = 17.27
    B = 237.7
    alpha = ((A * temperature) / (B + temperature)) + np.log(humidity / 100.0)
    dew_point = (B * alpha) / (A - alpha)
    return dew_point

data['Dew_Point_Temperature'] = dew_point_temperature(data['Temperature'], data['Humidity'])

# Data exploration and visualization
plt.figure(figsize=(12, 8))

# Time series plot
plt.subplot(2, 2, 1)
plt.plot(data['Time'], data['Temperature'], color='r', label='Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()

# Pressure vs. Altitude
plt.subplot(2, 2, 2)
plt.plot(data['Altitude'], data['Pressure'], color='b', label='Pressure')
plt.xlabel('Altitude (m)')
plt.ylabel('Pressure (hPa)')
plt.legend()

# Histogram of Humidity
plt.subplot(2, 2, 3)
plt.hist(data['Humidity'], bins=20, color='g', alpha=0.7)
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')

# Scatter plot of Temperature vs. Dew Point Temperature
plt.subplot(2, 2, 4)
plt.scatter(data['Temperature'], data['Dew_Point_Temperature'], color='m', marker='.')
plt.xlabel('Temperature (°C)')
plt.ylabel('Dew Point Temperature (°C)')

plt.tight_layout()
plt.show()