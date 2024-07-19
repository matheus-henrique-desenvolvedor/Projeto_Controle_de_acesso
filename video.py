import cv2
from PySide6.QtGui import QImage
from PySide6.QtCore import Signal, QThread
import cv2
from time import sleep 
import pandas as pd 
from datetime import datetime

class ValidaId(QThread):
    def __init__(self):  
        super(ValidaId, self).__init__()      
        self.path_database = "C:\\Users\\Mathusa\\Desktop\\Controle de acesso\\dataset.xlsx"
        self.path_final_file = "C:\\Users\\Mathusa\\Desktop\\Controle de acesso\\Access control.xlsx"
        self.today = datetime.today()
        self.stop = False
        self.data = None
    change_pixmap = Signal(QImage)
   
   
    def __read_qrcod(self):
        cap = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while cap.isOpened(): 
            ret, frame=cap.read()           
            if not ret:
                print("sem frame")
                cap.release()
                break
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            convertToQtFormat = QImage(frame, w, h, ch*w, QImage.Format_RGB888)
            self.change_pixmap.emit(convertToQtFormat)
            data,one, frame = detector.detectAndDecode(frame) 
            if data:
                self.data = data
                print(data)
                break
            if self.stop:
                cap.release()
                self.data = None
                self.today = datetime.today()
                break
    

    def database_validation(self):
        credential = self.data
        df = pd.read_excel(self.path_database, dtype=str)

        for index, x in df.iterrows():
            if x["id"] == str(credential): 
                person = x
        print(person)
        return person
        
    
    def set_data(self):
        df = pd.read_excel(self.path_final_file)
        validation = self.database_validation()
        
        self.nova_linha = pd.DataFrame({
            "ID":[validation["id"]],
            "Aluno":[validation["nome"]],
            "Data": [self.today.strftime("%d/%m/%Y")],
            "HORA": [self.today.strftime("%H:%M:%S")]
            })
        
        df = pd.concat([df, self.nova_linha], ignore_index=True)       
        df.to_excel(self.path_final_file, index=False)
        print(df)
    
            
    def run(self):
        self.__read_qrcod()
        self.set_data()
        self.cv=ValidaId()
        self.cv.start()
        