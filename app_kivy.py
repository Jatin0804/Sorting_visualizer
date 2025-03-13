import time
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

DEFAULT_CONFIG = {
    "INITIAL_ELEMENTS": 50,
    "INITIAL_SPEED": 100,
}

def get_random_value():
    return random.randint(10, 100)

class SortingVisualizerApp(App):
    def build(self):
        self.number_of_elements = DEFAULT_CONFIG["INITIAL_ELEMENTS"]
        self.speed = DEFAULT_CONFIG["INITIAL_SPEED"]
        self.data = []
        
        layout = BoxLayout(orientation='vertical')
        control_layout = BoxLayout(size_hint_y=0.2)
        
        self.canvas_area = BoxLayout()
        layout.add_widget(self.canvas_area)
        
        self.generate_btn = Button(text="Generate")
        self.generate_btn.bind(on_press=self.create_dataset)
        control_layout.add_widget(self.generate_btn)
        
        self.size_slider = Slider(min=10, max=100, value=self.number_of_elements)
        self.size_slider.bind(value=self.update_size)
        control_layout.add_widget(Label(text="Size: "))
        control_layout.add_widget(self.size_slider)
        
        self.speed_slider = Slider(min=10, max=500, value=self.speed)
        self.speed_slider.bind(value=self.update_speed)
        control_layout.add_widget(Label(text="Speed: "))
        control_layout.add_widget(self.speed_slider)
        
        self.algorithm_spinner = Spinner(text="Bubble Sort", values=["Bubble Sort", "Selection Sort"])
        control_layout.add_widget(self.algorithm_spinner)
        
        self.sort_btn = Button(text="Sort")
        self.sort_btn.bind(on_press=self.start_sorting)
        control_layout.add_widget(self.sort_btn)
        
        layout.add_widget(control_layout)
        self.create_dataset()
        return layout
    
    def create_dataset(self, *args):
        self.data = [get_random_value() for _ in range(self.number_of_elements)]
        self.draw_data()
    
    def update_size(self, instance, value):
        self.number_of_elements = int(value)
        self.create_dataset()
    
    def update_speed(self, instance, value):
        self.speed = 510 - int(value)  # Inverted so that higher value = faster sorting
    
    def draw_data(self):
        self.canvas_area.canvas.clear()
        with self.canvas_area.canvas:
            bar_width = self.canvas_area.width / self.number_of_elements
            for i, value in enumerate(self.data):
                Color(0.2, 0.6, 1, 1)
                Rectangle(
                    pos=(i * bar_width, 0),
                    size=(bar_width - 2, value * 3)
                )
    
    def start_sorting(self, *args):
        algorithm = self.algorithm_spinner.text
        if algorithm == "Bubble Sort":
            Clock.schedule_once(lambda dt: self.bubble_sort(), 0)
        elif algorithm == "Selection Sort":
            Clock.schedule_once(lambda dt: self.selection_sort(), 0)
    
    def bubble_sort(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1 - i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_data()
                    time.sleep(self.speed / 1000)
    
    def selection_sort(self):
        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw_data()
            time.sleep(self.speed / 1000)

if __name__ == '__main__':
    SortingVisualizerApp().run()