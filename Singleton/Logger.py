from datetime import datetime
class Logger:
    def __init__(self):
        self.name = "logger" + datetime.now().strftime("%Y-%M-%D_%S")
        self.logger = None

    def get_instance(self):
        if(self.logger == None):
            self.logger = Logger()
        return self.logger
    
    def log(self, message):
        print(f"[INFO] {message} from {self.name}")
    

logger1 = Logger()
logger2 = Logger()

logger1.log("message")
# [INFO] message from logger2024-42-03/17/24_59
logger2.log("message")
# [INFO] message from logger2024-42-03/17/24_59
