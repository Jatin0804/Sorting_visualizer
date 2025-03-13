from PyQt6.QtCore import QThread, pyqtSignal
from utils.helpers import sleep

class BaseSort(QThread):
    update_signal = pyqtSignal()

    def __init__(self, data, visualizer):
        super().__init__()
        self.data = data
        # self.speed = speed
        self.visualizer = visualizer
        self.running = True

    def get_speed(self):
        # return self.visualizer.speed_slider.value()

        max_speed = self.visualizer.speed_slider.maximum()
        min_speed = self.visualizer.speed_slider.minimum()
        slider_value = self.visualizer.speed_slider.value()
        
        return max_speed + min_speed - slider_value  # Reverse effect

    def stop(self):
        """ Stops sorting """
        self.running = False

    def draw(self):
        """ Updates UI """
        self.update_signal.emit()
        sleep(self.get_speed())
