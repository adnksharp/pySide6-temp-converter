import pyperclip as xclip
from notifypy import Notify as noty
import sys

from PySide6.QtWidgets import QApplication, QWidget

from ui_form import Ui_Widget

#modes
# C     0
# F     1
# K     2
# R     3
# N     4
# Ro    5
# Re    6
# De    7

def getTemp(t, mode):
    temps = [ 0 for _ in range(8)]
    match mode:
        case 0:
            temps[0] = t
            temps[1] = (t * 9 / 5) + 32
            temps[2] = t + 273.15
            temps[3] = (t * 9 / 5) + 491.67
            temps[4] = t * 33 / 100
            temps[5] = (t * 21 / 40) + 7.5
            temps[6] = t * 4 / 5
            temps[7] = (100 - t) * 3 / 2
        case 1:
            temps[0] = (t - 32) * 5 / 9
            temps[1] = t
            temps[2] = (t + 459.67) * 5 / 9
            temps[3] = t + 459.67
            temps[4] = (t - 32) * 11 / 60
            temps[5] = (t - 32) * 7 / 24 + 7.5
            temps[6] = (t - 32) * 4 / 9
            temps[7] = (212 - t) * 5 / 6
        case 2:
            temps[0] = t - 273.15
            temps[1] = (t * 9 / 5) - 459.67
            temps[2] = t
            temps[3] = t * 9 / 5 
            temps[4] = (t - 273.15) * 33 / 100
            temps[5] = (t - 273.15) * 21 / 40 + 7.5
            temps[6] = (t - 273.15) * 4 / 5
            temps[7] = (373.15 - t) * 3 / 2
        case 3:
            temps[0] = (t - 491.67) * 5 / 9
            temps[1] = t - 459.67
            temps[2] = t * 5 / 9
            temps[3] = t
            temps[4] = (t - 491.67) * 11 / 60
            temps[5] = (t - 491.67) * 7 / 24 + 7.5
            temps[6] = (t - 491.67) * 4 / 9
            temps[7] = (671.67 - t) * 5 / 6
        case 4:
            temps[0] = t * 100 / 33
            temps[1] = (t * 60 / 11) + 32
            temps[2] = (t * 100 / 33) + 273.15
            temps[3] = (t * 60 / 11) + 491.67
            temps[4] = t
            temps[5] = (t * 35 / 22) + 7.5
            temps[6] = t * 80 / 33
            temps[7] = (33 - t) * 50 / 11
        case 5:
            temps[0] = (t - 7.5) * 40 / 21
            temps[1] = ((t - 7.5) * 24 / 7) + 32
            temps[2] = ((t - 7.5) * 40 / 21) + 273.15
            temps[3] = ((t - 7.5) * 24 / 7) + 491.67
            temps[4] = (t - 7.5) * 22 / 35
            temps[5] = t
            temps[6] = (t - 7.5) * 32 / 21
            temps[7] = (60 - t) * 20 / 7
        case 6:
            temps[0] = t * 5 / 4
            temps[1] = (t * 9 / 4) + 32
            temps[2] = (t * 5 / 4) + 273.15
            temps[3] = (t * 9 / 4) + 491.67
            temps[4] = t * 33 / 80
            temps[5] = (t * 21 / 32) + 7.5
            temps[6] = t
            temps[7] = (80 - t) * 15 / 8
        case 7:
            temps[0] = (100 - t) * 2 / 3
            temps[1] = (212 - t) * 6 / 5
            temps[2] = (373.15 - t) * 2 / 3
            temps[3] = (671.67 - t) * 6 / 5
            temps[4] = (33 - t) * 11 / 50
            temps[5] = (60 - t) * 7 / 20
            temps[6] = (80 - t) * 8 / 15
            temps[7] = t
        case _:
            return [0 for _ in range(8)]
    
    return temps
            
    

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.noty = noty()
        self.noty.title = 'Temperatura copiada'
        
        self.temps = [0 for _ in range(8)]
        self.ui.comboBox.setCurrentIndex(-1)
        
        self.ui.lineEdit.textChanged.connect(self.updateUI)
        self.ui.comboBox.currentIndexChanged.connect(self.updateUI)
        self.ui.pushButton.clicked.connect(lambda x: self.copyTemp(0))
        self.ui.pushButton_2.clicked.connect(lambda x: self.copyTemp(1))
        self.ui.pushButton_3.clicked.connect(lambda x: self.copyTemp(2))
        self.ui.pushButton_4.clicked.connect(lambda x: self.copyTemp(3))
        self.ui.pushButton_5.clicked.connect(lambda x: self.copyTemp(4))
        self.ui.pushButton_6.clicked.connect(lambda x: self.copyTemp(5))
        self.ui.pushButton_7.clicked.connect(lambda x: self.copyTemp(6))
        self.ui.pushButton_8.clicked.connect(lambda x: self.copyTemp(7))
    
    def copyTemp(self, *args):
        if 0 <= args[0] <= 8:
            temp = str(self.temps[args[0]])
            match args[0]:
                case 0:
                    temp += '°C'
                case 1:
                    temp += '°F'
                case 2:
                    temp += 'K'
                case 3:
                    temp += 'R'
                case 4:
                    temp += '°N'
                case 5:
                    temp += '°Rø'
                case 6:
                    temp += '°Re'
                case 7:
                    temp += '°De'
            self.noty.message = temp
            xclip.paste()
            self.noty.send()
            
    def updateUI(self):
        try:
            self.temps = getTemp(float(self.ui.lineEdit.text()), self.ui.comboBox.currentIndex())
        except:
            pass
        self.ui.labelC.setText(str(round(self.temps[0], 2)))
        self.ui.labelF.setText(str(round(self.temps[1], 2)))
        self.ui.labelK.setText(str(round(self.temps[2], 2)))
        self.ui.labelR.setText(str(round(self.temps[3], 2)))
        self.ui.labelN.setText(str(round(self.temps[4], 2)))
        self.ui.labelRo.setText(str(round(self.temps[5], 2)))
        self.ui.labelRe.setText(str(round(self.temps[6], 2)))
        self.ui.labelDe.setText(str(round(self.temps[7], 2)))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
