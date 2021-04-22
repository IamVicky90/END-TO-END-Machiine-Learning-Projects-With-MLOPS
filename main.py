from flask import request,Flask,render_template
from wsgiref import simple_server
import flask_monitoringdashboard as dashboard
from flask_cors import CORS,cross_origin
import os
from werkzeug.utils import secure_filename
from TrainingDataValidation import TrainValidation
from PredictionDataValidation import PredictionValidation
from trainModel import modelTraining
app=Flask(__name__)
dashboard.bind(app)
CORS(app)
# Creating Training Folders if not exists
def createNotPresentTrainingDirectories():
    folders=os.listdir(os.getcwd())
    if 'Training_Batch_Files' not in folders:
        os.system("mkdir Training_Batch_Files")
    if 'TrainingLogs' not in folders:
        os.system("mkdir TrainingLogs")
# Creating Prediction Folders if not exists
def createNotPresentPredictionDirectories():
    folders=os.listdir(os.getcwd())

    if 'Prediction_Batch_Files' not in folders:
        os.system("mkdir Prediction_Batch_Files")
    if 'PredictionLogs' not in folders:
        os.system("mkdir PredictionLogs")
def delete_DataBase_Files():
    if 'wafer.db' in os.listdir(os.getcwd()):
        os.system('rm wafer.db')
    if 'pred_wafer.db' in os.listdir(os.getcwd()):
        os.system('rm pred_wafer.db')


@app.route("/",methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/train",methods=["POST"])
@cross_origin()
def train():
    createNotPresentTrainingDirectories()
    delete_DataBase_Files()
    Training_path='Training_Batch_Files'
    files=request.files.getlist("folder")
    for file in files:
        basepath = os.getcwd()
        file_path = os.path.join(
        basepath,Training_path, secure_filename(file.filename))
        file.save(file_path)
    Train_obj=TrainValidation(Training_path)
    Train_obj.TrainValidation()
    model_train=modelTraining()
    model_train.training_data()
    return "Suceccesfull"
@app.route("/predict",methods=["POST"])
@cross_origin()
def predict():
    createNotPresentPredictionDirectories()
    delete_DataBase_Files()
    Prediction_path='Prediction_Batch_Files'
    files=request.files.getlist("folder")
    for file in files:
        basepath = os.getcwd()
        file_path = os.path.join(
        basepath,Prediction_path, secure_filename(file.filename))
        file.save(file_path)
    Pred_obj=PredictionValidation(Prediction_path)
    Pred_obj.PredictionValidation()
    
    
    return "Suceccesfull"



port = int(os.getenv("PORT",5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    #port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()