import pandas as pd
import matplotlib.pyplot as plt
import os

# Change the working directory to the folder containing the ozone data
os.chdir("C:\\Users\\User\\Desktop\\ozone_data")

# Load the data from the first Excel file (replace 'brewer24.xlsx' with your actual file name)
data1 = pd.read_excel("brewer24.xlsx")
df1 = pd.DataFrame(data1)
df1['Day'] = pd.to_datetime(df1['Day'])
df1.set_index('Day', inplace=True)
# Resample and compute weekly averages, ignoring missing values
weekly_avg1 = df1.resample('W-WED').mean()
weekly_df1 = pd.DataFrame({
    'Date': weekly_avg1.index,
    'Brewer Weekly_Average_DS': weekly_avg1['DS'],
    'Brewer Weekly_Average_ZC': weekly_avg1['ZC']
})

# Load the data from the second Excel file (replace 'dobson24.xlsx' with your actual file name)
data2 = pd.read_excel("dobson24.xlsx")
df2 = pd.DataFrame(data2)
df2['Day'] = pd.to_datetime(df2['Day'])
df2.set_index('Day', inplace=True)
# Resample and compute weekly averages, ignoring missing values
weekly_avg2 = df2.resample('W-WED').mean()
weekly_df2 = pd.DataFrame({
    'Date': weekly_avg2.index,
    'Dobson Weekly_Average_DS': weekly_avg2['DS'],
    'Dobson Weekly_Average_ZC': weekly_avg2['ZC']
})

# Print the resulting DataFrames
print("Brewer weekly averages:\n", weekly_df1)
print("Dobson weekly averages:\n", weekly_df2)

# Plotting the line graphs
plt.figure(figsize=(12, 6))

# Plot DS from the first dataset
plt.plot(weekly_df1['Date'], weekly_df1['Brewer Weekly_Average_DS'], label='Weekly Average DS (Brewer)', color='r', marker='o')
# Plot ZC from the first dataset
plt.plot(weekly_df1['Date'], weekly_df1['Brewer Weekly_Average_ZC'], label='Weekly Average ZC (Brewer)', color='b', marker='o')

# Plot DS from the second dataset
plt.plot(weekly_df2['Date'], weekly_df2['Dobson Weekly_Average_DS'], label='Weekly Average DS (Dobson)', color='r', marker='x', linestyle='--')
# Plot ZC from the second dataset
plt.plot(weekly_df2['Date'], weekly_df2['Dobson Weekly_Average_ZC'], label='Weekly Average ZC (Dobson)', color='b', marker='x', linestyle='--')

# Set the title and labels
plt.title('Weekly Average of DS and ZC from Brewer and Dobson Instruments')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()
