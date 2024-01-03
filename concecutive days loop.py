import pandas as pd
import os

# Set the working directory
os.chdir("C:\\Users\\USER\\Documents")

# Read the CSV file
data = pd.read_csv("County gridded tmax.csv", skiprows=[1, 2])
df = data.copy()

# Create a new DataFrame to store consecutive counts
cumulative_counts_df = pd.DataFrame()

# Loop through the columns of the DataFrame
for column in df.columns:
    # Skip non-numeric columns and 'ID'
    if column == 'ID' or not pd.api.types.is_numeric_dtype(df[column]):
        continue

    count = 0

    # Create a new column in the cumulative_counts_df
    for index, value in enumerate(df[column]):
        if value > 30:
            count += 1
        else:
            count = 0
        cumulative_counts_df.loc[index, f'{column}'] = count

# Display the result
print(cumulative_counts_df)

# Save the result to an Excel file
cumulative_counts_df.to_excel("consecutive_tmax_indices.xlsx")
