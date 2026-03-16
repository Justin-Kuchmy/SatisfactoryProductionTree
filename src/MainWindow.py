import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QTreeWidgetItem, QSplitter
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Satisfactory Production Tree")
        self.resize(800, 600)
