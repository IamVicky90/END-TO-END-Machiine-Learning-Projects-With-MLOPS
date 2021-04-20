from application_loging import app_logger
import pickle
import os
import shutil
class model:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/models_saving_and_loading_logs.txt','a+')
        self.Exceptionfile=open('TrainingLogs/Exception.txt','a+')
        self.Exceptionfile=open('TrainingLogs/Exception.txt','a+')
    def model_savings(self,model_name,model):
        try:
            dir_name='Models'
            if os.path.isdir(os.getcwd()+'/'+dir_name):
                shutil.rmtree(dir_name)
            os.mkdir(dir_name)
            with open(dir_name+'/'+model_name+'.sav','wb') as f:
                pickle.dump(model,f)
                self.log.log(self.file,f'\tSuccessfully dump/save the model: {str(model_name)}.sav')
                self.file.close()
                self.Exceptionfile.close()
        except Exception as e:
                self.log.log(self.file,f'\tFacing error while dumping/saveing the model: {str(model_name)}.sav error: '+str(e))
                self.log.log(self.Exceptionfile,f'\tFacing error while dumping/saveing the model: {str(model_name)}.sav error: '+str(e))
                self.file.close()
                self.Exceptionfile.close()
    # def load_model(self):
    #     pass
    # def __str__(self):
    #     self.file.close()
    #     self.Exceptionfile.close()
                
            

