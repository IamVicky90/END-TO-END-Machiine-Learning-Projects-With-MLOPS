from application_loging import app_logger
import json,sys,os
import re
import shutil
import pandas as pd
class PredictionRawDataValidation:
    def __init__(self,path):
        self.directory_path=path
        self.log=app_logger.logger()
        self.schema_path='pred_schema.json'
    def ValuesfromSchema(self):
        """this will return the values according to the schema.json file"""
        try:
            with open(self.schema_path,'r') as f:
                dic=json.load(f)
                f.close()
            LengthOfDateStampInFile=dic['LengthOfDateStampInFile']
            LengthOfTimeStampInFile=dic['LengthOfTimeStampInFile']
            NumberofColumns=dic['NumberofColumns']
            ColName=dic['ColName']
            file=open('PredictionLogs/valuesFromSchemaLogs.txt','a+')
            message=f"\tSucessfully send values from schema.json file values are LengthOfDateStampInFile:{LengthOfDateStampInFile}\t\t  LengthOfTimeStampInFile:{LengthOfTimeStampInFile}\t\t NumberofColumns:{NumberofColumns}\n"
            self.log.log(file,message)
            file.close()
        except ValueError:
            file=open('PredictionLogs/valuesFromSchemaLogs.txt','a+')
            message=f"\tValue not found inside {self.schema_path}"
            self.log.log(file,message)
            file.close()
            raise ValueError

        except KeyError:
            file=open('PredictionLogs/valuesFromSchemaLogs.txt','a+')
            message=f"\tKey not found inside {self.schema_path}"
            self.log.log(file,message)
            file.close()
            raise KeyError

        except Exception as e:
            file=open('PredictionLogs/valuesFromSchemaLogs.txt','a+')
            message=f"\tError while taking ValuesFromSchema function: {str(e)}"
            self.log.log(file,message)
            file.close()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            raise e

        
        return ColName, LengthOfDateStampInFile, LengthOfTimeStampInFile, NumberofColumns
    def regex(self):
        """ This will return the manual regex expression that the file name shoud support"""
        return "Prediction_Batch_files_wafer+['_']+[\d]+['_']+[\d]+.csv"
        # "['wafer']+['\_'']+[\d_]+[\d]+\.csv"
    def PredictiondeleteGoodRawDataFolder(self):
        """For deleting the Good Raw Data Folder if Present, because every time we began with the new Good Data folder"""
        GoodDataPath='PredictionGoodRawDataFolder'
        try:
            if os.path.isdir(GoodDataPath):
                shutil.rmtree(GoodDataPath)
                file=open('PredictionLogs/PredictiondeleteGoodRawDataFolder.txt','a+')
                message=f"Good folder Deleted Successfully"
                self.log.log(file,message)
                file.close()
            else:
                file=open('PredictionLogs/PredictiondeleteGoodRawDataFolder.txt','a+')
                message=f"\tThere is no Good Data Folder"
                self.log.log(file,message)
                file.close()
        except Exception as e:
            file=open('PredictionLogs/Exception.txt','a+')
            message=f"\tcould not delete the Good directory error is, {str(e)}"
            self.log.log(file,message)
            file.close()
    def PredictiondeleteBadRawDataFolder(self):
        """For deleting the Bad Raw Data Folder if Present, because every time we began with the new Good Data folder"""
        BadDataPath='PredictionBadRawDataFolder'
        try:
            if os.path.isdir(BadDataPath):
                shutil.rmtree(BadDataPath)
                file=open('PredictionLogs/PredictiondeleteBadRawDataFolder.txt','a+')
                message=f"\tBad folder Deleted Successfully"
                self.log.log(file,message)
                file.close()
            else:
                file=open('PredictionLogs/PredictionBadRawDataFolder.txt','a+')
                message=f"\tThere is no Bad Data Folder"
                self.log.log(file,message)
                file.close()
        except Exception as e:
            file=open('PredictionLogs/Exception.txt','a+')
            message=f"\tcould not delete the Bad directory error is, {str(e)}"
            self.log.log(file,message)
            file.close()
    def PredictioncreateGoodRawDataFolder(self):
        '''This will create the Good Raw Data Folder'''
        try:
            # GoodDataPath='wafer_fault_detection'
            os.system('mkdir PredictionGoodRawDataFolder')
            file=open('PredictionLogs/PredictionGoodRawDataFolder.txt','a+')
            message=f"\tSucccessfully created the PredictionGoodRawDataFolder directory"
            self.log.log(file,message)
            file.close()
        except Exception as e:
            file=open('PredictionLogs/Exception.txt','a+')
            message=f"\tcould not create the PredictionGoodRawDataFolder directory error is, {str(e)}"
            self.log.log(file,message)
            file.close()
    def PredictioncreateBadRawDataFolder(self):
        '''This will create the Bad Raw Data Folder'''
        try:
            # GoodDataPath='wafer_fault_detection'
            os.system('mkdir PredictionBadRawDataFolder')
            file=open('PredictionLogs/PredictionBadRawDataFolder.txt','a+')
            message=f"\tSucccessfully created the PredictionBadRawDataFolder directory"
            self.log.log(file,message)
            file.close()
        except Exception as e:
            file=open('PredictionLogs/Exception.txt','a+')
            message=f"\tcould not create the PredictionBadRawDataFolder directory error is, {str(e)}"
            self.log.log(file,message)
            file.close()



    def validateRawDataByRegexExpression(self,regex,LengthOfDateStampInFile,LengthOfTimeStampInFile):
        self.PredictiondeleteGoodRawDataFolder()
        self.PredictiondeleteBadRawDataFolder()
        self.PredictioncreateGoodRawDataFolder()
        self.PredictioncreateBadRawDataFolder()
        files=os.listdir(self.directory_path)
        for f in files:
            if re.match(regex,f):
                file_name,_=f.split('.')
                filedatestamp,timestamptime=file_name.split('_')[4:]
                

                if len(filedatestamp)==LengthOfDateStampInFile:
                    if len(timestamptime)==LengthOfTimeStampInFile:

                        shutil.copy(f'Prediction_Batch_Files/{f}','PredictionGoodRawDataFolder')
                        file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
                        message=f"\tSucccessfully Validate the File name: {f} and copy it to ,PredictionGoodRawDataFolder"
                        self.log.log(file,message)
                        file.close()
                    else:
                        shutil.copy(f'Prediction_Batch_Files/{f}','PredictionBadRawDataFolder')
                        file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
                        message=f"\tFile name is not according to Schema.json, filename: {f}"
                        self.log.log(file,message)
                        file.close()
                else:
                    shutil.copy(f'Prediction_Batch_Files/{f}','PredictionBadRawDataFolder')
                    file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
                    message=f"\tFile name is not according to Schema.json, filename: {f}"
                    self.log.log(file,message)
                    file.close()
            else:
                shutil.copy(f'Prediction_Batch_Files/{f}','PredictionBadRawDataFolder')
                file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
                message=f"\tFile name is not according to Schema.json, filename: {f}"
                self.log.log(file,message)
                file.close()
    def validateDataByNumberOfColumns(self,NumberofColumns):
        ''''This will check the number of column according to our schema file'''
        path='PredictionGoodRawDataFolder'
        files=os.listdir(path)
        for f in files:
            
            if NumberofColumns==pd.read_csv(path+'/'+f).shape[1]:
                file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
                message=f"\tfile {f} columns is matching with our Schema"
                self.log.log(file,message)
                file.close()
            else:
                try:
                    shutil.move(path+'/'+f,'PredictionBadRawDataFolder')
                    file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
                    message=f"\tMove the file: {f} to PredictionBadRawDataFolder because columns was not matching with our Schema"
                    self.log.log(file,message)
                    file.close()
                except Exception as e:
                    file=open('PredictionLogs/Exception.txt','a+')
                    message=f"\tCouldn't move the file: {f} to PredictionBadRawDataFolder in which columns was not matching with our Schema due to error: {str(e)}"
                    self.log.log(file,message)
                    file.close()
    def validateColumnsbymissingvalues(self):
        '''This will move the csv files which contains all the null values in a columns'''
        csv_file_path='PredictionGoodRawDataFolder'
        for f in os.listdir(csv_file_path):
            data=pd.read_csv(csv_file_path+'/'+f)
            for col in data.columns:
                if data[col].isnull().sum()==len(data[col]):
                    try:
                        shutil.move(csv_file_path+'/'+f,'PredictionBadRawDataFolder')
                        file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
                        message=f"\tMove the file: {f} to PredictionBadRawDataFolder because this file contains all the null values in a  column: {col}"
                        self.log.log(file,message)
                        file.close()
                        break
                    except Exception as e:
                        file=open('PredictionLogs/Exception.txt','a+')
                        message=f"\tCouldn't move the file: {f} to PredictionBadRawDataFolder in which this file contains all the null values in a  column: {col} due to error: {str(e)}"
                        self.log.log(file,message)
                        file.close()
    def convertNANvaluesToNULL(self):
        '''As the Dtabase don't understand the Nan values so we convert it into string 'NULL' '''
        try:
            csv_file_path='PredictionGoodRawDataFolder'
            file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
            for f in os.listdir(csv_file_path):
                data=pd.read_csv(csv_file_path+'/'+f)
                # renamedFirstColumn()
                data.fillna('NULL',inplace=True)
                data['Wafer'] = data['Wafer'].str[6:]
                data.to_csv(csv_file_path+'/'+f,index=False,header=True)
                # data=pd.read_csv(csv_file_path+'/'+f)
                message=f"\tSuccessfully convert the file {f} NAN values to 'NULL' "

                self.log.log(file,message)
            file.close()
        except OSError:
            file=open('PredictionLogs/Exception.txt','a+')
            message=f"\tCouldn't convert the file {f}  NAN values to 'NULL' due to Operating System module error"
            self.log.log(file,message)
            file.close()
        except Exception as e:
            file=open('PredictionLogs/Exception.txt','a+')
            message=f"\tCouldn't convert the file {f}  NAN values to 'NULL' due to an unknown error: {e}"
            self.log.log(file,message)
            file.close()
    def renamedFirstColumn(self):
        '''Renamed first column from Unnamed: 0 to Wafer'''
        try:
            csv_file_path='PredictionGoodRawDataFolder'
            for f in os.listdir(csv_file_path):
                data=pd.read_csv(csv_file_path+'/'+f)
                data.rename(columns={'Unnamed: 0':'Wafer'},inplace=True)
                data.to_csv(csv_file_path+'/'+f,index=False)
            # file=open('PredictionLogs/PredictionDataValidationlogs.txt','a+')
            # message=f"\tSuccessfully renamed the first file {f} column from 'Unnamed: 0' to 'Wafer'"
            # self.log.log(file,message)
            # file.close()
        except OSError:
            # file=open('PredictionLogs/Exception.txt','a+')
            # message=f"\tCouldn't renamed the first file {f} column from 'Unnamed: 0' to 'Wafer' due to Operating System module error"
            # self.log.log(file,message)
            # file.close()
            raise e
        except Exception as e:
            raise e
            # file=open('PredictionLogs/Exception.txt','a+')
            # message=f"\tCouldn't renamed the first file {f} column from 'Unnamed: 0' to 'Wafer' due to an unknown error: {e}"
            # self.log.log(file,message)
            # file.close()
        






                





        
        



