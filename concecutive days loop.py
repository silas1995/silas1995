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

cumulative_counts_df.to_excel("consecutive indices dataframe1.xlsx")






######################################################################
##################################################################
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:35:59 2023

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:55:34 2023

@author: USER
"""
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
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
#print(cumulative_counts_df)

#cumulative_counts_df.to_excel("consecutive indices dataframe1.xlsx")

for column in df.columns:
    # Create a new figure for each column
    plt.figure()

    # Plot the data
    sns.lineplot(x=df.ID, y=column, data=df, label=column)
    
    # Fit a trend line (linear regression) and plot it
    sns.regplot(x=df.ID, y=column, data=df, scatter=False, ci=None, line_kws={'color': 'red'})

    # Set plot labels and title
    plt.xlabel('ID')
    plt.ylabel(column)
    plt.title(f'Line Graph for {column} with Trend Line')

    # Show the legend
    plt.legend()

# Display all the plots
plt.show()





