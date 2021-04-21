from application_loging import app_logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import xgboost
from sklearn.metrics import accuracy_score,roc_auc_score
class model_finder:
    def __init__(self):
        self.log=app_logger.logger()
        self.file=open('TrainingLogs/tuner.txt','a+')
        self.exception_file=open('TrainingLogs/Exception.txt','a+')
    def best_model(self,x_train,x_test,y_train,y_test):
        try:
            rfc=RandomForestClassifier()
            rf=self.rfc_hyperparameter_tunning(rfc,x_train,y_train)
            # rf.fit(train_features, train_labels)
            # CV_rfc.fit(x_train, y_train)
            rf.fit(x_train,y_train)
            y_pred=rf.predict(x_test)
            self.log.log(self.file,f'\tSucessfully loaded, fit and predict the x_test by Random Forest')
        except Exception as e:
            self.log.log(self.file,f'\tCouldn"t loaded, fit and predict the x_test by Random Forest error: '+str(e))
            self.log.log(self.exception_file,f'\tCouldn"t loaded, fit and predict the x_test by Random Forest error: '+str(e))
            raise e

        if len(y_test.unique())==1:
            #if there is only one value for prediction then roc_auc_score will give us an error so in this case we use accuracy score
            score_rf=accuracy_score(y_test,y_pred)
            self.log.log(self.file,f'\tAccuracy score for Random_Forest is {score_rf}')
        else:
            score_rf=roc_auc_score(y_test,y_pred)
            self.log.log(self.file,f'\troc_auc_score score for Random_Forest is {score_rf}')
        try:
            xgb=xgboost.XGBClassifier()
            xg=self.xg_hyperparameter_tunning(xgb,x_train,y_train)
            xg.fit(x_train,y_train)
            xg_pred=xg.predict(x_test)
            self.log.log(self.file,f'\tSucessfully loaded, fit and predict the x_test by XGBClassifier')
        except Exception as e:
            self.log.log(self.file,f'\tCouldn"t loaded, fit and predict the x_test by XGBClassifier error: '+str(e))
            self.log.log(self.exception_file,f'\tCouldn"t loaded, fit and predict the x_test by XGBClassifier error: '+str(e))
            raise e
        if len(y_test.unique())==1:
            #if there is only one value for prediction then roc_auc_score will give us an error so in this case we use accuracy score
            score_xg=accuracy_score(y_test,xg_pred)
            self.log.log(self.file,f'\taccuracy_score score for XGBClassifier is {score_xg}')
        else:
            score_xg=roc_auc_score(y_test,xg_pred)
            self.log.log(self.file,f'\troc_auc_score score for XGBClassifier is {score_xg}')
        if score_rf>score_xg:
            model_name='Random_Forest'
            model=rf

        else:
            model_name='XGBClassifier'
            model=xg
            self.log.log(self.file,f'\tBest model name for this cluster is {model_name}')
        return model_name,model
    def rfc_hyperparameter_tunning(self,rfc,train_x,train_y):
        try:
            param_grid = { 
            'n_estimators': [200, 500],
            'max_features': ['auto', 'sqrt', 'log2'],
            'max_depth' : [4,5,6,7,8],
            'criterion' :['gini', 'entropy']}
            grid = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 5)
            grid.fit(train_x, train_y)
            criterion = grid.best_params_['criterion']
            max_depth = grid.best_params_['max_depth']
            max_features = grid.best_params_['max_features']
            n_estimators =grid.best_params_['n_estimators']

            #creating a new model with the best parameters
            clf = RandomForestClassifier(n_estimators=n_estimators, criterion=criterion,
                                                max_depth=max_depth, max_features=max_features)
            
            self.log.log(self.file,f'\tBest params for random forest are; criterion : {criterion}, max_depth : {max_depth}, max_features : {max_features}, n_estimators : {n_estimators}')
            return clf
        except Exception as e:
            self.log.log(self.file,'\tError while knowing the best params for random forest error : '+str(e))
            self.log.log(self.exception_file,'\tError while knowing the best params for random forest error : '+str(e))
            raise e
    def xg_hyperparameter_tunning(self,xgb,train_x,train_y):
        try:
            param_grid_xgboost = {

                    'learning_rate': [0.5, 0.1, 0.01, 0.001],
                    'max_depth': [3, 5, 10, 20],
                    'n_estimators': [10, 50, 100, 200]

                }
            # Creating an object of the Grid Search class
            grid= GridSearchCV(xgb,param_grid_xgboost, verbose=3,cv=5)
            # finding the best parameters
            grid.fit(train_x, train_y)

            # extracting the best parameters
            learning_rate = grid.best_params_['learning_rate']
            max_depth = grid.best_params_['max_depth']
            n_estimators = grid.best_params_['n_estimators']

            # creating a new model with the best parameters
            xg = xgboost.XGBClassifier(learning_rate=learning_rate, max_depth=max_depth, n_estimators=n_estimators)
            # training the mew model
            self.log.log(self.file,f'\tBest params for XGBOOST are; learning_rate : {learning_rate}, max_depth : {max_depth},  n_estimators : {n_estimators}')
            return xg
        except Exception as e:
            self.log.log(self.file,'\tError while knowing the best params for XGBOOST error : '+str(e))
            self.log.log(self.exception_file,'\tError while knowing the best params for XGBOOST error : '+str(e))
            raise e
    def __str__(self):
        self.file.close()
        self.exception_file.close()




        

