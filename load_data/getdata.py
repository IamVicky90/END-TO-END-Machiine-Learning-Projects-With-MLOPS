from application_loging import app_logger
import pandas as pd
class getdata:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/getdata.txt','a+')
        self.exception_file=open('TrainingLogs/Exception.txt','a+')
    def datagetter(self):
        try:
            df=pd.read_csv('TrainingFileFromDB/trainingInput.csv')
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
    


