from application_loging import app_logger
import pandas as pd
class getdata:
    def __init__(self,logFolder,loggerFilename):
        self.log=app_logger.logger()
        self.file=open(f'{logFolder}/{loggerFilename}','a+')
        self.exception_file=open(f'{logFolder}/Exception.txt','a+')
    def datagetter(self,filepath):
        try:
            df=pd.read_csv(filepath)
            self.log.log(self.file,'\tSucessfully converted data into pandas dataframe')
            self.file.close()
            self.exception_file.close()
            return df
        except Exception as e:
            self.log.log(self.file,'\tError Occured while converted data into pandas dataframe')
            self.file.close()
            self.log.log(self.exception_file,'\tError Occured while converted data into pandas dataframe exception is: '+str(e))
            self.exception_file.close()
            self.file.close()
    


