from datetime import datetime

class logger:
    """For logging purposes"""
    def __init__(self):
        pass
    def log(self,file,Message):
        self.now=datetime.now()
        self.date=self.now.date()
        self.current_time=self.now.strftime("%H:%M:%S")
        file.write(str(self.date)+"\t\t"+str(self.current_time)+str(Message)+"\n")

