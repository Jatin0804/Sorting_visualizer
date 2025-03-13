from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSlider, QComboBox, QGraphicsView, QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QBrush, QPen
import random
from sorts.bubble_sort import BubbleSort
from sorts.selection_sort import SelectionSort

class SortingVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorting Visualizer")
        self.setGeometry(100, 100, 900, 500)

        self.data = []
        self.sorting_thread = None

        # Layout
        layout = QVBoxLayout()
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        layout.addWidget(self.view)

        # Control Buttons
        self.generate_button = QPushButton("Generate Data")
        self.sort_button = QPushButton("Sort")
        self.stop_button = QPushButton("Stop")
        
        self.generate_button.clicked.connect(self.create_dataset)
        self.sort_button.clicked.connect(self.start_sorting)
        self.stop_button.clicked.connect(self.stop_sorting)

        layout.addWidget(self.generate_button)
        layout.addWidget(self.sort_button)
        layout.addWidget(self.stop_button)

        # Sorting Algorithm Selector
        self.algorithm_selector = QComboBox()
        self.algorithm_selector.addItems(["Bubble Sort", "Selection Sort"])
        layout.addWidget(self.algorithm_selector)

        # Speed Slider
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(10)
        self.speed_slider.setMaximum(500)
        self.speed_slider.setValue(100)
        layout.addWidget(self.speed_slider)

        self.setLayout(layout)
        self.create_dataset()

    def create_dataset(self):
        """ Generates random dataset """
        self.data = [random.randint(10, 100) for _ in range(50)]
        self.draw_data()

    def draw_data(self):
        """ Draws the bars on the screen """
        self.scene.clear()
        width = self.view.width()
        height = self.view.height()
        bar_width = max(5, width // len(self.data))

        for i, value in enumerate(self.data):
            x = i * bar_width
            y = height - (value / 100) * height
            rect = self.scene.addRect(x, y, bar_width - 2, height - y, QPen(QColor("black")), QBrush(QColor("#2980b9")))

        self.update()

    def start_sorting(self):
        """ Starts sorting with selected algorithm """
        algorithm = self.algorithm_selector.currentText()
        # speed = self.speed_slider.value()

        if algorithm == "Bubble Sort":
            self.sorting_thread = BubbleSort(self.data, self)
        elif algorithm == "Selection Sort":
            self.sorting_thread = SelectionSort(self.data, self)

        self.sorting_thread.update_signal.connect(self.draw_data)
        self.sorting_thread.start()

    def stop_sorting(self):
        """ Stops sorting """
        if self.sorting_thread and self.sorting_thread.isRunning():
            self.sorting_thread.stop()
            self.sorting_thread.wait()

def main():
    app = QApplication([])
    window = SortingVisualizer()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
