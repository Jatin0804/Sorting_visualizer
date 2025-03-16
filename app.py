import sys
# The code snippet is importing the `QApplication` class from the `QtWidgets` module of the PyQt6
# library. `QApplication` is used to manage the GUI application's control flow and main settings.
from PyQt6.QtWidgets import QApplication
from gui.sort_visualizer import SortingVisualizer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())
