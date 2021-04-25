# END-TO-END-Wafer-Machiine-Learning-Project-With-MLOPS
## This is a Wafer Fault detection ML project, it tells you whether the wafer has some problems or not.
## Table of Contents.
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Docker Installation](#Docker)
  * [Directory Tree](#directory-tree)
  * [Libraries](#libraries)
  
  ## Demo
  Deployment Link. https://wafer-fault-detection-mlops.herokuapp.com/ .
  
 
 __Frontent based on html, css.__
  
  ![error check your internet](https://github.com/IamVicky90/END-TO-END-Wafer-Machiine-Learning-Project-With-MLOPS/blob/main/images/Front.PNG)
  
  

  
 

  
  ## Overview
I made this application to know that whether a particular Wafer has some deffect or not. If it has some defect then we can remove this so that our work runs smoothly.
## Motivation
The motivation behind this is not very interesting, I just want to work in some MLOPS/DEVOPS techniques like a realtime industry do. So i choose this project.

## Technical Aspect
This project is divided into two part:
1. Training a Machine Learning Model.
2. Building deployed, and hosting a Flask web app on Heroku( https://wafer-fault-detection-mlops.herokuapp.com/ ).

## Installation
The Code is written in Python 3.6.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [downloading it](https://github.com/IamVicky90/Plant-Disease-Prediction/archive/main.zip):
```bash
pip install -r requirements.txt
```
## Run
To run the app in a local machine, shoot this command in the project directory:
__Run the follwing command after installing requirements.txt__
```bash
python app.py
```
## Docker
To run the app n docker, you first need dockers installation by using the following steps:
```
For windows go to the link then download and install it : https://docs.docker.com/docker-for-windows/install/
For Ubuntu/Linux, run the command: apt install docker.io  
```
__Follow the following steps to run in dockers as I given a wafer_fault_detection.tar file__
```bash
>> docker load < wafer_fault_detection.tar
>> docker run -p [your port number]:5000 --name [Give any name] wafer_fault_detection:latest
```
## Directory Tree 
```
        PredictionDataValidation.py
        Procfile
        Runtime.txt
        TrainingDataValidation.py
        app.py
        flask_monitoringdashboard.db
        pred_schema.json
        pred_wafer.db
        requirements.txt
        test.py
        trainModel.py
        train_schema.json
        images
            Front.PNG
        .vscode/
            settings.json
        DataBaseOperation/
            dboperation.py
            
        Models/
            XGBClassifier_cluster_0.sav
            XGBClassifier_cluster_1.sav
            XGBClassifier_cluster_2.sav
            kmeans_clustering.sav
        Null_csv/
            null_data_info.csv
        PredictionBadRawDataFolder/
            Prediction_Batch_files_Wafer_13012020_141000.csv
            Prediction_Batch_files_Wafer_14012020_113045.csv
            Prediction_Batch_files_Wafer_15010_130532.csv
            Prediction_Batch_files_wafer_07012020_041011.csv
            Prediction_Batch_files_wafer_20012020_090819.csv
            Prediction_Batch_files_wafer_22022020_041119.csv
            Prediction_Batch_files_wafer_23012020_011008.csv
            Prediction_Batch_files_wafer_28012020_051011.csv
            Prediction_Batch_files_wafer_29012020_060756.csv
            Prediction_Batch_files_wafer_31012020_090811.csv
        PredictionFileFromDB/
            predictionInput.csv
        PredictionGoodRawDataFolder/
            Prediction_Batch_files_wafer_13012020_090817.csv
            Prediction_Batch_files_wafer_16012020_051629.csv
            Prediction_Batch_files_wafer_20022020_090716.csv
            Prediction_Batch_files_wafer_21012020_080913.csv
            Prediction_Batch_files_wafer_23012020_041211.csv
            Prediction_Batch_files_wafer_27012020_080911.csv
            Prediction_Batch_files_wafer_28012020_090817.csv
            Prediction_Batch_files_wafer_28042020_031911.csv
            Prediction_Batch_files_wafer_29012020_050617.csv
        PredictionLogs/
            Exception.txt
            MainPredictionDataValidationlogs.txt
            PredictionBadRawDataFolder.txt
            PredictionDataValidationlogs.txt
            PredictionGoodRawDataFolder.txt
            PredictiondeleteBadRawDataFolder.txt
            PredictiondeleteGoodRawDataFolder.txt
            data_preprocessing.txt
            dbOperation.txt
            getdata.txt
            modelPrediction.py
            models_saving_and_loading_logs.txt
            valuesFromSchemaLogs.txt
        PredictionProcess/
            modelPridiction.py
            __pycache__/
                modelPridiction.cpython-36.pyc
        PredictionRawDataValidation/
            PredictionRawDataValidation.py
            __pycache__/
                PredictionRawDataValidation.cpython-36.pyc
        wafer_fault_detection.tar
        Prediction_Batch_Files/
            Prediction_Batch_files_Wafer_13012020_141000.csv
            Prediction_Batch_files_Wafer_14012020_113045.csv
            Prediction_Batch_files_Wafer_15010_130532.csv
            Prediction_Batch_files_wafer_07012020_041011.csv
            Prediction_Batch_files_wafer_13012020_090817.csv
            Prediction_Batch_files_wafer_16012020_051629.csv
            Prediction_Batch_files_wafer_20012020_090819.csv
            Prediction_Batch_files_wafer_20022020_090716.csv
            Prediction_Batch_files_wafer_21012020_080913.csv
            Prediction_Batch_files_wafer_22022020_041119.csv
            Prediction_Batch_files_wafer_23012020_011008.csv
            Prediction_Batch_files_wafer_23012020_041211.csv
            Prediction_Batch_files_wafer_27012020_080911.csv
            Prediction_Batch_files_wafer_28012020_051011.csv
            Prediction_Batch_files_wafer_28012020_090817.csv
            Prediction_Batch_files_wafer_28042020_031911.csv
            Prediction_Batch_files_wafer_29012020_050617.csv
            Prediction_Batch_files_wafer_29012020_060756.csv
            Prediction_Batch_files_wafer_31012020_090811.csv
        Prediction_Output_File/
            Predictions.csv
        Processing/
            clustering.py
            data_preprocessing.py
            k-means-elbowplt.png
            oversampling.py
            __pycache__/
                clustering.cpython-36.pyc
                clustering.cpython-37.pyc
                clustering.cpython-38.pyc
                data_preprocessing.cpython-36.pyc
                data_preprocessing.cpython-37.pyc
                data_preprocessing.cpython-38.pyc
                oversampling.cpython-36.pyc
                oversampling.cpython-37.pyc
        TrainingBadRawDataFolder/
            Training_Batch_Files_Wafer12_20012.csv
            Training_Batch_Files_Wafer_07012020_000000.csv
            Training_Batch_Files_Wafer_07012020_223345.csv
            Training_Batch_Files_Wafer_08012020_120000.csv
            Training_Batch_Files_Wafer_10012020_131534.csv
            Training_Batch_Files_Wafer_11012020_151432.csv
            Training_Batch_Files_Wafer_12012020_111.csv
            Training_Batch_Files_Wafer_12012020_111213.csv
            Training_Batch_Files_Wafer_13012020_141000.csv
            Training_Batch_Files_Wafer_14012020_113045.csv
            Training_Batch_Files_Wafer_15010_130532.csv
            Training_Batch_Files_Wafer_15012020_130532.csv
            Training_Batch_Files_Wafer_18012020_121532.csv
            Training_Batch_Files_Wafer_19012020_141432.csv
            Training_Batch_Files_Wafer_20012020_135132.csv
            Training_Batch_Files_Wafer_21012020_143634.csv
            Training_Batch_Files_Wafer_22012020_173245.csv
            Training_Batch_Files_Wafer_23012020_163456.csv
            Training_Batch_Files_Wafer_24012020_150121.csv
            Training_Batch_Files_Wafer_25012020_142112.csv
            Training_Batch_Files_Wafer_fault_detection.csv
            Training_Batch_Files_Wafer_text_130532.csv
            Training_Batch_Files_Waferdefault_15010_130532.csv
            Training_Batch_Files_wafer_07012020_041011.csv
            Training_Batch_Files_wafer_16012020_134553.csv
            Training_Batch_Files_wafer_17012020_125434.csv
            Training_Batch_Files_wafer_20012020_090819.csv
            Training_Batch_Files_wafer_22022020_041119.csv
            Training_Batch_Files_wafer_23012020_011008.csv
            Training_Batch_Files_wafer_28012020_051011.csv
            Training_Batch_Files_wafer_29012020_060756.csv
            Training_Batch_Files_wafer_31012020_090811.csv
        TrainingFileFromDB/
            trainingInput.csv
        TrainingGoodRawDataFolder/
            Training_Batch_Files_wafer_13012020_090817.csv
            Training_Batch_Files_wafer_16012020_051629.csv
            Training_Batch_Files_wafer_20022020_090716.csv
            Training_Batch_Files_wafer_21012020_080913.csv
            Training_Batch_Files_wafer_23012020_041211.csv
            Training_Batch_Files_wafer_27012020_080911.csv
            Training_Batch_Files_wafer_28012020_090817.csv
            Training_Batch_Files_wafer_28042020_031911.csv
            Training_Batch_Files_wafer_29012020_050617.csv
        TrainingLogs/
            Exception.txt
            MainTrainingDataValidationlogs.txt
            TrainingBadRawDataFolder.txt
            TrainingDataValidationlogs.txt
            TrainingGoodRawDataFolder.txt
            TrainingdeleteBadRawDataFolder.txt
            TrainingdeleteGoodRawDataFolder.txt
            clustering.txt
            data_preprocessing.txt
            dbOperation.txt
            getdata.txt
            models_saving_and_loading_logs.txt
            oversamplig.txt
            tainModelLogs.txt
            tuner.txt
            valuesFromSchemaLogs.txt
        TrainingRawDataValidation/
            TrainingRawDataValidation.py
            __pycache__/
                TrainingRawDataValidation.cpython-36.pyc
                TrainingRawDataValidation.cpython-37.pyc
                TrainingRawDataValidation.cpython-38.pyc
        Training_Batch_Files/
            Training_Batch_Files_Wafer12_20012.csv
            Training_Batch_Files_Wafer_07012020_000000.csv
            Training_Batch_Files_Wafer_07012020_223345.csv
            Training_Batch_Files_Wafer_08012020_120000.csv
            Training_Batch_Files_Wafer_10012020_131534.csv
            Training_Batch_Files_Wafer_11012020_151432.csv
            Training_Batch_Files_Wafer_12012020_111.csv
            Training_Batch_Files_Wafer_12012020_111213.csv
            Training_Batch_Files_Wafer_13012020_141000.csv
            Training_Batch_Files_Wafer_14012020_113045.csv
            Training_Batch_Files_Wafer_15010_130532.csv
            Training_Batch_Files_Wafer_15012020_130532.csv
            Training_Batch_Files_Wafer_18012020_121532.csv
            Training_Batch_Files_Wafer_19012020_141432.csv
            Training_Batch_Files_Wafer_20012020_135132.csv
            Training_Batch_Files_Wafer_21012020_143634.csv
            Training_Batch_Files_Wafer_22012020_173245.csv
            Training_Batch_Files_Wafer_23012020_163456.csv
            Training_Batch_Files_Wafer_24012020_150121.csv
            Training_Batch_Files_Wafer_25012020_142112.csv
            Training_Batch_Files_Wafer_fault_detection.csv
            Training_Batch_Files_Wafer_text_130532.csv
            Training_Batch_Files_Waferdefault_15010_130532.csv
            Training_Batch_Files_wafer_07012020_041011.csv
            Training_Batch_Files_wafer_13012020_090817.csv
            Training_Batch_Files_wafer_16012020_051629.csv
            Training_Batch_Files_wafer_16012020_134553.csv
            Training_Batch_Files_wafer_17012020_125434.csv
            Training_Batch_Files_wafer_20012020_090819.csv
            Training_Batch_Files_wafer_20022020_090716.csv
            Training_Batch_Files_wafer_21012020_080913.csv
            Training_Batch_Files_wafer_22022020_041119.csv
            Training_Batch_Files_wafer_23012020_011008.csv
            Training_Batch_Files_wafer_23012020_041211.csv
            Training_Batch_Files_wafer_27012020_080911.csv
            Training_Batch_Files_wafer_28012020_051011.csv
            Training_Batch_Files_wafer_28012020_090817.csv
            Training_Batch_Files_wafer_28042020_031911.csv
            Training_Batch_Files_wafer_29012020_050617.csv
            Training_Batch_Files_wafer_29012020_060756.csv
            Training_Batch_Files_wafer_31012020_090811.csv
        __pycache__/
            PredictionDataValidation.cpython-36.pyc
            TrainingDataValidation.cpython-36.pyc
            TrainingDataValidation.cpython-37.pyc
            TrainingDataValidation.cpython-38.pyc
            main.cpython-36.pyc
            trainModel.cpython-36.pyc
            trainModel.cpython-37.pyc
            trainModel.cpython-38.pyc
        application_loging/
            app_logger.py
            __pycache__/
                app_logger.cpython-36.pyc
                app_logger.cpython-37.pyc
                app_logger.cpython-38.pyc
        load_data/
            getdata.py
            __pycache__/
                getdata.cpython-36.pyc
                getdata.cpython-37.pyc
                getdata.cpython-38.pyc
        model_finder/
            tuner.py
            __pycache__/
                tuner.cpython-36.pyc
                tuner.cpython-37.pyc
        models_operation/
            models_saving_and_loading.py
            __pycache__/
                models_saving_and_loading.cpython-36.pyc
                models_saving_and_loading.cpython-37.pyc
        templates/
            index.html
```
## Libraries
also mentioned in [requirements.txt](https://github.com/IamVicky90/END-TO-END-Wafer-Machiine-Learning-Project-With-MLOPS/blob/main/requirements.txt)
```
APScheduler==3.7.0
argon2-cffi==20.1.0
async-generator==1.10
attrs==20.3.0
backcall==0.2.0
bleach==3.3.0
certifi==2020.12.5
cffi==1.14.5
click==7.1.2
colorhash==1.0.3
configparser==5.0.2
cycler==0.10.0
decorator==5.0.5
defusedxml==0.7.1
entrypoints==0.3
Flask==1.1.2
Flask-Cors==3.0.10
Flask-MonitoringDashboard==3.1.0
greenlet==1.0.0
imbalanced-learn==0.8.0
imblearn==0.0
importlib-metadata==3.10.0
ipykernel==5.5.3
ipython==7.16.1
ipython-genutils==0.2.0
ipywidgets==7.6.3
itsdangerous==1.1.0
jedi==0.17.2
Jinja2==2.11.1
joblib==1.0.1
jsonschema==3.2.0
jupyter==1.0.0
jupyter-client==6.1.13
jupyter-console==6.4.0
jupyter-core==4.7.1
jupyterlab-pygments==0.1.2
jupyterlab-widgets==1.0.0
kiwisolver==1.3.1
kneed==0.7.0
MarkupSafe==1.1.1
matplotlib==3.3.4
mistune==0.8.4
nbclient==0.5.3
nbconvert==6.0.7
nbformat==5.1.3
nest-asyncio==1.5.1
notebook==6.3.0
numpy==1.19.5
packaging==20.9
pandas==1.1.5
pandocfilters==1.4.3
parso==0.7.1
pexpect==4.8.0
pickleshare==0.7.5
Pillow==8.2.0
prometheus-client==0.10.0
prompt-toolkit==3.0.18
psutil==5.8.0
# ptyprocess==0.7.0
gunicorn
pycparser==2.20
Pygments==2.8.1
pyparsing==2.4.7
pyrsistent==0.17.3
python-dateutil==2.8.1
pytz==2021.1
pyzmq==22.0.3
qtconsole==5.0.3
QtPy==1.9.0
scikit-learn==0.24.1
scipy==1.5.4
seaborn==0.11.1
Send2Trash==1.5.0
six==1.15.0
sklearn==0.0
SQLAlchemy==1.4.6
terminado==0.9.4
testpath==0.4.4
threadpoolctl==2.1.0
tornado==6.1
traitlets==4.3.3
typing-extensions==3.7.4.3
tzlocal==2.1
wcwidth==0.2.5
webencodings==0.5.1
Werkzeug==1.0.1
widgetsnbextension==3.5.1
xgboost==1.4.1
zipp==3.4.1
```

