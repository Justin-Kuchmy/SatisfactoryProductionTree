from PyQt6.QtWidgets import QTreeWidgetItem

class TreeNode:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.children = []
    
    def add_child(self, child):
        """Add a child node"""
        self.children.append(child)
    
    def to_tree_widget_item(self, parent=None):
        if parent is None:
            item = QTreeWidgetItem()
        else:
            item = QTreeWidgetItem(parent)
        
        item.setText(0, self.name)
        item.setText(1, str(round(self.amount, 2)))
        
        for child in self.children:
            child.to_tree_widget_item(item)
        
        return item