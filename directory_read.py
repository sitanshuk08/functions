# Importing required libraries for the function
# os lib helps interaction with the directories
import os
# pandas help interaction with the dataframe
import pandas as pd

# creating the function to read into the directory
# import pandas and os library as a prerequisite


# function takes in 2 values, path and dataframe
def directory_read(pathName, df):
    # ignore the commented out lines, inserted for testing purpose
    # count_file = 0
    # count_subdirectory = 0
    
    # for loop which scans all the directories
    for i in os.scandir(pathName):
        # print(i)
        # if the path ends in a file reads the csv or excel file else continue
        if os.path.isfile(i):
            # count_file = count_file +1
            # print(count_file)
            if i.path.endswith('.csv'):
                df1 = pd.read_csv(i)
                df = pd.concat([df, df1], axis =1)
            elif i.endswith('.xlsx'):
                df1 = pd.read_excel(i)
                df=pd.concat([df, df1], axis = 1)
            else: 
                continue
        # if the director is subdirectory, calls the function to read the directory and appends to the existing dataframe
        elif os.path.isdir(i):
            # count_subdirectory = count_subdirectory+1
            # print(count_subdirectory)
            directory_read(i, df)
    # print(count_file)

# defining blank dataframe in which we will append the files being read
df = pd.DataFrame()
# defining the path variable
path_test = r'/home/sitanshu/Documents/Python/datasets/tempreture'
directory_read(path_test, df)


