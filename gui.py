# importing libraries
from PyQt5.QtWidgets import *
import sys

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Wiki-Summary-Scrapper")
        self.setGeometry(100, 100, 200, 300)
        self.fromGroupBox = QGroupBox("Do your research")
        self.nameLineEdit = QLineEdit()
        self.createForm()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.getInfo)
        self.buttonBox.rejected.connect(self.reject)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.fromGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.layout = mainLayout
        self.setLayout(mainLayout)
        
    def getInfo(self):
        if self.nameLineEdit.text() == "":
            message = QMessageBox()
            message.setText("You need to enter a subject.")
            message.exec_()
            
        else:
            button = QPushButton('Download summary', self)
            button.move(50, 300)
            self.text = self.nameLineEdit.text()
            self.layout.removeWidget(self.buttonBox)
            self.buttonBox.deleteLater()
            self.buttonBox = None
            self.layout.removeWidget(self.fromGroupBox)
            self.fromGroupBox.deleteLater()
            self.fromGroupBox = None
            button.clicked.connect(self.download)
            self.layout.addWidget(button)
            
    def download(self):
        print(self.text)
        return True
    
    def createForm(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Subject"), self.nameLineEdit)
        self.fromGroupBox.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())