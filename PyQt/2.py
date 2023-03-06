import sys


from PyQt6.QtWidgets import *


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def button_equals_was_cliced(self):
            self.lable.setText(str(int(self.temp)+int(self.lable.text())))

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(500,500,500,500)

        self.lable=QLineEdit(self)
        self.lable.setGeometry(50,330,300,60)


        self.button_1 = QPushButton("9",self)
        self.button_1.setGeometry(300,180,60,60)
        self.button_1.clicked.connect(self.button_9_was_cliced)



        self.button_7 = QPushButton("8",self)
        self.button_7.setGeometry(300,100,60,60)
        self.button_7.clicked.connect(self.button_8_was_cliced)

        self.button_8 = QPushButton("7",self)
        self.button_8.setGeometry(300,30,60,60)
        self.button_8.clicked.connect(self.button_7_was_cliced)

        self.button_9 = QPushButton("6",self)
        self.button_9.setGeometry(200,180,60,60)
        self.button_9.clicked.connect(self.button_6_was_cliced)

        self.button_15 = QPushButton("0",self)
        self.button_15.setGeometry(200,260,60,60)
        self.button_15.clicked.connect(self.button_0_was_cliced)

        self.button_10 = QPushButton("5",self)
        self.button_10.setGeometry(200,100,60,60)
        self.button_10.clicked.connect(self.button_5_was_cliced)

        self.button_11 = QPushButton("4",self)
        self.button_11.setGeometry(200,30,60,60)
        self.button_11.clicked.connect(self.button_4_was_cliced)

        self.button_12 = QPushButton("1",self)
        self.button_12.setGeometry(100,30,60,60)
        self.button_12.clicked.connect(self.button_1_was_cliced)

        self.button_13 = QPushButton("2",self)
        self.button_13.setGeometry(100,100,60,60)
        self.button_13.clicked.connect(self.button_2_was_cliced)

        self.button_14 = QPushButton("3",self)
        self.button_14.setGeometry(100,180,60,60)
        self.button_14.clicked.connect(self.button_3_was_cliced)

        self.button_5 = QPushButton("/",self)
        self.button_5.setGeometry(400,270,60,60)
        self.button_5.clicked.connect(self.button_dev_was_cliced)


        self.button_2 = QPushButton("*",self)
        self.button_2.setGeometry(400,180,60,60)
        self.button_2.clicked.connect(self.button_mult_was_cliced)

        self.button_3 = QPushButton("+",self)
        self.button_3.setGeometry(400,100,60,60)
        self.button_3.clicked.connect(self.button_plus_was_cliced)

        self.button_4 = QPushButton("-",self)
        self.button_4.setGeometry(400,30,60,60)
        self.button_4.clicked.connect(self.button_minus_was_cliced)

        self.button_6 = QPushButton("=",self)
        self.button_6.setGeometry(400,350,60,60)
        self.button_6.clicked.connect(self.button_equal_was_cliced)

    def button_9_was_cliced(self):
        self.lable.setText(self.lable.text() + '9')

    def button_8_was_cliced(self):
        self.lable.setText(self.lable.text() + '8')

    def button_7_was_cliced(self):
        self.lable.setText(self.lable.text() + '7')

    def button_6_was_cliced(self):
        self.lable.setText(self.lable.text() + '6')

    def button_5_was_cliced(self):
        self.lable.setText(self.lable.text() + '5')

    def button_4_was_cliced(self):
        self.lable.setText(self.lable.text() + '4')

    def button_3_was_cliced(self):
        self.lable.setText(self.lable.text() + '3')

    def button_2_was_cliced(self):
        self.lable.setText(self.lable.text() + '2')

    def button_1_was_cliced(self):
        self.lable.setText(self.lable.text() + '1')

    def button_0_was_cliced(self):
        self.lable.setText(self.lable.text() + '0')

    def button_equal_was_cliced(self):
        self.lable.setText(self.lable.text() + '=')

    def button_minus_was_cliced(self):
        self.lable.setText(self.lable.text() + '-')

    def button_plus_was_cliced(self):
        self.lable.setText(self.lable.text() + '+')

    def button_mult_was_cliced(self):
        self.lable.setText(self.lable.text() + '*')

    def button_dev_was_cliced(self):
        self.lable.setText(self.lable.text() + '/')

    def button_plus_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('+')
        self.lable.clear()
        self.count = 1

    def button_minus_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('-')
        self.lable.clear()
        self.count = 2

    def button_clear_was_cliced(self):
        self.temp = 0
        self.lable.clear()

    # def button_clear_1_was_cliced(self):
    #     self.lable.text([-1])

    def button_multiply_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('*')
        self.lable.clear()
        self.count = 3

    def button_divide_was_cliced(self):
        self.temp = self.lable.text()
        self.lable.setText('/')
        self.lable.clear()
        self.count = 4






    def button_equal_was_cliced(self):
        if self.count==1:
            self.lable.setText(str(int(self.temp)+int(self.lable.text())))

        if self.count==2:
            self.lable.setText(str(int(self.temp)-int(self.lable.text())))

        if self.count==3:
            self.lable.setText(str(int(self.temp)*int(self.lable.text())))

        if self.count==4:
            self.lable.setText(str(int(self.temp)/int(self.lable.text())))





apps=QApplication([])
window = MainWindow()
window.show()
sys.exit(apps.exec())
