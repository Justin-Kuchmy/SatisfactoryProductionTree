from src.Ingredient import Ingredient
class Item:
    """Represents a craftable item with recipe"""
    def __init__(self, name, key_name, category, time, ingredients, product):
        self.name = name
        self.key_name = key_name
        self.category = category
        self.time = time  # Seconds to craft
        self.ingredients = [Ingredient(ing["key"], ing["value"]) for ing in ingredients]
        self.product = [Ingredient(prod["key"], prod["value"]) for prod in product]
    
    @property
    def crafting_rate(self):
        """Items per minute"""
        return 60 / self.time
    
    def get_product_quantity(self):
        """How many of this item the recipe produces"""
        return self.product[0].quantity if self.product else 1

    def __str__(self):
        ingredients_str = "\n  ".join([f"- {ing.name}" for ing in self.ingredients])
        product_str = "\n  ".join([f"- {prod.name}" for prod in self.product])
        
        return (
            f"Item: {self.name}\n"
            f"  Key Name: {self.key_name}\n"
            f"  Category: {self.category}\n"
            f"  Time: {self.time}\n"
            f"  Ingredients:\n  {ingredients_str}\n"
            f"  Products:\n  {product_str}"
        )


