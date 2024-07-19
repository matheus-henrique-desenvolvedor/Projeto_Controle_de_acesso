import sys
from window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QGridLayout, QLineEdit
from PySide6.QtGui import QImage, QPixmap, QRegularExpressionValidator
from PySide6.QtCore import Slot, QRegularExpression
from entrar import Ui_Dialog
from video import ValidaId
from cpf_validator import ValidaCpf
from cadastro_metodos import Cadastro
     
class Janela(QMainWindow, Ui_MainWindow, QLineEdit):
    def __init__(self, *args,**argvs):
        super(Janela, self).__init__(*args,**argvs)
        self.ui = QGridLayout()
        self.setupUi(self)
        self.setWindowTitle('Controler de acesso ')
        self.vs = ValidaId()
        self.vs.change_pixmap.connect(self.frame_update)
        self.statusBar().showMessage('  Seja bem vindo  ')        
        self.genero1 = "Mulher"
        self.date_str =None
        self.gets_name(), self.individuals(), self.address(), self.fone() 
        self.btRegister.clicked.connect(self.run)# type: ignore
        self.cadastro = Cadastro() 


    def gets_name(self):
        regex = QRegularExpression(r"^[a-zA-Z\s]+$")
        validator = QRegularExpressionValidator(regex, self.lineName)
        self.lineName.setValidator(validator)       
        self.nome = self.lineName.text()
        
   
    def individuals(self):
        regex = QRegularExpression(r"^[0-9]{11}$")
        validator = QRegularExpressionValidator(regex, self.inputCpf)
        self.inputCpf.setValidator(validator)        
        self.cpf = self.inputCpf.text()
        dados = self.cpf
        data = ValidaCpf().run(dados)         
        if data[0] == False:
            print("CPF invalido")
            self.statusBar().showMessage('CPF invalido')
            return False
        else:
            print("CPF valido")
            self.statusBar().showMessage('CPF valido')
            return True
                          

    def birth(self):
        date = self.dateEdit.date()
        self.date_str = date.toString("dd/MM/yyyy")
        self.date_str
    

    def address(self):
        regex = QRegularExpression(r"^[0-9]{8}$")
        validator = QRegularExpressionValidator(regex, self.inputCep)
        self.inputCep.setValidator(validator)  
        self.cep = self.inputCep.text()
        

    def fone(self):
        regex = QRegularExpression(r"^[0-9]{11}$")
        validator = QRegularExpressionValidator(regex, self.inputFone)
        self.inputFone.setValidator(validator)     
        self.telefone = self.inputFone.text()
        

    def sexo(self):        
        if self.radioButton.isChecked():
            self.genero1 = "Homem"             
        else:
            self.genero1 = "Mulher"
            
        return self.genero1
    
        
    def modolos(self):
        self.gets_name()
        self.birth()
        self.individuals()
        self.address()
        self.fone()
        self.sexo()


    def dados_cadastrais(self):        
        dados = {
            "Nome": self.nome,
            "CPF": self.cpf,
            "Data de Nascimento": self.date_str,
            "Endereço": self.cep,
            "Telefone": self.telefone,
            "Gênero": self.genero1
    }
    
        
        result = self.cadastro.run(dados)
              

    def run(self, dados):
        self.modolos()        
        self.dados_cadastrais()
        self.statusBar().showMessage('Cadastro realizado com sucesso ')
                

    @Slot()
    def on_pushButtonValidate_clicked(self):
        if not self.vs.isRunning():
            self.vs.stop=False           
            self.vs.start()
            self.statusBar().showMessage('Apresente o QR em frente a camera')
        else:            
            self.vs.start()
            self.vs.stop=True
            self.statusBar().showMessage('Camera desligada')


    @Slot(QImage)
    def frame_update(self, image):
        self.label_video.setPixmap(QPixmap.fromImage(image))


class ButtonEntrar(QDialog, Ui_MainWindow):
    def __init__(self, *args,**argvs):
        super(ButtonEntrar, self).__init__(*args,**argvs)   
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        self.setWindowTitle('Controler de acesso ')
        self.ui.pushButtonEntrar.clicked.connect(self.entrar)


    def entrar(self):
        self.tela = Janela()
        self.tela.show()
        ButtonEntrar.hide(self)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ButtonEntrar()

    window.show()
    app.exec()
    
