import pandas as pd
import matplotlib.pyplot as plt
import os

# Change the working directory to where the CSV file is located
os.chdir("C:\\Users\\USER\\Desktop")

# Read the data from the CSV file (assuming the file is named 'GAW.csv')
data = pd.read_csv('18v.csv')

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
plt.axhline(y=61.5, color='r', linestyle='--', label='61.5')
plt.axhline(y=62.8, color='g', linestyle='--', label='62.8')
plt.axhline(y=63.6, color='b', linestyle='--', label='63.6')

# Add title and labels
plt.title('DOBSON STANDARD 18V LAMPTESTS')
plt.xlabel('Date')
plt.ylabel('Values')


# Add a legend
plt.legend()

# Show the plot
plt.show()
