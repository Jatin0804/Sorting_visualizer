import sys
import time
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QLabel, QComboBox, QGraphicsView, QGraphicsScene, QGraphicsRectItem
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor

# Configuration
DEFAULT_CONFIG = {
    "INITIAL_ELEMENTS": 50,
    "INITIAL_SPEED": 100,
}
COLORS = {
    "BAR": QColor("#3498db"),
    "BACKGROUND": QColor("#f5f5f5"),
    "TEXT": QColor("#333"),
}

def get_random_value():
    return random.randint(10, 100)

class SortingVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorting Visualizer - PyQt6")
        self.setGeometry(100, 100, 1000, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.layout.addWidget(self.view)
        
        self.controls = QHBoxLayout()
        self.layout.addLayout(self.controls)
        
        # Buttons & Controls
        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self.create_dataset)
        self.controls.addWidget(self.generate_btn)
        
        self.size_slider = QSlider(Qt.Orientation.Horizontal)
        self.size_slider.setMinimum(10)
        self.size_slider.setMaximum(100)
        self.size_slider.setValue(DEFAULT_CONFIG["INITIAL_ELEMENTS"])
        self.size_slider.valueChanged.connect(self.update_size)
        self.controls.addWidget(QLabel("Size: "))
        self.controls.addWidget(self.size_slider)
        
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(10)
        self.speed_slider.setMaximum(500)
        self.speed_slider.setValue(DEFAULT_CONFIG["INITIAL_SPEED"])
        self.speed_slider.valueChanged.connect(self.update_speed)
        self.controls.addWidget(QLabel("Speed: "))
        self.controls.addWidget(self.speed_slider)
        
        self.algorithm_dropdown = QComboBox()
        self.algorithm_dropdown.addItems(["Bubble Sort", "Selection Sort"])
        self.controls.addWidget(self.algorithm_dropdown)
        
        self.sort_btn = QPushButton("Sort")
        self.sort_btn.clicked.connect(self.start_sorting)
        self.controls.addWidget(self.sort_btn)
        
        self.number_of_elements = DEFAULT_CONFIG["INITIAL_ELEMENTS"]
        self.speed = DEFAULT_CONFIG["INITIAL_SPEED"]
        self.data = []
        
        self.create_dataset()
    
    def create_dataset(self):
        self.data = [get_random_value() for _ in range(self.number_of_elements)]
        self.draw_data()
    
    def update_size(self):
        self.number_of_elements = int(self.size_slider.value())
        self.create_dataset()
    
    def update_speed(self):
        self.speed = self.speed_slider.maximum() - self.speed_slider.value() + self.speed_slider.minimum()
    
    def draw_data(self):
        self.scene.clear()
        bar_width = self.view.width() // self.number_of_elements
        canvas_height = self.view.height()
        for i, value in enumerate(self.data):
            rect = QGraphicsRectItem(i * bar_width, canvas_height - (value * 3), bar_width - 2, value * 3)
            rect.setBrush(COLORS["BAR"])
            self.scene.addItem(rect)
    
    def start_sorting(self):
        algorithm = self.algorithm_dropdown.currentText()
        if algorithm == "Bubble Sort":
            self.bubble_sort()
        elif algorithm == "Selection Sort":
            self.selection_sort()
    
    def bubble_sort(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1 - i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_data()
                    QApplication.processEvents()
                    time.sleep(self.speed / 1000)
    
    def selection_sort(self):
        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw_data()
            QApplication.processEvents()
            time.sleep(self.speed / 1000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())
