from application_loging import app_logger
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator 
class clustering:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/clustering.txt','a+')
        self.Exceptionfile=open('TrainingLogs/Exception.txt','a+')
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

    def __str__(self):
        self.file.close()
        self.Exceptionfile.close()






