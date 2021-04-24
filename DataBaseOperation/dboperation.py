import sqlite3
import os
import sys
from application_loging import app_logger
import csv
import shutil
class dbOperation:
    def __init__(self,logFile):
        self.logger=app_logger.logger()
        self.file=open(f'{logFile}/dbOperation.txt','a+')
        self.exceptionfile=open(f'{logFile}/Exception.txt','a+')
    def connectionEstablished(self,dbConnectionName):
        try:
            con = sqlite3.connect(dbConnectionName)
            self.logger.log(self.file,'\tSuccessfully Established the DataBase Connection')
        except Exception as e:
            self.logger.log(self.file,"\tCouldn't  Established the DataBase Connection due to error: "+str(e))
            self.logger.log(self.exceptionfile,"\tCouldn't  Established the DataBase Connection due to error: "+str(e))
        return con
    def createTable(self,TableName,colNames,dbname):


        try:
            conn=self.connectionEstablished(dbname)
            c=conn.cursor()
            c.execute(f"SELECT count(name)  FROM sqlite_master WHERE type = 'table'AND name = '{TableName}'")
            if c.fetchone()[0] ==1:
                conn.close()
                self.logger.log(self.file, "\tTables created successfully!!")
                # self.file.close()

                self.logger.log(self.file, f"\tClosed {dbname} database successfully" )
                # self.file.close()
            else:
                for key in colNames.keys():
                    
                    Dtype=colNames[key]
                    try:
                        # cur = con.cursor()
                        c.execute(f'ALTER TABLE {TableName} ADD COLUMN  "{key}" {Dtype}')
                        
                    except:
                        # cur = con.cursor()
                        c.execute(f'CREATE TABLE {TableName} ({key} {Dtype})')
                conn.close()
            
                
            self.logger.log(self.file,"\tTable Created Successfully")
        except Exception as e:
                self.logger.log(self.file,"\tCouldn't  Create The Table! due to an error: "+str(e))
                self.logger.log(self.exceptionfile,"\tCouldn't  Create The Table! due to an error: "+str(e))
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                
    def insertValuesintoTable(self,TableName,dbname,GoodRawDataFolderName):
            GoodDataPath=GoodRawDataFolderName
            conn=self.connectionEstablished(dbname)
            onlyfiles=[f for f in os.listdir(GoodDataPath)]
            for file in onlyfiles:
                try:
                    with open(GoodDataPath+'/'+file, "r") as f:
                        next(f)
                        reader = csv.reader(f, delimiter="\n")
                        for line in enumerate(reader):
                            for list_ in (line[1]):
                                try:
                                    conn.execute(f'INSERT INTO {TableName} values ({list_})')
                                    conn.commit()
                                except Exception as e:
                                    raise e
                    self.logger.log(self.file,"\t%s: File loaded successfully!!" % file)
                                
                except Exception as e:
                    conn.rollback()
                    self.logger.log(self.file,"\tCouldn't  insert value into table! due to an error: "+str(e))
            conn.close()
    def inputvaluesintocsv(self,TableName,dbname,foldername,filename):
        '''Take the data from Data Base and insert it into a csv file'''
        try:
            conn=self.connectionEstablished(dbname)
            c=conn.cursor()
            c.execute(f"SELECT * FROM {TableName}")
            table = c.fetchall()
            headers=[i[0] for i in c.description]
            dirname=foldername
            if os.path.isdir(dirname):
                shutil.rmtree(dirname)
            os.mkdir(dirname)
            
            csvFile=csv.writer(open(dirname+'/'+filename,'w',newline=''),delimiter=',',lineterminator='\r\n',quoting=csv.QUOTE_ALL, escapechar='\\')
            csvFile.writerow(headers)
            csvFile.writerows(table)
            self.logger.log(self.file,f"\t'{filename}' file Loaded Successfully")
            self.file.close()
        except Exception as e:
            self.logger.log(self.exceptionfile,f"\tColudn't loaded '{filename}' error is: "+str(e))
            self.exceptionfile.close()
            self.file.close()
            raise e
        





                    

            
        


            

