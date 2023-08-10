from PyQt5 import QtCore, QtGui, QtWidgets
import requests as req
from bs4 import BeautifulSoup
import re
from io import BytesIO
from PIL import Image,ImageQt
from urllib.request import urlopen

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 100, 711, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 5, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 530, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 530, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 60, 300, 25))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 60, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(770, 100, 160, 421))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.checkBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox_6)
        self.checkBox_8 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_8)
        self.checkBox_7 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox_7)
        self.checkBox_12 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBox_12)
        self.checkBox_13 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBox_13)
        self.checkBox_9 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkBox_9)
        self.checkBox_11 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.checkBox_11)
        self.checkBox_10 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.checkBox_10)
        self.checkBox_14 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_14.setObjectName("checkBox_14")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.checkBox_14)
        self.checkBox_15 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_15.setObjectName("checkBox_15")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkBox_15)
        self.checkBox_16 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_16.setObjectName("checkBox_16")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.checkBox_16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", ">"))
        self.pushButton_2.setText(_translate("MainWindow", "<"))
        self.label.setText(_translate("MainWindow", "Website:"))
        self.label_2.setText(_translate("MainWindow", "Booru Scraper"))
        self.pushButton_3.setText(_translate("MainWindow", "Search?"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_12.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_13.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_9.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_11.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_10.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_14.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_15.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_16.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton_3.clicked.connect(self.webCheck)


class ScraperApp:
    def __init__(self, master):
        self.entry = None
        self.master = master
        title = tk.Label(self.master, text="Booruu Scraper", font=("Roman", 25)).place(relx=0.05,rely=0.1)
        entryLabel = tk.Label(self.master, text="Website: ").place(relx=0.1,rely=0.2)
        self.entry = tk.Entry(self.master)
        button = tk.Button(self.master, text="Search!",relief=tk.RAISED)
        button.bind("<Button-1>", self.webCheck)
        self.entry.place(relx=0.13,rely=0.2,relwidth=0.5)
        button.place(relx=0.64,rely=0.2)
        

    def webCheck(self,master):
        site = self.lineEdit.text()
        page = req.get(site)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.content = soup.find_all(class_="post-preview-image")
        self.present()

    def present(self):
        imageSRCRegEx = 'src="(.*?)"'
        data = self.content[0]
        print(data)
        datasetter = str(re.findall(imageSRCRegEx, str(self.content[0]))[0])
        print(datasetter)
        image = req.get(datasetter,stream=True)
        img = Image.open(urlopen(datasetter))
        img2 = ImageQt.ImageQt(img)
        pix = QtGui.QPixmap.fromImage(img2)
        self.label_7.setPixmap(pix)
        self.master.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
