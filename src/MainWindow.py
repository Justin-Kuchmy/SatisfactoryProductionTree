import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QTreeWidgetItem, QSplitter
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
import json
from src.Item import Item
from src.Resource import Resource

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Satisfactory Production Tree")
        loadUi("ui/satisfactory_calculator.ui", self)

        with open("src/Data/Recipes.json", "r") as file:
            rawRecipes = json.load(file)
        with open("src/Data/Resources.json", "r") as file:
            rawResources = json.load(file)

        self.items = [Item(**item) for item in rawRecipes]
        self.rawResources = [Resource(**raw_mat) for raw_mat in rawResources]

        self.loadItems()

        #connecting the ui elements to the python functions
        self.searchLineEdit.textChanged.connect(self.on_search_text_changed)
        self.calculateButton.clicked.connect(self.on_calculate_clicked)
        self.rateSpinBox.valueChanged.connect(self.on_spinbox_changed)
        self.itemListWidget.itemClicked.connect(self.on_item_clicked)
        self.allowUnderClocking.clicked.connect(self.toggleCheckBox)

        #right side of the app
        layout = self.rightPanel.layout()
        
        #create a splitter and add the two widgets that will be above and below
        splitter = QSplitter(Qt.Orientation.Vertical)
        splitter.addWidget(self.recipieTreeBox)
        splitter.addWidget(self.rawMaterialsBox)
        splitter.setSizes([400, 300])
        
        layout.addWidget(splitter) 

        main_layout = self.centralwidget.layout()
        main_layout.setStretch(0, 1)  #left column width (ratio. example 1/4, 25%)
        main_layout.setStretch(1, 1)  #center column width  (ratio. example 1/4, 25%)
        main_layout.setStretch(2, 2)  #right column width  (ratio. example 2/4, 50%)

    def loadItems(self):
        index = 0
        for i in range(len(self.items)):
            item_obj = self.items[i]
            display_name = item_obj.name.replace("_", " ")
            list_item = QListWidgetItem(display_name)
            list_item.setData(Qt.ItemDataRole.UserRole, {"obj": item_obj, "index": index})
            index += 1
            self.itemListWidget.addItem(list_item)

    def on_search_text_changed(self):
        pass
    def on_calculate_clicked(self):
        pass
    def on_spinbox_changed(self):
        pass    
    def on_item_clicked(self, list_item: QListWidgetItem):
        item = list_item.data(Qt.ItemDataRole.UserRole)
        label = "Selected Item: " + item["obj"].name
        self.selectedItemLabel.setText(label)
        self.selectedObject = item
    def toggleCheckBox(self):
        pass