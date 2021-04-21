from application_loging import app_logger
from collections import Counter
from imblearn.over_sampling import RandomOverSampler
class sampling:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/oversamplig.txt','a+')
        self.exception_file=open('TrainingLogs/Exception.txt','a+')
    def checking_for_samples_needed_or_not(self,data,target_feature,percentage):
        '''This will tell you whether you need oversampling for the provided percentage or not return True it is neded otherwise False
        Prameters:
        data:dataFrame,
        target_feature: Dependent Feature/y_label,
        percentage: The percentage within which you want toi ignore oversampling,
        '''
        try:
            dic=Counter(data[target_feature])
            val=list(dic.values())
            if val[0]<val[1]:
                percent=(val[0]/val[1])*100
            else:
                percent=(val[1]/val[0])*100
            if percent<percentage:
                output=True
                self.log.log(self.file,f'\tpercent of difference of data is {percent} so we oversampling is neded in this case')
            else:
                output=False
                self.log.log(self.file,f"\tpercent of difference of data is {percent} so we don't needed any oversampling is neded in this case")
            return output
        except Exception as e:
                self.log.log(self.file,"\tAn error is occured in checking_for_samples_needed_or_not error: "+str(e))
                self.log.log(self.exception_file,"\tAn error is occured in checking_for_samples_needed_or_not error: "+str(e))
                raise e
    def creating_samples(self,X_train,y_train):
        try:
            ros=RandomOverSampler(0.75)
            X_train_ns,y_train_ns=ros.fit_resample(X_train,y_train)
            print("The number of classes before fit {}".format(Counter(y_train)))
            print("The number of classes after fit {}".format(Counter(y_train_ns)))
            self.log.log(self.file,"\tThe number of classes before fit {}".format(Counter(y_train))+"\t"+"The number of classes after fit {}".format(Counter(y_train_ns)))
            return X_train_ns,y_train_ns
        except Exception as e:
            self.log.log(self.file,"\tAn error is occured in creating_samples error: "+str(e))
            self.log.log(self.exception_file,"\tAn error is occured in creating_samples error: "+str(e))
            raise e



    def __str__(self):
        self.file.close()
        self.exception_file.close()


