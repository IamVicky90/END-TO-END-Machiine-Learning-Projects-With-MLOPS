from application_loging import app_logger
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator 
from models_operation.models_saving_and_loading import model
class clustering:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/clustering.txt','a+')
        self.Exceptionfile=open('TrainingLogs/Exception.txt','a+')
        self.model_obj=model()
    def elbow_method(self,data):
        try:
            wcss=[]
            for i in range(1,11):
                kmeans=KMeans(n_clusters=i,random_state=42)
                kmeans.fit(data)
                wcss.append(kmeans.inertia_)
            plt.plot(range(1,11),wcss)
            plt.title('The elbow method')
            plt.xlabel('number of clusters')
            plt.ylabel('WCSS')
            plt.savefig('Processing/k-means-elbowplt.png')
            kn=KneeLocator(range(1,11),wcss,curve='convex',direction='decreasing')
            self.log.log(self.file,f'\t{kn.knee} are the appropriate number for clusters')
            return kn.knee
        except Exception as e:
            self.log.log(self.file,'\tError while knowing the appropraite number of clusters error is: '+str(e))
            self.log.log(self.Exceptionfile,'\tError while knowing the appropraite number of clusters error is: '+str(e))
    def create_clusters(self, data,number_of_clusters):
        try:
            kmeans=KMeans(n_clusters=number_of_clusters,random_state=42)
            y_kmeans=kmeans.fit_predict(data)
            data['Clusters']=y_kmeans
            self.log.log(self.file,'\tSuccessfully created the clusters in create_clusters method!')
            try:
                self.model_obj.model_savings('kmeans_clustering',kmeans)
                self.log.log(self.file,'Successfully called the model_obj')

            except Exception as e:
                self.log.log(self.file,'Error while calling the model_obj error: '+str(e))
                self.log.log(self.Exceptionfile,'Error while calling the model_obj error: '+str(e))

            return data
        except Exception as e:
            self.log.log(self.file,'\tError while making the clusters in create_clusters method'+str(e))
            self.log.log(self.Exceptionfile,'\tError while making the clusters in create_clusters method'+str(e))

    def __str__(self):
        self.file.close()
        self.Exceptionfile.close()






