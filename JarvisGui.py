from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextBrowser, QPushButton
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtCore import QTimer, QTime, QDate, QThread
import Main1
import os
import webbrowser as web
import sys
from JarvisUi import Ui_JarvisUi


class MainThread(QThread):
    def run(self):
        print("Running Main Thread")
        Main1.TaskExe()
startExe=MainThread()
class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_JarvisUi()
        self.gui.setupUi(self)
        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_exit.clicked.connect(self.close)
        


    def chrome_app(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def yt_app(self):
        web.open("https://www.youtube.com/")

    def whatsapp_app(self):
        web.open("https://web.whatsapp.com/")

    def startTask(self):

        self.gui.lable3 = QMovie("GUI matrials/Ntuks.gif")
        self.gui.Gif_3.setMovie(self.gui.lable3)
        self.gui.lable3.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString("hh:mm:ss") 
        d_ate = QDate.currentDate()
        date = d_ate.toString("yyyy-MM-dd")  
        lable_time = "Time: " + time
        lable_date = "Date: " + date

        self.gui.label_time.setText(lable_time)
        self.gui.label_time.setStyleSheet("color: red; font-size:10px;")
        self.gui.label_day.setText(lable_date)
        self.gui.label_day.setStyleSheet("color: red; font-size:10px;")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis_gui = Gui_Start()
    jarvis_gui.show()
    sys.exit(app.exec_())
  