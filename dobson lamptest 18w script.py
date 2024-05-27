import pandas as pd
import matplotlib.pyplot as plt
import os

# Change the working directory to where the CSV file is located
os.chdir("C:\\Users\\USER\\Desktop")

# Read the data from the CSV file (assuming the file is named 'GAW.csv')
data = pd.read_csv('18w.csv')

# Parse the date column with the correct date format
# Assuming the date format in the CSV file is 'dd/mm/yyyy'
data['Dates'] = pd.to_datetime(data['Dates'], format='%d/%m/%Y')

# Set the date column as the index
data.set_index('Dates', inplace=True)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['A'], label='Setting A')
plt.plot(data.index, data['C'], label='Setting C')
plt.plot(data.index, data['D'], label='Setting D')

# Add horizontal lines at specific y-values
plt.axhline(y=61.2, color='r', linestyle='--', label='61.2')
plt.axhline(y=62.6, color='g', linestyle='--', label='62.6')
plt.axhline(y=63.4, color='b', linestyle='--', label='63.4')

# Add title and labels
plt.title('DOBSON STANDARD 18W LAMPTESTS')
plt.xlabel('Date')
plt.ylabel('Values')

# Add a legend
plt.legend()

# Show the plot
plt.show()
