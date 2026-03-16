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
        self.underClockingIsAllowed = False
        self.selectedObject = None

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

    def on_search_text_changed(self, text):
        for i in range(self.itemListWidget.count()):
            item = self.itemListWidget.item(i)
            matches = text.lower() in item.text().lower()
            item.setHidden(not matches)

    def on_calculate_clicked(self):
        if not self.selectedObject :
            return
        itemName = self.items[self.selectedObject["index"]].name
        returnValue = self.items[self.selectedObject["index"]].product[0].quantity
        item = next((i for i in self.items if i.name == itemName), None)
        
        # 60 seconds divided by number of time per craft.
        # multiply by the number of items each craft will return
        # example, each craft takes 6 seconds so we have 10 crafts per minute
        # but if each craft gives us 2 of said item so our default is 20 items per minute. 
        crafts_per_minute = 60 / item.time
        default_amount = crafts_per_minute * returnValue
      
        #get multiplier via spin box
        user_amount= self.rateSpinBox.value()
        
        # each item as a default "items made per minute"
        # use default if spinbox amount is lower then the spinbox value unless 
        # underClockingIsAllowed checkbox is checked
        if (user_amount < default_amount) and not self.underClockingIsAllowed:
            final_amount = default_amount
            self.rateSpinBox.setValue(final_amount)
        else:
            final_amount = user_amount
        
        self.statusbar.showMessage(f"Calculated {final_amount} {itemName}/min")   

    def on_spinbox_changed(self, text):
        self.rateSpinBox.setValue(round(float(text), 3))
        self.multiplier =  self.rateSpinBox.value()         

    def on_item_clicked(self, list_item: QListWidgetItem):
        item = list_item.data(Qt.ItemDataRole.UserRole)
        label = "Selected Item: " + item["obj"].name
        self.selectedItemLabel.setText(label)
        self.selectedObject = item
        self.rateSpinBox.setValue(1.00)
    def toggleCheckBox(self):
        self.underClockingIsAllowed =  self.allowUnderClocking.isChecked()