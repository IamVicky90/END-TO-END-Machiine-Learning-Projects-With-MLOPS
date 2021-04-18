from application_loging import app_logger
from TrainingRawDataValidation.TrainingRawDataValidation import TrainingRawDataValidation
from DataBaseOperation.dboperation import dbOperation
class TrainValidation:
    def __init__(self,path):
        self.raw_data=TrainingRawDataValidation(path)
        self.dbOperation=dbOperation()
        self.path=path
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/MainTrainingDataValidationlogs.txt','a+')
        
    def TrainValidation(self):
        self.log.log(self.file,"\tStarting the TrainigValidation Part")
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
        self.dbOperation.createTable('Good_Raw_Data',ColNames)
        self.log.log(self.file,"\tSuccessfully complete the process of method createTable")
        self.dbOperation.insertValuesintoTable('wafer.db')
        self.log.log(self.file,"\tSuccessfully complete the process of method insertValuesintoTable")
        self.dbOperation.inputvaluesintocsv()
        self.log.log(self.file,"\tSuccessfully complete the process of method inputvaluesintocsv")
        self.file.close()



