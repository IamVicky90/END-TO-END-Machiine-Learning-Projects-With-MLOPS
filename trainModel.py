from application_loging import app_logger
from load_data import getdata
from Processing import data_preprocessing, clustering
from sklearn.model_selection import train_test_split
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
            x=clustering_data.create_clusters(x,no_of_clusters)
            self.log.log(self.file,f'\tSuccessfully complete the process of create_clusters')
            x['target']=y
            for i in x['Clusters'].unique():
                data_=x[x['Clusters']==i]
                independent_features=data_.drop(['target','Clusters'],axis=1)
                dependent_feature=data_['target']
                x_train,x_test,y_train,y_test=train_test_split(independent_features,dependent_feature,test_size=1/3,random_state=786)


            self.file.close()
        except Exception as e:
            self.file.close()
            raise e
