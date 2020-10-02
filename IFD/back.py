# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'back.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os , subprocess, time
from PyQt5.QtCore import  pyqtSlot, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QLineEdit, QFileDialog
from PyQt5.uic import loadUi
from taskthread import *


class Ui_Second(object):
    
    def setupUi(self, Second):
        Second.setObjectName("Second")
        Second.resize(543, 306)
        self.gridLayout = QtWidgets.QGridLayout(Second)
        self.gridLayout.setObjectName("gridLayout")
        self.ligand_value = QtWidgets.QLineEdit(Second)
        self.ligand_value.setObjectName("ligand_value")
        self.gridLayout.addWidget(self.ligand_value, 2, 1, 1, 1)
        self.api_name = QtWidgets.QLabel(Second)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 149, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 56, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 149, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 56, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 149, 175))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 56, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.api_name.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.api_name.setFont(font)
        self.api_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.api_name.setObjectName("api_name")
        self.gridLayout.addWidget(self.api_name, 0, 0, 1, 6)
        self.LigandButton = QtWidgets.QToolButton(Second)
        self.LigandButton.setObjectName("LigandButton")
        self.gridLayout.addWidget(self.LigandButton, 2, 2, 1, 1)
        self.receptor_value = QtWidgets.QLineEdit(Second)
        self.receptor_value.setObjectName("receptor_value")
        self.gridLayout.addWidget(self.receptor_value, 1, 1, 1, 1)
        self.ligand_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ligand_name.setFont(font)
        self.ligand_name.setObjectName("ligand_name")
        self.gridLayout.addWidget(self.ligand_name, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Second)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 6)
        self.OK_button = QtWidgets.QPushButton(Second)
        self.OK_button.setObjectName("OK_button")
        self.gridLayout.addWidget(self.OK_button, 8, 4, 1, 1)
        self.exit2_button = QtWidgets.QPushButton(Second)
        self.exit2_button.setObjectName("exit2_button")
        self.gridLayout.addWidget(self.exit2_button, 8, 5, 1, 1)
        self.ref_ligandButton = QtWidgets.QToolButton(Second)
        self.ref_ligandButton.setObjectName("ref_ligandButton")
        self.gridLayout.addWidget(self.ref_ligandButton, 3, 2, 1, 1)
        self.receptor_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.receptor_name.setFont(font)
        self.receptor_name.setObjectName("receptor_name")
        self.gridLayout.addWidget(self.receptor_name, 1, 0, 1, 1)
        self.ReceptorButton = QtWidgets.QToolButton(Second)
        self.ReceptorButton.setObjectName("ReceptorButton")
        self.gridLayout.addWidget(self.ReceptorButton, 1, 2, 1, 1)
        self.rec_lig_name = QtWidgets.QLabel(Second)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rec_lig_name.setFont(font)
        self.rec_lig_name.setObjectName("rec_lig_name")
        self.gridLayout.addWidget(self.rec_lig_name, 3, 0, 1, 1)
        self.rec_lig_value = QtWidgets.QLineEdit(Second)
        self.rec_lig_value.setObjectName("rec_lig_value")
        self.gridLayout.addWidget(self.rec_lig_value, 3, 1, 1, 1)
        self.no_poses = QtWidgets.QLineEdit(Second)
        self.no_poses.setObjectName("no_poses")
        self.gridLayout.addWidget(self.no_poses, 4, 1, 1, 1)
        self.no_poese_label = QtWidgets.QLabel(Second)
        self.no_poese_label.setObjectName("no_poese_label")
        self.gridLayout.addWidget(self.no_poese_label, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(Second)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Second)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 1)

        self.retranslateUi(Second)
        QtCore.QMetaObject.connectSlotsByName(Second)

    def retranslateUi(self, Second):
        _translate = QtCore.QCoreApplication.translate
        Second.setWindowTitle(_translate("Second", "FitDock"))
        self.api_name.setText(_translate("Second", "               FitDock"))
        self.LigandButton.setText(_translate("Second", "..."))
        self.ligand_name.setText(_translate("Second", "Ligand file:"))
        self.OK_button.setText(_translate("Second", "OK"))
        self.exit2_button.setText(_translate("Second", "Exit"))
        self.ref_ligandButton.setText(_translate("Second", "..."))
        self.receptor_name.setText(_translate("Second", "Receptor file:"))
        self.ReceptorButton.setText(_translate("Second", "..."))
        self.rec_lig_name.setText(_translate("Second", "Reference ligand:"))
        self.no_poese_label.setText(_translate("Second", "Number of poses:"))
        self.label.setText(_translate("Second", "Active receptor chain:"))

        self.ReceptorButton.clicked.connect(self.ReceptorID)
        self.LigandButton.clicked.connect(self.LigandID)
        self.ref_ligandButton.clicked.connect(self.refLigandID)

        self.no_poses.setPlaceholderText('10')

        self.myLongTask = TaskThread() 
        self.myLongTask.taskFinished.connect(self.onFinished)
        

        self.OK_button.clicked.connect(self.OK)
        self.exit2_button.clicked.connect(self.Exit2)

    def ReceptorID(self):
        filename = QFileDialog.getOpenFileName()
        file = filename[0]
        folder, name = os.path.split(file)
        receptor, ext = os.path.splitext(name)
        self.receptor_value.setText(receptor)
        

        with open('parameters.py','a') as p:
            name1 = "receptor ='"
            name2 = "apo ='"
            p.write(name1 + receptor + "'\n")
            p.write(name2 + receptor + "'\n")

    def LigandID(self):
        filename = QFileDialog.getOpenFileName()
        file = filename[0]
        folder, name = os.path.split(file)
        ligand, ext = os.path.splitext(name)
        self.ligand_value.setText(ligand)

        with open('parameters.py','a') as p:
            name = "ligand ='"
            p.write(name + ligand + "'\n")

    def refLigandID(self):
        filename = QFileDialog.getOpenFileName()
        file = filename[0]
        folder, name = os.path.split(file)
        rec_ligand, ext = os.path.splitext(name)
        self.rec_lig_value.setText(rec_ligand)

        with open('parameters.py','a') as p:
            name = "rec_ligand ='"
            p.write(name + rec_ligand + "'\n")


    def OK(self):

        no_poses = self.no_poses.text()
        act_chain = self.lineEdit.text()
        
        with open('parameters.py','a') as p:
            name = "no_poses ='"
            if no_poses == "":
                p.write(name + "10'\n")
            else:
                p.write(name + no_poses + "'\n")
            name2 = "act_chain ='"
            p.write(name2 + act_chain + "'\n")
        

        self.progressBar.setRange(0,0) 
        self.myLongTask.start()
        
    def onFinished(self): 
        self.progressBar.setRange(0,1)
             

    def Exit2(self):
        Second = QtWidgets.QWidget()
        Second.close()
        exit(subprocess.run(["python3","0_RUN.py"]))
        
class TaskThread(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()
    def run(self):
        time.sleep(3)
        subprocess.run(["python3","0_RUN.py"])
        self.taskFinished.emit()  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Second = QtWidgets.QWidget()
    ui = Ui_Second()
    ui.setupUi(Second)
    Second.show()
    sys.exit(app.exec_())
