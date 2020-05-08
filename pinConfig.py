# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pinConfig.ui'
##
## Original file created by: Qt User Interface Compiler version 5.14.0
##
##  Authors:
##    - Bassem Ezzat
##    - Mariam El-Shakafi
##
##  Version:  1.0
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(645, 851)
        font = QFont()
        font.setPointSize(11)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.selectGroup = QGroupBox(Form)
        self.selectGroup.setObjectName(u"selectGroup")
        self.selectGroup.setGeometry(QRect(20, 30, 601, 131))
        self.selectGroup.setFont(font)
        self.portLabel = QLabel(self.selectGroup)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setGeometry(QRect(20, 40, 56, 16))
        self.portLabel.setFont(font)
        self.portCombo = QComboBox(self.selectGroup)
        self.portCombo.addItem("PORTA")
        self.portCombo.addItem("PORTB")
        self.portCombo.addItem("PORTC")
        self.portCombo.addItem("PORTD")
        self.portCombo.setObjectName(u"portCombo")
        self.portCombo.setGeometry(QRect(20, 70, 211, 31))
        self.portCombo.setFont(font)
        self.pinLabel = QLabel(self.selectGroup)
        self.pinLabel.setObjectName(u"pinLabel")
        self.pinLabel.setGeometry(QRect(370, 40, 56, 16))
        self.pinLabel.setFont(font)
        self.pinCombo = QComboBox(self.selectGroup)
        self.pinCombo.addItem("PIN0")
        self.pinCombo.addItem("PIN1")
        self.pinCombo.addItem("PIN2")
        self.pinCombo.addItem("PIN3")
        self.pinCombo.addItem("PIN4")
        self.pinCombo.addItem("PIN5")
        self.pinCombo.addItem("PIN6")
        self.pinCombo.addItem("PIN7")
        self.pinCombo.setObjectName(u"pinCombo")
        self.pinCombo.setGeometry(QRect(370, 70, 131, 31))
        self.pinCombo.setFont(font)
        self.modeGroup = QGroupBox(Form)
        self.modeGroup.setObjectName(u"modeGroup")
        self.modeGroup.setGeometry(QRect(20, 180, 271, 221))
        self.modeGroup.setFont(font)
        self.inputRadioBtn = QRadioButton(self.modeGroup)
        self.inputRadioBtn.setObjectName(u"inputRadioBtn")
        self.inputRadioBtn.setGeometry(QRect(20, 60, 97, 21))
        self.inputRadioBtn.setFont(font)
        self.inputRadioBtn.setChecked(True)
        self.outputRadioBtn = QRadioButton(self.modeGroup)
        self.outputRadioBtn.setObjectName(u"outputRadioBtn")
        self.outputRadioBtn.setGeometry(QRect(20, 160, 97, 20))
        self.outputRadioBtn.setFont(font)
        self.inConfigGroup = QGroupBox(Form)
        self.inConfigGroup.setObjectName(u"inConfigGroup")
        self.inConfigGroup.setGeometry(QRect(320, 180, 301, 101))
        self.inConfigGroup.setFont(font)
        self.pullRadioBtn = QRadioButton(self.inConfigGroup)
        self.pullRadioBtn.setObjectName(u"pullRadioBtn")
        self.pullRadioBtn.setGeometry(QRect(30, 30, 97, 31))
        self.pullRadioBtn.setFont(font)
        self.pullRadioBtn.setChecked(True)
        self.floatRadioBtn = QRadioButton(self.inConfigGroup)
        self.floatRadioBtn.setObjectName(u"floatRadioBtn")
        self.floatRadioBtn.setGeometry(QRect(30, 60, 160, 31))
        self.floatRadioBtn.setFont(font)
        self.outLevelGroup = QGroupBox(Form)
        self.outLevelGroup.setObjectName(u"outLevelGroup")
        self.outLevelGroup.setGeometry(QRect(320, 300, 301, 101))
        self.outLevelGroup.setFont(font)
        self.outLevelGroup.setDisabled(True)
        self.highRadioBtn = QRadioButton(self.outLevelGroup)
        self.highRadioBtn.setObjectName(u"highRadioBtn")
        self.highRadioBtn.setGeometry(QRect(30, 30, 97, 31))
        self.highRadioBtn.setFont(font)
        self.lowRadioBtn = QRadioButton(self.outLevelGroup)
        self.lowRadioBtn.setObjectName(u"lowRadioBtn")
        self.lowRadioBtn.setGeometry(QRect(30, 70, 97, 20))
        self.lowRadioBtn.setFont(font)
        self.lowRadioBtn.setChecked(True)
        self.fileGenGroup = QGroupBox(Form)
        self.fileGenGroup.setObjectName(u"fileGenGroup")
        self.fileGenGroup.setGeometry(QRect(20, 430, 601, 181))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50);
        self.fileGenGroup.setFont(font1)
        self.pathEdit = QLineEdit(self.fileGenGroup)
        self.pathEdit.setObjectName(u"pathEdit")
        self.pathEdit.setGeometry(QRect(30, 60, 541, 41))
        self.pathEdit.setFont(font1)
        self.pathLabel = QLabel(self.fileGenGroup)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setGeometry(QRect(30, 30, 61, 21))
        self.pathLabel.setFont(font1)
        self.genBtn = QPushButton(self.fileGenGroup)
        self.genBtn.setObjectName(u"genBtn")
        self.genBtn.setGeometry(QRect(420, 110, 151, 41))
        self.genBtn.setFont(font1)
        self.genBtn.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.configGenGroup = QGroupBox(Form)
        self.configGenGroup.setObjectName(u"configGenGroup")
        self.configGenGroup.setGeometry(QRect(20, 640, 601, 181))
        self.configGenGroup.setFont(font1)
        self.configNameEdit = QLineEdit(self.configGenGroup)
        self.configNameEdit.setObjectName(u"configNameEdit")
        self.configNameEdit.setGeometry(QRect(30, 70, 541, 41))
        self.configNameEdit.setFont(font1)
        self.configNameLbl = QLabel(self.configGenGroup)
        self.configNameLbl.setObjectName(u"configNameLbl")
        self.configNameLbl.setGeometry(QRect(30, 30, 211, 31))
        self.configNameLbl.setFont(font1)
        self.loadBtn = QPushButton(self.configGenGroup)
        self.loadBtn.setObjectName(u"loadBtn")
        self.loadBtn.setGeometry(QRect(380, 130, 91, 41))
        self.loadBtn.setFont(font1)
        self.loadBtn.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.saveBtn = QPushButton(self.configGenGroup)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(480, 130, 91, 41))
        self.saveBtn.setFont(font1)
        self.saveBtn.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.newBtn = QPushButton(self.configGenGroup)
        self.newBtn.setObjectName(u"newBtn")
        self.newBtn.setGeometry(QRect(30, 130, 91, 41))
        self.newBtn.setFont(font1)
        self.newBtn.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.retranslateUi(Form)
        
        QObject.connect(self.outputRadioBtn, SIGNAL("clicked(bool)"), self.inConfigGroup.setDisabled )
        QObject.connect(self.inputRadioBtn, SIGNAL("clicked(bool)"), self.outLevelGroup.setDisabled )
        QObject.connect(self.outputRadioBtn, SIGNAL("clicked(bool)"), self.outLevelGroup.setEnabled )
        QObject.connect(self.inputRadioBtn, SIGNAL("clicked(bool)"), self.inConfigGroup.setEnabled )
        self.genBtn.clicked.connect(self.genBtnHandle)
        self.saveBtn.clicked.connect(self.saveBtnHandle)
        self.loadBtn.clicked.connect(self.loadBtnHandle)
        self.newBtn.clicked.connect(self.newBtnHandle)
        self.portCombo.highlighted.connect(self.updateDic)
        self.pinCombo.highlighted.connect(self.updateDic)
        self.portCombo.currentIndexChanged.connect(self.updateHandle)
        self.pinCombo.currentIndexChanged.connect(self.updateHandle)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AVR Pin Configurator", None))
        self.selectGroup.setTitle(QCoreApplication.translate("Form", u"Selection", None))
        self.portLabel.setText(QCoreApplication.translate("Form", u"Port", None))
        self.portCombo.setItemText(0, QCoreApplication.translate("Form", u"PORTA", None))
        self.portCombo.setItemText(1, QCoreApplication.translate("Form", u"PORTB", None))
        self.portCombo.setItemText(2, QCoreApplication.translate("Form", u"PORTC", None))
        self.portCombo.setItemText(3, QCoreApplication.translate("Form", u"PORTD", None))

        self.pinLabel.setText(QCoreApplication.translate("Form", u"Pin", None))
        self.pinCombo.setItemText(0, QCoreApplication.translate("Form", u"PIN0", None))
        self.pinCombo.setItemText(1, QCoreApplication.translate("Form", u"PIN1", None))
        self.pinCombo.setItemText(2, QCoreApplication.translate("Form", u"PIN2", None))
        self.pinCombo.setItemText(3, QCoreApplication.translate("Form", u"PIN3", None))
        self.pinCombo.setItemText(4, QCoreApplication.translate("Form", u"PIN4", None))
        self.pinCombo.setItemText(5, QCoreApplication.translate("Form", u"PIN5", None))
        self.pinCombo.setItemText(6, QCoreApplication.translate("Form", u"PIN6", None))
        self.pinCombo.setItemText(7, QCoreApplication.translate("Form", u"PIN7", None))

        self.modeGroup.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.inputRadioBtn.setText(QCoreApplication.translate("Form", u"Input", None))
        self.outputRadioBtn.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inConfigGroup.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pullRadioBtn.setText(QCoreApplication.translate("Form", u"Pull-Up", None))
        self.floatRadioBtn.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.outLevelGroup.setTitle(QCoreApplication.translate("Form", u"Output Level", None))
        self.highRadioBtn.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowRadioBtn.setText(QCoreApplication.translate("Form", u"Low", None))
        self.fileGenGroup.setTitle(QCoreApplication.translate("Form", u"Code File Generation", None))
        self.pathLabel.setText(QCoreApplication.translate("Form", u"Path", None))
        self.genBtn.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.configGenGroup.setTitle(QCoreApplication.translate("Form", u"Configuration Save Utility", None))
        self.configNameLbl.setText(QCoreApplication.translate("Form", u"Configuration File Name", None))
        self.loadBtn.setText(QCoreApplication.translate("Form", u"Load", None))
        self.saveBtn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.newBtn.setText(QCoreApplication.translate("Form", u"New", None))
    # retranslateUi
    
    """
    This is the callback function of the "Generate" button, which generates DIO_config.h file
    """
    def genBtnHandle(self):
      self.updateDic()
      if self.pathEdit.text() != '':
        DIO_H_Handler = open(self.pathEdit.text() + '\DIO.h', 'w')
        DIO_Handler = open(self.pathEdit.text() + '\DIO_config.h', 'w')
      else:
        DIO_Handler = open('DIO_config.h', 'w')
        DIO_H_Handler = open('DIO.h', 'w')
      
      DIO_H_Handler.write("#ifndef DIO_H\n")
      DIO_H_Handler.write("#define DIO_H\n\n\n")
      DIO_H_Handler.write("#define DIO_IN                   0\n")
      DIO_H_Handler.write("#define DIO_OUT                  1\n\n")
      DIO_H_Handler.write("#define DIO_PULL_UP              1\n")
      DIO_H_Handler.write("#define DIO_HIGH_IMPEDANCE       0\n\n")
      DIO_H_Handler.write("#define DIO_HIGH                 1\n")
      DIO_H_Handler.write("#define DIO_LOW                  0\n\n")
      DIO_H_Handler.write("#endif\n")
      DIO_H_Handler.close()
      
      DIO_Handler.write("#ifndef DIO_CFG_H\n")
      DIO_Handler.write("#define DIO_CFG_H\n\n\n")
      for port in PortDic:
        for pin in PortDic[port][1]:
          if PortDic[port][1][pin].strip() == "DIO_HIGH" or PortDic[port][1][pin].strip() == "DIO_LOW":
            DIO_Handler.write('#define DIO_'+PortDic[port][0]+'_'+pin+'      '+"DIO_OUT\n")
          else:
            DIO_Handler.write('#define DIO_'+PortDic[port][0]+'_'+pin+'      '+"DIO_IN\n")
      
      DIO_Handler.write('\n\n\n')
      
      for port in PortDic:
        for pin in PortDic[port][1]:
            DIO_Handler.write('#define DIO_'+port+'_'+pin+'     '+PortDic[port][1][pin])
      
      DIO_Handler.write("\n\n#endif\n")
      DIO_Handler.close()
      return
    
    
    """
    This is the callback function of the "New" button, which resets pin states to default
    """
    def newBtnHandle(self):
      self.configNameEdit.setText('')
      for port in PortDic:
        for pin in PortDic[port][1]:
          PortDic[port][1][pin] = "DIO_PULL_UP\n"
      self.updateHandle()
      return

    """
    This is the callback function of the "Save" button, which saves configurations to be loaded any time
    """
    def saveBtnHandle(self):
      self.updateDic()
      if self.configNameEdit.text() != '':
        ConfigFileName = self.configNameEdit.text()
      else:
        ConfigFileName = 'DefaultConfig.txt'
      SaveFile = open(ConfigFileName, 'w')
      for port in PortDic:
        for pin in PortDic[port][1]:
          SaveFile.write(port + ' ' + pin + ' ' + PortDic[port][1][pin])
      SaveFile.close()
      return

    """
    This is the callback function of the "Load" button, which loads any configurations saved by Save button
    """
    def loadBtnHandle(self):
      if self.configNameEdit.text() != '':
        ConfigFileName = self.configNameEdit.text()
      else:
        return
      LoadFile = open(ConfigFileName, 'r')
      for line in LoadFile:
        configList = line.split()
        PortDic[configList[0]][1][configList[1]] = configList[2]
      self.updateHandle()
      LoadFile.close()
      return
      
    
    """
    This function updates GUI according to the configuration chosen to the pin
    """
    def updateHandle(self):
      if (PortDic[self.portCombo.currentText()][1][self.pinCombo.currentText()].strip() == "DIO_HIGH"):
        self.outputRadioBtn.setChecked(True)
        self.inConfigGroup.setDisabled(True)
        self.outLevelGroup.setEnabled(True)
        self.highRadioBtn.setChecked(True)
      
      elif (PortDic[self.portCombo.currentText()][1][self.pinCombo.currentText()].strip() == "DIO_LOW"):
        self.outputRadioBtn.setChecked(True)
        self.inConfigGroup.setDisabled(True)
        self.outLevelGroup.setEnabled(True)
        self.lowRadioBtn.setChecked(True)
        
      elif (PortDic[self.portCombo.currentText()][1][self.pinCombo.currentText()].strip() == "DIO_HIGH_IMPEDANCE"):
        self.inputRadioBtn.setChecked(True)
        self.inConfigGroup.setEnabled(True)
        self.outLevelGroup.setDisabled(True)
        self.floatRadioBtn.setChecked(True)
      
      else:
        self.inputRadioBtn.setChecked(True)
        self.inConfigGroup.setEnabled(True)
        self.outLevelGroup.setDisabled(True)
        self.pullRadioBtn.setChecked(True)
      return

    """
    This function updates the dictionary of the pins according to the GUI changes
    """
    def updateDic(self): 
      if self.outputRadioBtn.isChecked():
        if self.highRadioBtn.isChecked():
          PortDic[self.portCombo.currentText()][1][self.pinCombo.currentText()] = "DIO_HIGH\n"
        else:
          PortDic[self.portCombo.currentText()][1][self.pinCombo.currentText()] = "DIO_LOW\n"

      else:
        if self.pullRadioBtn.isChecked():
          PortDic[self.portCombo.currentText()][1][self.pinCombo.currentText()] = "DIO_PULL_UP\n"
        else:
          PortDic[self.portCombo.currentText()][1][self.pinCombo.currentText()] = "DIO_HIGH_IMPEDANCE\n"
      return


#Dictionaries that save pin values
PORTA={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTB={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTC={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTD={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PortDic = {"PORTA": ["DDRA", PORTA], "PORTB": ["DDRB", PORTB], "PORTC": ["DDRC", PORTC], "PORTD": ["DDRD", PORTD]}

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())