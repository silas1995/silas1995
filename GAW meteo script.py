# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:14:22 2023

@author: USER
"""
import glob
import os
import pandas as pd
os.chdir("C:\\Users\\USER\\Documents\\gaw mt kenya\\meteo")
#merge all text files into one dataframe
#define path to text files
path=r"C:\\Users\\USER\\Documents\\gaw mt kenya\\meteo"
path
#identify all text files                         
all_files=glob.glob(os.path.join("*.*"))
all_files

#merge all dat files into one dataframe
df=pd.concat((pd.read_table(f,skiprows=3,delim_whitespace=True) for f in all_files),ignore_index=True)

#export file to csv
df.to_csv("df.csv")
