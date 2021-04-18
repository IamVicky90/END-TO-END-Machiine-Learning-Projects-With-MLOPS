import os
import pandas as pd
path='Training_Batch_Files'
files=os.listdir('Training_Batch_Files')
for f in files:
    csv=pd.read_csv('Training_Batch_Files/'+f)
    print("read csv",pd.read_csv(path+'/'+f).shape[1])
    # print("Number of columns",NumberofColumns)
    if 592==pd.read_csv(path+'/'+f).shape[1]:
        print("file name",f)
