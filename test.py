import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout


class JarvisUi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Jarvis UI")
        self.setFixedSize(1908, 932)

        # Create central widget and main layout
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.main_layout = QVBoxLayout(self.centralwidget)

        # Background image
        self.bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.bg_1.setScaledContents(True)  # Ensure image scales to fit
        try:
            self.bg_1.setPixmap(QtGui.QPixmap("GUI materials/Black_Template.jpg"))  # Assuming image path is correct
        except FileNotFoundError:
            print("Error: Image file 'GUI materials/Black_Template.jpg' not found.")

        self.main_layout.addWidget(self.bg_1)

        # Create sections with appropriate layouts
        self.left_section = self.create_left_section()
        self.right_section = self.create_right_section()
        self.bottom_section = self.create_bottom_section()

        # Add sections to main layout
        self.main_layout.addWidget(self.left_section)
        self.main_layout.addWidget(self.right_section)
        self.main_layout.addWidget(self.bottom_section)

    def create_left_section(self):
        # Create left section layout and widgets (e.g., GIFs, labels)
        left_section_layout = QVBoxLayout()

        self.bg_2 = QtWidgets.QLabel()
        self.bg_2.setStyleSheet("background-color: lightblue")  # Customize color if needed
        left_section_layout.addWidget(self.bg_2)

        self.Gif_1 = QtWidgets.QLabel()
        self.Gif_1.setScaledContents(True)
        try:
            self.Gif_1.setPixmap(QtGui.QPixmap("GUI materials/Iron_Template_9.gif"))
        except FileNotFoundError:
            print("Error: Image file 'GUI materials/Iron_Template_9.gif' not found.")
        left_section_layout.addWidget(self.Gif_1)

        self.Gif_3 = QtWidgets.QLabel()
        self.Gif_3.setScaledContents(True)
        try:
            self.Gif_3.setPixmap(QtGui.QPixmap("GUI materials/Ntuks.gif"))
        except FileNotFoundError:
            print("Error: Image file 'GUI materials/Ntuks.gif' not found.")
        left_section_layout.addWidget(self.Gif_3)

        # ... add more widgets for the left section ...

        return left_section_layout

    def create_right_section(self):
        # Create right section layout and widgets (e.g., GIFs, labels)
        right_section_layout = QVBoxLayout()

        self.bg_3 = QtWidgets.QLabel()
        self.bg_3.setStyleSheet("background-color: lightblue")
        right_section_layout.addWidget(self.bg_3)

        self.Gif_2 = QtWidgets.QLabel()
        self.Gif_2.setScaledContents(True)
        try:
            self.Gif_2.setPixmap(QtGui.QPixmap("GUI materials/live.gif"))
        except FileNotFoundError:
            print("Error: Image file 'GUI materials/live.gif' not found.")
        right_section_layout.addWidget(self.Gif_2)

        self.bg_4 = QtWidgets.QLabel()
        self.bg_4.setStyleSheet("background-color: lightblue")
        right_section_layout.addWidget(self.bg_4)

        self.Gif_4 = QtWidgets.QLabel()
        self.Gif_4.setScaledContents(True)
        try:
            self.Gif_4.setPixmap(QtGui.QPixmap("GUI materials/Earth_Template.gif"))
        except FileNotFoundError:
            print("Error: Image file 'GUI materials/Earth_Template.gif' not found.")
        right_section_layout.addWidget(self.Gif_4)

        # ... add more widgets for the right
