from application_loging import app_logger
import json,sys,os
import re
import shutil
import pandas as pd
class TrainingRawDataValidation:
    def __init__(self,path):
        self.directory_path=path
        self.log=app_logger.logger()
        self.schema_path='train_schema.json'
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
            file=open('TrainingLogs/valuesFromSchemaLogs.txt','a+')
            message=f"\tSucessfully send values from schema.json file values are LengthOfDateStampInFile:{LengthOfDateStampInFile}\t\t  LengthOfTimeStampInFile:{LengthOfTimeStampInFile}\t\t NumberofColumns:{NumberofColumns}\n"
            self.log.log(file,message)
            file.close()
        except ValueError:
            file=open('TrainingLogs/valuesFromSchemaLogs.txt','a+')
            message=f"\tValue not found inside {self.schema_path}"
            self.log.log(file,message)
            file.close()
            raise ValueError

        except KeyError:
            file=open('TrainingLogs/valuesFromSchemaLogs.txt','a+')
            message=f"\tKey not found inside {self.schema_path}"
            self.log.log(file,message)
            file.close()
            raise KeyError

        except Exception as e:
            file=open('TrainingLogs/valuesFromSchemaLogs.txt','a+')
            message=f"\tError while taking ValuesFromSchema function: {str(e)}"
            self.log.log(file,message)
            file.close()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            raise e

        
        return ColName, LengthOfDateStampInFile, LengthOfTimeStampInFile, NumberofColumns
    def regex(self):
        """ This will return the manual regex expression that the file name shoud support"""
        return "Training_Batch_Files_wafer+['_']+[\d]+['_']+[\d]+.csv"
        # "['wafer']+['\_'']+[\d_]+[\d]+\.csv"
    def TrainingdeleteGoodRawDataFolder(self):
        """For deleting the Good Raw Data Folder if Present, because every time we began with the new Good Data folder"""
        GoodDataPath='TrainingGoodRawDataFolder'
        try:
            if os.path.isdir(GoodDataPath):
                shutil.rmtree(GoodDataPath)
                file=open('TrainingLogs/TrainingdeleteGoodRawDataFolder.txt','a+')
                message=f"Good folder Deleted Successfully"
                self.log.log(file,message)
                file.close()
            else:
                file=open('TrainingLogs/TrainingdeleteGoodRawDataFolder.txt','a+')
                message=f"\tThere is no Good Data Folder"
                self.log.log(file,message)
                file.close()
        except Exception as e:
            file=open('TrainingLogs/Exception.txt','a+')
            message=f"\tcould not delete the Good directory error is, {str(e)}"
            self.log.log(file,message)
            file.close()
    def TrainingdeleteBadRawDataFolder(self):
        """For deleting the Bad Raw Data Folder if Present, because every time we began with the new Good Data folder"""
        BadDataPath='TrainingBadRawDataFolder'
        try:
            if os.path.isdir(BadDataPath):
                shutil.rmtree(BadDataPath)
                file=open('TrainingLogs/TrainingdeleteBadRawDataFolder.txt','a+')
                message=f"\tBad folder Deleted Successfully"
                self.log.log(file,message)
                file.close()
            else:
                file=open('TrainingLogs/TrainingdeleteGoodRawDataFolder.txt','a+')
                message=f"\tThere is no Bad Data Folder"
                self.log.log(file,message)
                file.close()
        except Exception as e:
            file=open('TrainingLogs/Exception.txt','a+')
            message=f"\tcould not delete the Bad directory error is, {str(e)}"
            self.log.log(file,message)
            file.close()
    def TrainingcreateGoodRawDataFolder(self):
        '''This will create the Good Raw Data Folder'''
        try:
            # GoodDataPath='wafer_fault_detection'
            os.system('mkdir TrainingGoodRawDataFolder')
            file=open('TrainingLogs/TrainingGoodRawDataFolder.txt','a+')
            message=f"\tSucccessfully created the TrainingGoodRawDataFolder directory"
            self.log.log(file,message)
            file.close()
        except Exception as e:
            file=open('TrainingLogs/Exception.txt','a+')
            message=f"\tcould not create the TrainingGoodRawDataFolder directory error is, {str(e)}"
            self.log.log(file,message)
            file.close()
    def TrainingcreateBadRawDataFolder(self):
        '''This will create the Bad Raw Data Folder'''
        try:
            # GoodDataPath='wafer_fault_detection'
            os.system('mkdir TrainingBadRawDataFolder')
            file=open('TrainingLogs/TrainingBadRawDataFolder.txt','a+')
            message=f"\tSucccessfully created the TrainingBadRawDataFolder directory"
            self.log.log(file,message)
            file.close()
        except Exception as e:
            file=open('TrainingLogs/Exception.txt','a+')
            message=f"\tcould not create the TrainingBadRawDataFolder directory error is, {str(e)}"
            self.log.log(file,message)
            file.close()



    def validateRawDataByRegexExpression(self,regex,LengthOfDateStampInFile,LengthOfTimeStampInFile):
        self.TrainingdeleteGoodRawDataFolder()
        self.TrainingdeleteBadRawDataFolder()
        self.TrainingcreateGoodRawDataFolder()
        self.TrainingcreateBadRawDataFolder()
        files=os.listdir(self.directory_path)
        for f in files:
            if re.match(regex,f):
                # print("file match,",file)
                file_name,_=f.split('.')
                # print(file_name.split('_')[4:])
                filedatestamp,timestamptime=file_name.split('_')[4:]
                # print(type(timestamptime))
                # print(type(filedatestamp))
                # filedatestamp=int(filedatestamp)
                # timestamptime=int(timestamptime)

                if len(filedatestamp)==LengthOfDateStampInFile:
                    # print('filedatestamp',len(filedatestamp),f)
                    if len(timestamptime)==LengthOfTimeStampInFile:
                        # print('timestamptime',len(timestamptime),f)

                        shutil.copy(f'Training_Batch_Files/{f}','TrainingGoodRawDataFolder')
                        file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
                        message=f"\tSucccessfully Validate the File name: {f} and copy it to ,TrainingGoodRawDataFolder"
                        self.log.log(file,message)
                        file.close()
                    else:
                        shutil.copy(f'Training_Batch_Files/{f}','TrainingBadRawDataFolder')
                        file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
                        message=f"\tFile name is not according to Schema.json, filename: {f}"
                        self.log.log(file,message)
                        file.close()
                else:
                    shutil.copy(f'Training_Batch_Files/{f}','TrainingBadRawDataFolder')
                    file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
                    message=f"\tFile name is not according to Schema.json, filename: {f}"
                    self.log.log(file,message)
                    file.close()
            else:
                shutil.copy(f'Training_Batch_Files/{f}','TrainingBadRawDataFolder')
                file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
                message=f"\tFile name is not according to Schema.json, filename: {f}"
                self.log.log(file,message)
                file.close()
    def validateDataByNumberOfColumns(self,NumberofColumns):
        ''''This will check the number of column according to our schema file'''
        path='TrainingGoodRawDataFolder'
        files=os.listdir(path)
        for f in files:
            # print("read csv",pd.read_csv(path+'/'+f).shape[1])
            # print("Number of columns",NumberofColumns)
            if NumberofColumns==pd.read_csv(path+'/'+f).shape[1]:
                file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
                message=f"\tfile {f} columns is matching with our Schema"
                self.log.log(file,message)
                file.close()
            else:
                try:
                    shutil.move(path+'/'+f,'TrainingBadRawDataFolder')
                    file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
                    message=f"\tMove the file: {f} to TrainingBadRawDataFolder because columns was not matching with our Schema"
                    self.log.log(file,message)
                    file.close()
                except Exception as e:
                    file=open('TrainingLogs/Exception.txt','a+')
                    message=f"\tCouldn't move the file: {f} to TrainingBadRawDataFolder in which columns was not matching with our Schema due to error: {str(e)}"
                    self.log.log(file,message)
                    file.close()
    def validateColumnsbymissingvalues(self):
        '''This will move the csv files which contains all the null values in a columns'''
        csv_file_path='TrainingGoodRawDataFolder'
        for f in os.listdir(csv_file_path):
            data=pd.read_csv(csv_file_path+'/'+f)
            for col in data.columns:
                if data[col].isnull().sum()==len(data[col]):
                    try:
                        shutil.move(csv_file_path+'/'+f,'TrainingBadRawDataFolder')
                        file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
                        message=f"\tMove the file: {f} to TrainingBadRawDataFolder because this file contains all the null values in a  column: {col}"
                        self.log.log(file,message)
                        file.close()
                        break
                    except Exception as e:
                        file=open('TrainingLogs/Exception.txt','a+')
                        message=f"\tCouldn't move the file: {f} to TrainingBadRawDataFolder in which this file contains all the null values in a  column: {col} due to error: {str(e)}"
                        self.log.log(file,message)
                        file.close()
    def convertNANvaluesToNULL(self):
        '''As the Dtabase don't understand the Nan values so we convert it into string 'NULL' '''
        try:
            csv_file_path='TrainingGoodRawDataFolder'
            file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
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
            file=open('TrainingLogs/Exception.txt','a+')
            message=f"\tCouldn't convert the file {f}  NAN values to 'NULL' due to Operating System module error"
            self.log.log(file,message)
            file.close()
        except Exception as e:
            file=open('TrainingLogs/Exception.txt','a+')
            message=f"\tCouldn't convert the file {f}  NAN values to 'NULL' due to an unknown error: {e}"
            self.log.log(file,message)
            file.close()
    def renamedFirstColumn(self):
        '''Renamed first column from Unnamed: 0 to Wafer'''
        # pass
        try:
            csv_file_path='TrainingGoodRawDataFolder'
            for f in os.listdir(csv_file_path):
                data=pd.read_csv(csv_file_path+'/'+f)
                data.rename(columns={'Unnamed: 0':'Wafer'},inplace=True)
                data.to_csv(csv_file_path+'/'+f,index=False)
            file=open('TrainingLogs/TrainingDataValidationlogs.txt','a+')
            message=f"\tSuccessfully renamed the first file {f} column from 'Unnamed: 0' to 'Wafer'"
            self.log.log(file,message)
            file.close()
        except OSError:
            file=open('TrainingLogs/Exception.txt','a+')
            message=f"\tCouldn't renamed the first file {f} column from 'Unnamed: 0' to 'Wafer' due to Operating System module error"
            self.log.log(file,message)
            file.close()
        except Exception as e:
            file=open('TrainingLogs/Exception.txt','a+')
            message=f"\tCouldn't renamed the first file {f} column from 'Unnamed: 0' to 'Wafer' due to an unknown error: {e}"
            self.log.log(file,message)
            file.close()
        






                





        
        



