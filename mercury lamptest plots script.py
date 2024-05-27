import pandas as pd
import matplotlib.pyplot as plt
import os

# Change the working directory to where the CSV file is located
os.chdir("C:\\Users\\USER\\Desktop")

# Read the data from the CSV file (assuming the file is named 'mercury.csv')
data = pd.read_csv('mercury.csv')

# Parse the date column with the correct date format
# Assuming the date format in the CSV file is 'dd/mm/yyyy'
data['Dates'] = pd.to_datetime(data['Dates'], format='%d/%m/%Y')

# Set the date column as the index
data.set_index('Dates', inplace=True)

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

# Plot the first line on the first subplot
ax1.plot(data.index, data['TEST MEAN Qm'], label='TEST MEAN Qm', color='b')
ax1.set_ylabel('TEST MEAN Qm', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.legend(loc='best')
ax1.set_title('Mercury lamptest plots')

# Plot the second line on the second subplot
ax2.plot(data.index, data['TABLE Q1 at Tm'], label='TABLE Q1 at Tm', color='g')
ax2.set_ylabel('TABLE Q1 at Tm', color='g')
ax2.tick_params(axis='y', labelcolor='g')
ax2.legend(loc='best')

# Plot the third line on the third subplot
ax3.plot(data.index, data['DIFFERENCE'], label='DIFFERENCE', color='r')
ax3.set_xlabel('Date')
ax3.set_ylabel('DIFFERENCE', color='r')
ax3.tick_params(axis='y', labelcolor='r')
ax3.legend(loc='best')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
