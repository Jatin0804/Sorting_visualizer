from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, 
                             QVBoxLayout, QPushButton, QSlider, 
                             QComboBox, QGraphicsView, 
                             QGraphicsScene)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QBrush, QPen
import random

from sorts.bubble_sort import BubbleSort
from sorts.selection_sort import SelectionSort
from sorts.insertion_sort import InsertionSort
from sorts.radix_sort import RadixSort
from sorts.counting_sort import CountingSort
from sorts.quick_sort import QuickSort
from sorts.shell_sort import ShellSort
from sorts.merge_sort import MergeSort
from sorts.heap_sort import HeapSort
from sorts.tim_sort import TimSort
from sorts.comb_Sort import CombSort

class SortingVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorting Visualizer")
        self.setGeometry(100, 100, 900, 500)

        self.data = []
        self.sorting_thread = None
        self.dataset_size = 50
        self.bar_colors = []

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
        self.algorithm_selector.addItems([
            "Bubble Sort",
            "Comb Sort",
            "Counting Sort",
            "Heap Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            "Radix Sort",
            "Selection Sort",
            "Shell Sort",
            "Tim Sort"
        ])
        layout.addWidget(self.algorithm_selector)

        # Speed Slider
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(10)
        self.speed_slider.setMaximum(500)
        self.speed_slider.setValue(100)

        layout.addWidget(QLabel("Sorting Speed:"))
        layout.addWidget(self.speed_slider)

        # Size Slider
        self.size_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.size_slider.setMinimum(10)  
        self.size_slider.setMaximum(150)  
        self.size_slider.setValue(50)  
        self.size_slider.valueChanged.connect(self.update_dataset_size)

        layout.addWidget(QLabel("Dataset Size:"))
        layout.addWidget(self.size_slider)

        self.setLayout(layout)
        self.create_dataset()

    def update_dataset_size(self):
        """ Updates dataset size when slider is changed """
        self.dataset_size = self.size_slider.value()
        self.create_dataset()


    def create_dataset(self):
        """
        The function `create_dataset` generates a random dataset of 50 integers between 10 and 100 and
        then calls the `draw_data` method.
        """
        self.data = [random.randint(10, 100) for _ in range(self.dataset_size)]
        self.bar_colors = ["#2980b9"] * len(self.data)
        self.draw_data()

    def draw_data(self):
        """
        The `draw_data` function draws bars representing data values on the screen using PyQt.
        """
        self.scene.clear()
        width = self.view.width()
        height = self.view.height()
        bar_width = max(5, width // len(self.data))

        for i, value in enumerate(self.data):
            x = i * bar_width
            y = height - (value / 100) * height
            color = self.bar_colors[i]
            
            self.scene.addRect(x, y, bar_width - 2, height - y, QPen(QColor("black")), QBrush(QColor(color)))

        self.update()

    def start_sorting(self):
        """ Starts sorting with selected algorithm """
        algorithm = self.algorithm_selector.currentText()
        # speed = self.speed_slider.value()

        if algorithm == "Bubble Sort":
            self.sorting_thread = BubbleSort(self.data, self)
        elif algorithm == "Counting Sort":
            self.sorting_thread = CountingSort(self.data, self)
        elif algorithm == "Selection Sort":
            self.sorting_thread = SelectionSort(self.data, self)
        elif algorithm == "Insertion Sort":
            self.sorting_thread = InsertionSort(self.data, self)
        elif algorithm == "Radix Sort":
            self.sorting_thread = RadixSort(self.data, self)
        elif algorithm == "Quick Sort":
            self.sorting_thread = QuickSort(self.data, self)
        elif algorithm == "Shell Sort":
            self.sorting_thread = ShellSort(self.data, self)
        elif algorithm == "Merge Sort":
            self.sorting_thread = MergeSort(self.data, self)
        elif algorithm == "Heap Sort":
            self.sorting_thread = HeapSort(self.data, self)
        elif algorithm == "Tim Sort":
            self.sorting_thread = TimSort(self.data, self)
        elif algorithm == "Comb Sort":
            self.sorting_thread = CombSort(self.data, self)

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

