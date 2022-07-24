# importing libraries
from PyQt5.QtWidgets import *
import sys

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Wiki-Summary-Scrapper")
        self.setGeometry(100, 100, 400, 500)
        self.fromGroupBox = QGroupBox("Do your research")
        self.nameLineEdit = QLineEdit()
        self.createForm()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.getInfo)
        self.buttonBox.rejected.connect(self.reject)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.fromGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)
        
    def getInfo(self):
        mainLayout = QVBoxLayout()
        self.button = QPushButton.Download
        mainLayout.addWidget(self.button)
        self.setLayout(mainLayout)