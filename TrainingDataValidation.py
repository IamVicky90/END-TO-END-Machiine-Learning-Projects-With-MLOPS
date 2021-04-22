from application_loging import app_logger
from TrainingRawDataValidation.TrainingRawDataValidation import TrainingRawDataValidation
from DataBaseOperation.dboperation import dbOperation
class TrainValidation:
    def __init__(self,path):
        self.raw_data=TrainingRawDataValidation(path)
        self.dbOperation=dbOperation('TrainingLogs')
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
        TableName='Good_Raw_Data'
        dbname='wafer.db'
        self.dbOperation.createTable(TableName,ColNames,dbname)
        self.log.log(self.file,"\tSuccessfully complete the process of method createTable")
        self.dbOperation.insertValuesintoTable(TableName,dbname,'TrainingGoodRawDataFolder')
        self.log.log(self.file,"\tSuccessfully complete the process of method insertValuesintoTable")
        self.dbOperation.inputvaluesintocsv(TableName,dbname,'TrainingFileFromDB','trainingInput.csv')
        self.log.log(self.file,"\tSuccessfully complete the process of method inputvaluesintocsv")
        self.file.close()



