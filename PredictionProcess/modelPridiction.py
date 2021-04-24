from application_loging import app_logger
from load_data import getdata
from Processing import data_preprocessing
from model_finder.tuner import model_finder
from Processing import clustering
from models_operation.models_saving_and_loading import model
from models_operation import models_saving_and_loading
import pandas as pd
class predictModel:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('PredictionLogs/modelPrediction.py','a+')
    def processdata(self):
        try:
            obj=getdata.getdata('PredictionLogs','getdata.txt')
            df=obj.datagetter('PredictionFileFromDB/predictionInput.csv')
            self.log.log(self.file,'\tPandas Dataframe executed successfully')
            processing=data_preprocessing.preocess_data('PredictionLogs/data_preprocessing.txt','PredictionLogs/Exception.txt')
            self.log.log(self.file,'\tSuccessfully called the process_data method from Processing')
            isnull=processing.isnull(df)
            self.log.log(self.file,'\tSuccessfully complete the process of isnull')
            if isnull:
                df=processing.knn_nan_values_imputer(df)
                self.log.log(self.file,'\tSuccessfully complete the process of knn_nan_values_imputer')
            else:
                self.log.log(self.file,'\t No nan values present in this dataset')
            df=processing.drop_column_with_std_zero(df)
            models_sav_and_load_obj=models_saving_and_loading.model('PredictionLogs/models_saving_and_loading_logs.txt','PredictionLogs/Exception.txt')
            load_model_=models_sav_and_load_obj.load_model('Models/kmeans_clustering.sav')
            df['Clusters']=load_model_.predict(df.drop(['Wafer'],axis=1))
            for i in df['Clusters'].unique():
                df_cluster=df[df['Clusters']==i]
                df_cluster_wafer_list=list(df_cluster['Wafer'])
                df_cluster=df_cluster.drop(['Wafer','Clusters'],axis=1)
                model_=models_sav_and_load_obj.load_model_by_cluster(i)
                result=list(model_.predict(df_cluster))
                result = pd.DataFrame(list(zip(df_cluster_wafer_list,result)),columns=['Wafer','Prediction'])
                path="Prediction_Output_File/Predictions.csv"
                result.to_csv("Prediction_Output_File/Predictions.csv",header=True,mode='a+') 
            return result
        except Exception as e:
            self.file.close()
            raise e
            


