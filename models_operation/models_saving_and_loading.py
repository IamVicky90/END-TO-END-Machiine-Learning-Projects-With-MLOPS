from application_loging import app_logger
import pickle
import os
import shutil
class model:
    def __init__(self,file_path,exception_file_path):
        self.log=app_logger.logger()
        self.file=open(file_path,'a+')
        self.Exceptionfile=open(exception_file_path,'a+')
    def model_savings(self,model_name,model):
        try:
            dir_name='Models'
            if not os.path.isdir(os.getcwd()+'/'+dir_name):
                os.mkdir(dir_name)
            with open(dir_name+'/'+model_name+'.sav','wb') as f:
                pickle.dump(model,f)
                self.log.log(self.file,f'\tSuccessfully dump/save the model: {str(model_name)}.sav')
        except Exception as e:
                self.log.log(self.file,f'\tFacing error while dumping/saving the model: {str(model_name)}.sav error: '+str(e))
                self.log.log(self.Exceptionfile,f'\tFacing error while dumping/saving the model: {str(model_name)}.sav error: '+str(e))
    def load_model(self,model_name):
        '''Parameter hint:
           model_name: give the model name if its present in this folder otherwise give its path'''
        try:
            with open(model_name,'rb') as f:
                load_model=pickle.load(f)
                self.log.log(self.file,f'\tSuccessfully loading the model: {str(model_name)}.sav')
                return load_model
        except Exception as e:
                self.log.log(self.file,f'\tFacing error while loading the model: {str(model_name)}.sav error: '+str(e))
                self.log.log(self.Exceptionfile,f'\tFacing error while loading the model: {str(model_name)}.sav error: '+str(e))
               
    def load_model_by_cluster(self,cluster_number):
        try:
            i=str(cluster_number)
            for model in os.listdir('Models'):
                if i in model:
                    self.log.log(self.file,f'\tSuccessfully load model by cluster')
                    return self.load_model('Models'+'/'+model)

        except Exception as e:
                self.log.log(self.file,f'\tFacing error while loading model by cluster  error: '+str(e))
                self.log.log(self.Exceptionfile,f'\tFacing error while loading model by cluster  error: '+str(e))
                self.Exceptionfile.close()
                self.file.close()
            

    def __str__(self):
        self.file.close()
        self.Exceptionfile.close()
                
            

