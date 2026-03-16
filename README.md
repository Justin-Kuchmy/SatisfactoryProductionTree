# Satisfactory Production Tree

A PyQt6 desktop app for [Satisfactory](https://www.satisfactorygame.com/) that lets you visualise the full ingredient tree for any item. Set your desired production rate (items per minute) and the app recursively calculates every intermediate ingredient needed, plus a summary of all raw materials (iron ore, coal, copper ore, crude oil, etc.) required to meet your target.

---

## Features

- Browse and search all craftable items
- Set a target production rate (items/min)
- View the full recursive ingredient tree
- See a breakdown of total raw materials needed
- Clean Qt-based UI via a `.ui` file

---

## Download & Run

Go to the [Releases](../../releases) page and download the build for your platform.

### Windows

1. Download `SatisfactoryProductionTree-windows.zip`
2. Extract the zip — you'll get a `SatisfactoryProductionTree` folder
3. Open the folder and double-click `SatisfactoryProductionTree.exe`

> **Note:** On first launch Windows may take a moment to scan the bundled DLLs. Subsequent launches will be instant.

### Linux

1. Download `SatisfactoryProductionTree.x86_64`
2. Make it executable and run it:

```bash
chmod +x SatisfactoryProductionTree.x86_64
./SatisfactoryProductionTree.x86_64
```

---

## Build from Source

### Requirements

- Python 3.12.3+
- PyQt6

### Setup

```bash

git clone https://github.com/Justin-Kuchmy/SatisfactoryProductionTree.git
cd SatisfactoryProductionTree

python3 -m venv myenv
source myenv/bin/activate  # Windows: myenv\Scripts\activate

pip install PyQt6
```

### Run

```bash
python3 main.py
```

### Build executable (optional)

```bash
pip install pyinstaller

# Linux
pyinstaller --onefile --windowed --name SatisfactoryProductionTree.x86_64 --add-data "ui:ui" --add-data "src/Data:Data" main.py

# Windows
pyinstaller --onedir --windowed --collect-all PyQt6 --name SatisfactoryProductionTree --add-data "ui;ui" --add-data "src/Data;Data" main.py
```

---

## Project Structure

```
SatisfactoryProductionTree/
├── main.py               # Entry point
├── src/
│   ├── MainWindow.py     # Main UI logic
│   ├── Tree_Builder.py   # Recursive tree construction
│   ├── Item.py           # Item model
│   ├── Resource.py       # Raw resource model
│   ├── Ingredient.py     # Ingredient model
│   ├── TreeNode.py       # Tree node model
│   └── Data/
│       ├── Recipes.json  # Item recipes
│       └── Resources.json# Raw resource definitions
└── ui/
    └── satisfactory_calculator.ui  # Qt UI layout
```
