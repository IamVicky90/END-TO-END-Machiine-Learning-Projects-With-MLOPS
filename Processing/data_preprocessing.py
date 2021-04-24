from application_loging import app_logger
import pandas as pd
import os
import shutil
from sklearn.impute import KNNImputer
import numpy as np
class preocess_data:
    def __init__(self,file_path,exception_file_path):
        self.log=app_logger.logger()
        self.file=open(file_path,'a+')
        self.exception_file=open(exception_file_path,'a+')
    def remove_column(self,df,column):
        try:
            df=df.drop(column,axis=1)
            self.log.log(self.file,f'\t{column} removed sucessfully')
            
            return df
        except Exception as e:
            self.log.log(self.file,f"\tCouldn't remove {column} due to error: "+str(e))
            self.log.log(self.exception_file,f"\tCouldn't remove {column} due to error: "+str(e))
    def seprate_labels_and_features(self,df):
        try:
            features=df.drop(['Output'],axis=1)
            labels=df['Output']
            self.log.log(self.file,f"\tSucessfully seprate labels and features")
            return features,labels
        except Exception as e:
            self.log.log(self.file,f"\tCouldn't seprate labels and features due to error: "+str(e))
            self.log.log(self.exception_file,f"\tseprate labels and features due to error: "+str(e))
    def isnull(self,df):
        try:
            null_values_sum=df.isnull().sum()
            null_present=False
            d={'columns':'null_values'}
            for col,i in zip(df.columns,null_values_sum):
                if i>0:    
                    d[col]=i
                    null_present=True
                    self.log.log(self.file,f"\t{i} Null values present in column {col}")
            if not null_present:
                self.log.log(self.file,f"\tNo null values present in any column")
            try:
                null_df=pd.DataFrame.from_dict(d,orient='index',columns=None)
                null_csv='Null_csv'
                if os.path.isdir(null_csv):
                    shutil.rmtree(null_csv)
                os.mkdir(null_csv)
                null_df.to_csv(null_csv+'/'+'null_data_info.csv',header=False)
            except:
                self.log.log(self.file,f"\tCouldn't create the null_data_info.csv error: "+str(e))
            return null_present
        except Exception as e:
            self.log.log(self.file,f"\terror occured in isnull method: "+str(e))
            self.log.log(self.exception_file,f"\terror occured in isnull method: "+str(e))
    def knn_nan_values_imputer(self,data):
        try:
            imputer = KNNImputer(n_neighbors=3)
            array_data=imputer.fit_transform(data)
            self.log.log(self.file,'\tSuccessfully fill the nan values with the help of knn imputer')
            return pd.DataFrame(array_data,columns=data.columns)
        except Exception as e:
            self.log.log(self.file,"\tCouldn't fill the nan values with the help of knn imputer due to error: "+str(e))
            self.log.log(self.exception_file,"\tCouldn't fill the nan values with the help of knn imputer due to error: "+str(e))
    def drop_column_with_std_zero(self,data):
        try:
            zero_std_col=[]
            for col in data.columns:
                if data[col].describe()['std']==0:
                    zero_std_col.append(col)
                    self.log.log(self.file,f'\tWarning: {col} has zero standared deviation')
            self.log.log(self.file,f'\t{col} columns removed sucessfully as they has zero standared deviation')
            return self.remove_column(data,zero_std_col)
        except Exception as e:
            self.log.log(self.file,f"\tCouldn't complete the process of drop_column_with_std_zero due to error: "+str(e))
            self.log.log(self.exception_file,f"\tCouldn't complete the process of drop_column_with_std_zero due to error: "+str(e))


    def __str__(self):
        self.file.close()
        self.exception_file.close()





    