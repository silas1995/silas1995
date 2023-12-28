# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:55:34 2023

@author: USER
"""
import pandas as pd
import os
os.chdir("C:\\Users\\USER\\Documents")
data=pd.read_csv("County gridded tmax.csv",skiprows=[1,2])
df=data

cumulative_counts_df = pd.DataFrame()
for column in df.columns:
    # Skip non-numeric columns
    if column=='ID':
        continue
    
    # Initialize count for each column
    count = 0
    
    # Create a new column in the cumulative_counts_df
    for index, value in df[column].iteritems():
        if value > 30:
            count += 1
        else:
            count = 0
        cumulative_counts_df.loc[index, f'{column}'] = count

# Display the result
print(cumulative_counts_df)

cumulative_counts_df.to_excel("consecutive tmaxindices.xlsx")

###########################################################
#############################################
import pandas as pd
import os
import sys

os.chdir("C:\\Users\\USER\\Documents")

# Read the CSV file
data = pd.read_csv("County gridded tmax.csv", skiprows=[1, 2])

cumulative_counts_df = pd.DataFrame()

# Iterate through columns
for column in data.columns:
    # Skip non-numeric columns
    if column == 'ID':
        continue

    # Count consecutive occurrences using apply and lambda function
    cumulative_counts_df[column] = data[column].apply(lambda x: 0 if x <= 30 else 1).groupby(
        data[column].gt(30).ne(data[column].gt(30).shift()).cumsum()).cumsum()

# Display the result
print(cumulative_counts_df)

# Save to Excel
cumulative_counts_df.to_csv("consecutive_tmax_indices.csv", index=False)




