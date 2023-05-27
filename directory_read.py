import os
import pandas as pd
pathName = r'/home/sitanshu/Documents/Python/datasets'



def directory_read(pathName):
    df = pd.DataFrame()
    for i in os.scandir(pathName):
        if os.path.isfile(i):
            if i.endswith('.csv'):
                df1 = pd.read_csv(i)
                df = pd.concat([df, df1], axis =1)
            elif i.endswith('.xlsx'):
                df1 = pd.read_excel(i)
                df=pd.concat([df, df1], axis = 1)
        elif os.path.isdir(i):
            directory_read(i)

# Splitting the file into multiple files
csvfile = open('/home/sitanshu/Documents/Python/datasets/tempreture/city_temperature.csv', 'r').readlines()
path = '/home/sitanshu/Documents/Python/datasets/tempreture/'
filename = 1
for i in range(len(csvfile)):
    if i % 10000 == 0:
        open(path+ str(filename) + '.csv', 'w+').writelines(csvfile[i:i+10000])
        filename += 1
