class Ingredient:
    """Represents a crafting ingredient or product"""

    #converts json key to normalized string
    RAW_MATERIALS = {
        "iron_ore": "iron",
        "copper_ore": "copper",
        "coal": "coal",
        "sam": "sam",
        "petroleum_coke": "petroleum coke",
        "compacted_coal": "compacted coal",
        "limestone": "limestone",
        "caterium_ore": "caterium",
        "sulfur": "sulfur",
        "raw_quartz": "quartz",
        "crude_oil": "oil",
        "bauxite": "bauxite",
        "water": "water",
        "uranium": "uranium",
        "nitrogen_gas": "nitrogen gas",
    }
    
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    @property
    def is_raw_material(self):
        """check if this is a raw material"""
        return self.name in self.RAW_MATERIALS
    
    def display_name(self):
        """get formatted display name"""
        return self.RAW_MATERIALS.get(self.name)