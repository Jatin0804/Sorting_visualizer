import sys
from PyQt6.QtWidgets import QApplication
from gui.sort_visualizer import SortingVisualizer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())
