# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:55:01 2024

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:14:51 2024

@author: USER
"""

import matplotlib.pyplot as plt
import pandas as pd

# Function to extract data within a pressure range
def extract_data_within_pressure_range(data, pressure_range):
    min_pressure, max_pressure = pressure_range
    data['Press'] = pd.to_numeric(data['Press'], errors='coerce')  # Convert 'Press' column to numeric type
    extracted_data = data[(data['Press'] >= min_pressure) & (data['Press'] <= max_pressure)]
    return extracted_data

import os
os.chdir("C:\\Users\\USER\\Desktop\\dats")

# Load data for each launch (assuming CSV files)
launch_files = ["launch1.csv", "launch2.csv"]

# Pressure ranges of interest
pressure_ranges = [(820, 821), (800, 801), (700, 701), (600, 601), (500, 501), (400, 401), (300, 301)]

# Lists to store x and y values for each launch
launch1_O3_mPa = []
launch1_pressures = []
launch2_O3_mPa = []
launch2_pressures = []

# Plotting
plt.figure(figsize=(10, 6))

for launch_file in launch_files:
    # Read data for the launch
    launch_data = pd.read_csv(launch_file)
    
    # Plot temperature vs. pressure within each pressure range
    for pressure_range in pressure_ranges:
        data_within_range = extract_data_within_pressure_range(launch_data, pressure_range)
        avg_temp = data_within_range['O3_mPa'].mean()
        
        # Store data for each launch
        if launch_file == "launch1.csv":
            launch1_O3_mPa.append(avg_temp)
            launch1_pressures.append(sum(pressure_range)/2)
        elif launch_file == "launch2.csv":
            launch2_O3_mPa.append(avg_temp)
            launch2_pressures.append(sum(pressure_range)/2)

# Plot lines connecting all data points for each launch
plt.plot(launch1_O3_mPa , launch1_pressures, label='Launch 1', marker='o')
plt.plot(launch2_O3_mPa , launch2_pressures, label='Launch 2', marker='o')

plt.xlabel('Average O3_mPa')
plt.ylabel('Average Pressure (hPa)')
plt.title('Average Pressure vs Average O3_mPa within Pressure Ranges')
plt.legend()
plt.gca().invert_yaxis()  # Invert y-axis to represent higher pressure at bottom
plt.grid(True)
plt.tight_layout()
plt.show()
