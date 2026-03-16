from src.TreeNode import TreeNode

def build_recipe_tree(self, item_name, amount, return_value):
    #Build TreeNode recursively from item and amount
    item = next((i for i in self.items if i.name == item_name), None)
    if not item:
        return None
    
    # Create root node (showing final amount)
    root = TreeNode(item_name, amount)
    
    # Recursively add children
    build_tree_recursive(self, root, item, amount, return_value)
    
    return root

def build_tree_recursive(self, node, item, amount, return_value):
    # Recursively add children to a TreeNode
    for ingredient in item.ingredients:
        # Calculate ingredient amount needed
        ingredient_amount = ingredient.quantity * amount / return_value
        
        # Create child node
        child_node = TreeNode(ingredient.name, ingredient_amount)
        node.add_child(child_node)
        
        # Recurse if ingredient has a recipe
        ingredient_item = next((i for i in self.items if i.name == ingredient.name), None)
        if ingredient_item:
            ingredient_return = ingredient_item.get_product_quantity()
            build_tree_recursive(self, child_node, ingredient_item, ingredient_amount, ingredient_return)

def extract_raw_materials(self, node):
    #Recursively extract raw materials from TreeNode
    raw_materials = {}
    
    def traverse(n):
        if n.name in [i.name for i in self.rawResources]:
            raw_materials[n.name] = raw_materials.get(n.name, 0) + n.amount
        
        for child in n.children:
            traverse(child)
    
    traverse(node)
    return raw_materials

def extract_raw_materials(self, node):
    #Recursively extract raw materials from TreeNode
    raw_materials = {}
    
    def traverse(n):
        if n.name in [i.name for i in self.rawResources]:
            raw_materials[n.name] = raw_materials.get(n.name, 0) + n.amount
        
        for child in n.children:
            traverse(child)
    
    traverse(node)
    return raw_materials
