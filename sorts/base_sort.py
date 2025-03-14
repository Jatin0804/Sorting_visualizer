from PyQt6.QtCore import QThread, pyqtSignal
from utils.helpers import sleep

class BaseSort(QThread):
    # The line `update_signal = pyqtSignal()` is creating a custom signal named `update_signal` using
    # PyQt6's `pyqtSignal` class. This signal can be emitted to notify other parts of the program that
    # an update has occurred and they need to take some action, such as updating the UI. By defining
    # this signal in the class, you can connect it to slots (functions) in other objects to handle the
    # update event.
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
        # `self.update_signal.emit()` is emitting the custom signal `update_signal`. When this line is
        # executed, it notifies any connected slots (functions) that are listening for this signal
        # that an update event has occurred. This allows other parts of the program to respond to the
        # update event, such as updating the user interface (UI) to reflect changes in the data or
        # state of the program.
        self.update_signal.emit()
        sleep(self.get_speed())
