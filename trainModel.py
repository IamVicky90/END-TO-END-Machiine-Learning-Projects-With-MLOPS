from application_loging import app_logger
from load_data import getdata
from Processing import data_preprocessing, clustering
class modelTraining:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/tainModelLogs.txt','a+')
    def training_data(self):
        try:
            obj=getdata.getdata()
            df=obj.datagetter()
            self.log.log(self.file,'\tPandas Dataframe executed successfully')
            processing=data_preprocessing.preocess_data()
            self.log.log(self.file,'\tSuccessfully called the process_data method from Processing')
            df=processing.remove_column(df,['Wafer'])
            self.log.log(self.file,'\tSuccessfully complete the process of remove columns')
            x,y=processing.seprate_labels_and_features(df)
            self.log.log(self.file,'\tSuccessfully complete the process of seprate_labels_and_features')
            isnull=processing.isnull(df)
            self.log.log(self.file,'\tSuccessfully complete the process of isnull')
            if isnull:
                x=processing.knn_nan_values_imputer(x)
                self.log.log(self.file,'\tSuccessfully complete the process of knn_nan_values_imputer')
            else:
                self.log.log(self.file,'\t No nan values present in this dataset')
            x=processing.drop_column_with_std_zero(x)
            clustering_data=clustering.clustering()
            no_of_clusters=clustering_data.elbow_method(x)
            self.log.log(self.file,f'\tSuccessfully complete the process of elbow_method the no of clusters are {no_of_clusters}')
            print(no_of_clusters)           


            self.file.close()
        except Exception as e:
            self.file.close()
            raise e
