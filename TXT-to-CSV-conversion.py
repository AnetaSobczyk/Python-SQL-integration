## Script to convert comma-seperated TXT files into CSV 
## packages OS and pandas must be installed
import os
import pandas as pd

## Directory where all files are placed
path_of_the_directory= "C:\\XXXXX"
for filename in os.listdir(path_of_the_directory):
    file = os.path.join(path_of_the_directory,filename)
## Name of CSV file will be first 3 characters of the original TXT file
    short_name = filename[0:3]
    if os.path.isfile(file):
        read_file = pd.read_csv (file)
        read_file.to_csv (path_of_the_directory+"\\"+short_name+".csv", index=None)