from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PySide6.QtCore import Qt,   QLine
from PySide6.QtGui import QIcon, QFont
import sys


#configuration de l'application
app = QApplication()
window = QWidget()

#app = QApplication()
appIcon = QIcon("Icons//download.jpeg")

#window = QWidget()
window.setWindowTitle("KEDI Download")
window.setWindowIcon(appIcon)
window.setFixedSize(600, 500)


# Create a Label and set its properties
appLabel = QLabel(parent=window)
appLabel.setText("Ajouter le lien de téléchargement")
appLabel.setStyleSheet("QLabel {margin-left: 100% auto; margin-right: 100% auto; padding-top: 50px; }")
appLabel_font = QFont("Poppins", 12)
appLabel.setFont(appLabel_font)


findLabel = QLabel("Find &What:", parent=window   )
#lineEdit = QLineEdit()
#findLabel.setBuddy(lineEdit)
#buttons
 
       
btnAccept = QPushButton("Accepte", parent=window)
btn_font = QFont("Poppins", 12)
btnAccept.setFont(btn_font)
btnAccept.move(180, 230)
btnAccept.setStyleSheet("QPushButton {background-color: #2d3e4e; color: white}")

btnClosed = QPushButton("Closed", parent=window)
btn_font = QFont("Poppins", 12)
btnClosed.setFont(btn_font)
btnClosed.move(270, 230)
btnClosed.setStyleSheet("QPushButton {background-color: white; color:#2d3e4e }")



window.show()
app.exec()