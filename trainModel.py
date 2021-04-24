from application_loging import app_logger
from load_data import getdata
from Processing import data_preprocessing
from sklearn.model_selection import train_test_split
from model_finder.tuner import model_finder
from Processing import clustering
from models_operation.models_saving_and_loading import model
from Processing import oversampling
class modelTraining:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/tainModelLogs.txt','a+')
        self.model_finder_obj=model_finder()
        self.model_obj=model('TrainingLogs/models_saving_and_loading_logs.txt','TrainingLogs/Exception.txt')
    def training_data(self):
        try:
            obj=getdata.getdata('TrainingLogs','getdata.txt')
            df=obj.datagetter('TrainingFileFromDB/trainingInput.csv')
            self.log.log(self.file,'\tPandas Dataframe executed successfully')
            processing=data_preprocessing.preocess_data('TrainingLogs/data_preprocessing.txt','TrainingLogs/Exception.txt')
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
            sampling_obj=oversampling.sampling()
            flag= sampling_obj.checking_for_samples_needed_or_not(x,'target',30)
            # x.to_csv('x.csv')
            for i in x['Clusters'].unique():
                data_=x[x['Clusters']==i]
                independent_features=data_.drop(['target','Clusters'],axis=1)
                dependent_feature=data_['target']
                # independent_features.to_csv(f'independent_features_{str(i)}.csv') 
                # dependent_feature.to_csv(f'dependent_feature_{str(i)}.csv') 
                x_train,x_test,y_train,y_test=train_test_split(independent_features,dependent_feature,test_size=1/3,random_state=786)
                if flag:
                    x_train, y_train=sampling_obj.creating_samples(x_train,y_train)
                model_name,model=self.model_finder_obj.best_model(x_train,x_test,y_train,y_test)
                self.model_obj.model_savings(model_name+'_cluster_'+str(i),model)



            self.file.close()
        except Exception as e:
            self.file.close()
            raise e
