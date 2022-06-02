## script to import CSV files from a given directory to an existing table in the database

## following packages must be installed and imported
import os
import mysql.connector as msql
import pandas as pd

## connecting to the existing database with the username and password
mydb = msql.connect(
    host = "localhost",
    user = "root",
    password = "XXXX",
    database="NameOfDB"
)
cursor = mydb.cursor()

## directory with all CSV files to be imported
path_of_the_directory= "C:\\XXXX"
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)

## command print(f) might be useful to se progress of the script
## particularly when amount of CSV files is big and the script runs for a longer time
    
    if os.path.isfile(f):
        df = pd.read_csv (f)
        for i,row in df.iterrows():

## VALUES must be formatted properly to reflect existing columns in the table

            sql = "INSERT INTO DBName.TableName VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            mydb.commit()