from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_JarvisUi(object):
 
    def setupUi(self, JarvisUi):
        JarvisUi.setObjectName("JarvisUi")
        JarvisUi.resize(400, 500)  # Adjust size as needed
        JarvisUi.setWindowTitle("Dry Run")
        

        self.centralwidget = QtWidgets.QWidget(JarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("padding:10px; margin-top:20px;")

        # Set background image
        self.Gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_3.setGeometry(QtCore.QRect(0, 0, 400, 500))  # Adjust size as needed
        self.Gif_3.setText("")
        self.Gif_3.setPixmap(QtGui.QPixmap("GUI matrials/Ntuks.gif"))
        self.Gif_3.setScaledContents(True)
        self.Gif_3.setStyleSheet(" margin 10px; border:1px solid transparent ; border-radius:50px")
        self.Gif_3.setObjectName("Gif_3")

        # Create label for displaying time
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(0, 440, 150, 50))  # Adjust size as needed
        self.label_time.setObjectName("label_time")
        self.update_time()  # Update time initially

        # Create label for displaying day
        self.label_day = QtWidgets.QLabel(self.centralwidget)
        self.label_day.setGeometry(QtCore.QRect(300, 440, 150, 50))  # Adjust size as needed
        self.label_day.setObjectName("label_day")
        
        self.update_day()  # Update day initially

        # Make buttons transparent
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(150, 160, 100, 60))  # Adjust size as needed
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.setFlat(True)
        self.pushButton_start.setStyleSheet("background-color: transparent; border:  1px solid #fff; border-radius:20px; color :white;")

        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(150, 260, 100, 60))  # Adjust size as needed
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_exit.setFlat(True)
        self.pushButton_exit.setStyleSheet("background-color: transparent; border:  1px solid #fff; border-radius:20px; color :white;")

    
        self.display_box = QtWidgets.QLabel(self.centralwidget)
        self.display_box.setGeometry(QtCore.QRect(20,20,350,60))  # Adjust size as needed
        self.display_box.setStyleSheet("color: #467d73; font-weight: bold; font size-20px;")
        self.display_box.setObjectName("display_box")
        self.update_msg()
     
        JarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(JarvisUi)
        QtCore.QMetaObject.connectSlotsByName(JarvisUi)

    def retranslateUi(self, JarvisUi):
        _translate = QtCore.QCoreApplication.translate
        JarvisUi.setWindowTitle(_translate("JarvisUi", "Dry Run"))
        self.pushButton_start.setText(_translate("JarvisUi", "START"))
        self.pushButton_exit.setText(_translate("JarvisUi", "EXIT"))

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.label_time.setText(current_time)
        QtCore.QTimer.singleShot(1000, self.update_time)  # Update time every second

    def update_day(self):
        current_day = datetime.datetime.now().strftime("%A")
        self.label_day.setText(current_day)

    def update_msg(self):
        global msg
        self.display_box.setText(msg)
        QtCore.QTimer.singleShot(1000, self.update_msg)  # Update time every second
    def display(ms):
        global msg
        msg=ms
       

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    JarvisUi = QtWidgets.QMainWindow()
    ui = Ui_JarvisUi()
    screen_geo = app.desktop().availableGeometry()
    win_geo = JarvisUi.frameGeometry()
    x = screen_geo.width() - win_geo.width()
    y = screen_geo.height() - win_geo.height()
    JarvisUi.move(x, y)
    ui.setupUi(JarvisUi)
    
    JarvisUi.show()
    sys.exit(app.exec_())