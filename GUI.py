import sys, os
from datetime import datetime
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout,  QLineEdit, QMessageBox, QComboBox, QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from map import MainMap
from DB_UK import Db


class Example(QMainWindow):
    def __init__(self, *args, **kwargs):

        super(Example, self).__init__(*args, **kwargs)

        self.setMinimumSize(QSize(1900, 1000))
        self.setWindowTitle("Информационно-справочная система военной инфраструктуры Великобритании")
        self.setGeometry(0, 0, 1900, 1000)
        self.setStyleSheet("background-color: rgb(187, 247, 178);")

        self.layout = QGridLayout()
        self.browser = QWebEngineView()
        self.browser.setGeometry(0, 0, 800, 980)

        with open('total_map.html', 'r', encoding="utf8") as f:
            self.start_map = f.read()

        self.browser.setHtml(self.start_map)

        self.setCentralWidget(self.browser)
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

        stylesheet = ("""QPushButton#pushButton {
                                    color: rgb(7, 107, 36);
                                    border-style: outset; 
                                    border-radius: 10px;
                                    font: bold 16px; 
                                    padding: 6px;
                                    color: rgb(255, 255, 255);
                                    border-bottom-width: 4px;
                                    border-right-width: 4px;
                                    border-color: rgb(7, 107, 36) ;     
                                    background-color: green;
                                    }
                                    QPushButton#pushButton:pressed {
                                    border-top-width: 2px;
                                    border-left-width: 2px; 
                                    border-bottom-width: 0px;
                                    border-right-width: 0px;
                                    background-color: green;
                                    border-style: inset;
                                    }""")

        text_box_style = """QTextEdit {color: rgb(7, 107, 36);
                                    background-color: rgb(255, 255, 255);
                                    border-radius: 10px;
                                    border: 4px solid rgb(7, 107, 36);} """
        
        self.qcombobox_box_style = """QComboBox {color: rgb(7, 107, 36);
                                    background-color: rgb(255, 255, 255);
                                    border-radius: 10px;
                                    border: 4px solid rgb(7, 107, 36);} """
        
        # self.bt1 = QPushButton("Выполнить", self)
        # self.bt1.move(1300, 20)
        # self.bt1.setFont(QFont('San Francisco', 16))
        # self.bt1.setFixedSize(170, 50)
        # self.bt1.setObjectName("pushButton")
        # self.bt1.setStyleSheet(stylesheet)
        # self.bt1.clicked.connect(self.Button1)

        self.bt2 = QPushButton("Карта", self)
        self.bt2.move(1565, 20)
        self.bt2.setFont(QFont('San Francisco', 16))
        self.bt2.setFixedSize(170, 50)
        self.bt2.setObjectName("pushButton")
        self.bt2.setStyleSheet(stylesheet)
        self.bt2.clicked.connect(self.Button2)

        self.bt3 = QPushButton("О нас", self)
        self.bt3.move(1750, 20)
        self.bt3.setFont(QFont('San Francisco', 16))
        self.bt3.setFixedSize(130, 50)
        self.bt3.setObjectName("pushButton")
        self.bt3.setStyleSheet(stylesheet)
        self.bt3.clicked.connect(self.Button3)

        self.days_combo = QComboBox(self)
 
        self.days_combo.addItem('Военно-морская база')
        self.days_combo.addItem('Авиационная база')
        self.days_combo.addItem('Военный городок')

        self.days_combo.move(835, 20)
        self.days_combo.resize(300, 50)

        self.days_combo.setFont(QFont('San Francisco', 14))
        self.days_combo.setStyleSheet(self.qcombobox_box_style)
        self.days_combo.activated[str].connect(self.change_list)

        self.db = Db()
        records_vmb = self.db.read_db_vmb()

        self.obj_combo = QComboBox(self)

        for row in records_vmb:
            self.obj_combo.addItem(row[1])

        self.obj_combo.move(1200, 20)
        self.obj_combo.resize(300, 50)
        self.obj_combo.setFont(QFont('San Francisco', 14))
        self.obj_combo.setStyleSheet(self.qcombobox_box_style)
        self.obj_combo.activated[str].connect(self.Button1)

        self.textbox2 = QTextEdit(self)
        self.textbox2.move(835, 150)
        self.textbox2.resize(300, 50)
        self.textbox2.setFont(QFont('San Francisco', 14))
        self.textbox2.setStyleSheet(text_box_style)
        self.textbox2.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox3 = QTextEdit(self)
        self.textbox3.move(1200, 150)
        self.textbox3.resize(300, 50)
        self.textbox3.setFont(QFont('San Francisco', 14))
        self.textbox3.setStyleSheet(text_box_style)
        self.textbox3.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox4 = QTextEdit(self)
        self.textbox4.move(1565, 150)
        self.textbox4.resize(320, 50)
        self.textbox4.setFont(QFont('San Francisco', 14))
        self.textbox4.setStyleSheet(text_box_style)
        self.textbox4.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox5 = QTextEdit(self)
        self.textbox5.move(835, 450)
        self.textbox5.resize(1050, 530)
        self.textbox5.setFont(QFont('San Francisco', 14))
        self.textbox5.setStyleSheet(text_box_style)
        self.textbox5.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox6 = QTextEdit(self)
        self.textbox6.move(835, 250)
        self.textbox6.resize(1050, 150)
        self.textbox6.setFont(QFont('San Francisco', 14))
        self.textbox6.setStyleSheet(text_box_style)
        self.textbox6.setAlignment(QtCore.Qt.AlignCenter)

        self.label1 = QLabel('<b>Широта</b>', self)
        self.label1.setGeometry(835, 100, 300, 50)
        self.label1.setFont(QFont('San Francisco', 16))

        self.label2 = QLabel('<b>Долгота</b>', self)
        self.label2.setGeometry(1200, 100, 300, 50)
        self.label2.setFont(QFont('San Francisco', 16))

        self.label3 = QLabel('<b>Важность</b>', self)
        self.label3.setGeometry(1565, 100, 300, 50)
        self.label3.setFont(QFont('San Francisco', 16))

        self.label4 = QLabel('<b>Подробное описание</b>', self)
        self.label4.setGeometry(835, 400, 300, 50)
        self.label4.setFont(QFont('San Francisco', 16))

        self.label5 = QLabel('<b>Краткое описание</b>', self)
        self.label5.setGeometry(835, 200, 300, 50)
        self.label5.setFont(QFont('San Francisco', 16))
    
    def change_list(self):
        self.obj_combo.clear()
        list_name = self.days_combo.currentText()

        if list_name == 'Военно-морская база':
            records_vmb = self.db.read_db_vmb()
            for row in records_vmb:
                self.obj_combo.addItem(row[1])

        if list_name == 'Авиационная база':
            records_avb = self.db.read_db_avb()
            for row in records_avb:
                self.obj_combo.addItem(row[1])

        if list_name == 'Военный городок':
            records_vg = self.db.read_db_vg()
            for row in records_vg:
                self.obj_combo.addItem(row[1])

    def Button1(self):
        try:
            name = self.obj_combo.currentText()
            obj_type = self.days_combo.currentText()

            db = Db()
            object = db.read_one_note(obj_type, name)

            self.map = MainMap()
            self.map.map_creation(object[2], object[3])

            self.browser.setHtml(self.map.html)

            self.textbox2.setPlainText(str(object[2]))
            self.textbox3.setPlainText(str(object[3]))
            self.textbox4.setPlainText(object[4])
            self.textbox5.setPlainText(object[6])
            self.textbox6.setPlainText(object[5])
            
        except Exception as error:
            print(error)

    def Button2(self):
        self.browser.setHtml(self.start_map)

    def Button3(self):
        os.startfile('AboutUs.png')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Example()
    mainWin.show()
    sys.exit(app.exec_())
