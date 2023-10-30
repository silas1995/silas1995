# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 08:54:44 2023

@author: USER
"""

import zipfile, os
working_directory=os.chdir("C:\\Users\\USER\\Documents\\gaw mt kenya\\tei49i")
for file in os.listdir(working_directory):   # get the list of files
    if zipfile.is_zipfile(file): # if it is a zipfile, extract it
        with zipfile.ZipFile(file) as item: # treat the file as a zip
           item.extractall()  # extract it in the working directory
          
            
import glob
import os
import pandas as pd

os.chdir("C:\\Users\\USER\\Documents\\gaw mt kenya\\tei49i")
os.getcwd()
#define path to dat files
path=r"C:\\Users\\USER\\Documents\\gaw mt kenya\\tei49i"

#identify all text files                         
all_files=glob.glob(os.path.join("*.dat"))
all_files
#merge all dat files into one dataframe
df=pd.concat((pd.read_table(f,delim_whitespace=True) for f in all_files),ignore_index=True)
df
df.to_csv(r"C:\Users\USER\Documents\gaw mt kenya\tei49i\mt_Kenya_tei491.csv", index=False)
#select specific columns of interest from the dataframe
mt_kenya_tei49i_spec=df[["pcdate","pctime","time","date","o3"]]
mt_kenya_tei49i_spec.to_csv(r"C:\Users\USER\Documents\gaw mt kenya\tei49i\mt_Kenya_spec.csv", index=False)
print(mt_kenya_tei49i_spec)

import os
import shutil
 
source ="C:\Users\USER\Documents\gaw mt kenya\tei49i"
destination = "C:\\Users\\USER\\Desktop\\archive"
 
# gather all files and move to the archive folder
directory_files = os.listdir(source)
for f in directory_files: # grabs all files
    src_path=os.path.join(source,f)
    dst_path=os.path.join(destination,f)
    shutil.move(src_path,dst_path)
