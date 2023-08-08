# Importing required libraries for the function
# os lib helps interaction with the directories
import os
# pandas help interaction with the dataframe
import pandas as pd
# creating the function to read into the directory
# import pandas and os library as a prerequisite


# function takes in 2 values, path and dataframe
def directory_read(pathName, df):
    # declare the variable global so they can be used outside function
    global df_1
    
    # for loop which scans all the directories
    for i in os.scandir(pathName):
        # if the path ends in a file reads the csv or excel file else continue
        if os.path.isfile(i):
            
            if i.path.endswith('.csv'):
                df1 = pd.read_csv(i,low_memory = False)
                
            elif i.endswith('.xlsx'):
                df1 = pd.read_excel(i)
                
            else: 
                continue
            df=pd.concat([df, df1], axis = 0)
            
        # if the director is subdirectory, calls the function to read the directory and appends to the existing dataframe
        elif os.path.isdir(i):
            # count_subdirectory = count_subdirectory+1
            # print(count_subdirectory)
            directory_read(i, df)
        
    # print(count_file)
    df_1 = df.copy() 
    return df_1

import os
import pandas as pd
import dask as dd


def directory_read_dask(pathName, df):
    # declare the variable global so they can be used outside function
    global df_1
    
    # for loop which scans all the directories
    for i in os.scandir(pathName):
        # if the path ends in a file reads the csv or excel file else continue
        if os.path.isfile(i):
            
            if i.path.endswith('.csv'):
                df1 = dd.read_csv(i,low_memory = False)
                
            elif i.path.endswith('.xlsx'):
                df1 = dd.read_excel(i)
                
            else: 
                continue
            df=dd.concat([df, df1], axis = 0)
            
        # if the director is subdirectory, calls the function to read the directory and appends to the existing dataframe
        elif os.path.isdir(i):
            # count_subdirectory = count_subdirectory+1
            # print(count_subdirectory)
            directory_read(i, df)
        
    # print(count_file)
    df_1 = df.copy() 
    return df_1


# defining blank dataframe in which we will append the files being read
df = pd.DataFrame()
empty_dask_df = dd.from_delayed([df], meta=df)
# empty_dask_df = dd.from_pandas(df, npartitions=1) 

# defining the path variable
# directory_read(path_test,df)
path_test = r'/home/sitanshu/Documents/Python/datasets/tempreture/Files1'

directory_read_dask(path_test,df)
df_1.head()

