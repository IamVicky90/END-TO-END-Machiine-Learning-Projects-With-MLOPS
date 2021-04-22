from application_loging import app_logger
from PredictionRawDataValidation.PredictionRawDataValidation import PredictionRawDataValidation
from DataBaseOperation.dboperation import dbOperation
class PredictionValidation:
    def __init__(self,path):
        self.raw_data=PredictionRawDataValidation(path)
        self.dbOperation=dbOperation('PredictionLogs')
        self.path=path
        self.log=app_logger.logger()
        self.file=open('PredictionLogs/MainPredictionDataValidationlogs.txt','a+')
        
    def PredictionValidation(self):
        try:
            self.log.log(self.file,"\tStarting the PredictionValidation Part")
            ColNames, LengthOfDateStampInFile, LengthOfTimeStampInFile, NumberofColumns=self.raw_data.ValuesfromSchema()
            regex=self.raw_data.regex()
            self.raw_data.validateRawDataByRegexExpression(regex,LengthOfDateStampInFile,LengthOfTimeStampInFile)
            self.log.log(self.file,"\tSuccessfully complete the process of validating the csv data fomat")
            self.raw_data.validateDataByNumberOfColumns(NumberofColumns)
            self.log.log(self.file,"\tSuccessfully complete the process of validating the  no. of columns")
            self.raw_data.validateColumnsbymissingvalues()
            self.log.log(self.file,"\tSuccessfully complete the process of method validateColumnsbymissingvalues")
            self.raw_data.renamedFirstColumn()
            self.log.log(self.file,"\tSuccessfully complete the process of method renamedFirstColumn")
            self.raw_data.convertNANvaluesToNULL()
            self.log.log(self.file,"\tSuccessfully complete the process of method convertNANvaluesToNULL")
            # con=self.dbOperation.connectionEstablished('wafer.db')
            # self.log.log(self.file,"\tSuccessfully complete the process of method connectionEstablished")
            TableName='Good_Raw_Data_pred'
            dbname='pred_wafer.db'
            self.dbOperation.createTable(TableName,ColNames,dbname)
            self.log.log(self.file,"\tSuccessfully complete the process of method createTable")
            self.dbOperation.insertValuesintoTable(TableName,dbname,'PredictionGoodRawDataFolder')
            self.log.log(self.file,"\tSuccessfully complete the process of method insertValuesintoTable")
            self.dbOperation.inputvaluesintocsv(TableName,dbname,'PredictionFileFromDB','predictionInput.csv')
            self.log.log(self.file,"\tSuccessfully complete the process of method inputvaluesintocsv")
            self.file.close()
        except Exception as e:
            self.file.close()
            raise e



