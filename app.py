import time
import random
import tkinter as tk
from tkinter import Canvas, Button, Scale, HORIZONTAL, StringVar, OptionMenu, Label, Frame

# Default Configuration
DEFAULT_CONFIG = {
    "INITIAL_ELEMENTS": 50,
    "INITIAL_SPEED": 100,
    "MOBILE_BREAKPOINT": 600
}
COLORS = {
    "PRIMARY": "#3498db",
    "SUCCESS": "#2ecc71",
    "DISABLED": "#95a5a6",
    "ACTIVE": "#e74c3c",
    "BAR": "#2980b9",
    "BACKGROUND": "#f5f5f5",
    "TEXT": "#333"
}

def sleep(duration):
    time.sleep(duration / 1000)

def get_random_value():
    return random.randint(10, 100)

def calculate_bar_width(number_of_elements, canvas_width):
    return max(5, canvas_width // number_of_elements)

def calculate_bar_height(value, is_mobile, canvas_height):
    return max(10, (value / 100) * (canvas_height if not is_mobile else canvas_height // 2))

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg=COLORS["BACKGROUND"])
        
        # Main Frame for Layout
        self.main_frame = Frame(root, bg=COLORS["BACKGROUND"])
        self.main_frame.pack(pady=10)
        
        # Canvas
        self.canvas = Canvas(self.main_frame, width=900, height=400, bg="white")
        self.canvas.pack()
        
        # Control Panel
        self.control_frame = Frame(self.main_frame, bg=COLORS["BACKGROUND"])
        self.control_frame.pack(pady=10)
        
        self.number_of_elements = DEFAULT_CONFIG["INITIAL_ELEMENTS"]
        self.speed = DEFAULT_CONFIG["INITIAL_SPEED"]
        self.data = []
        
        self.sorting_algorithms = {"Bubble Sort": self.bubble_sort, "Selection Sort": self.selection_sort}
        self.selected_algorithm = StringVar(root)
        self.selected_algorithm.set("Bubble Sort")
        
        # Buttons and Controls
        self.generate_btn = Button(self.control_frame, text="Generate", command=self.create_dataset, bg=COLORS["PRIMARY"], fg="white", font=("Arial", 12, "bold"))
        self.generate_btn.grid(row=0, column=0, padx=5)
        
        self.size_slider = Scale(self.control_frame, from_=10, to=100, orient=HORIZONTAL, command=self.update_size, bg=COLORS["BACKGROUND"], highlightthickness=0)
        self.size_slider.set(self.number_of_elements)
        self.size_slider.grid(row=0, column=1, padx=5)
        
        self.speed_slider = Scale(self.control_frame, from_=10, to=500, orient=HORIZONTAL, command=self.update_speed, bg=COLORS["BACKGROUND"], highlightthickness=0)
        self.speed_slider.set(self.speed)
        self.speed_slider.grid(row=0, column=2, padx=5)
        
        self.sort_menu = OptionMenu(self.control_frame, self.selected_algorithm, *self.sorting_algorithms.keys())
        self.sort_menu.grid(row=0, column=3, padx=5)
        
        self.sort_btn = Button(self.control_frame, text="Sort", command=self.start_sorting, bg=COLORS["SUCCESS"], fg="white", font=("Arial", 12, "bold"))
        self.sort_btn.grid(row=0, column=4, padx=5)
        
        self.create_dataset()
    
    def create_dataset(self):
        self.data = [get_random_value() for _ in range(self.number_of_elements)]
        self.draw_data()
    
    def update_size(self, event):
        self.number_of_elements = int(self.size_slider.get())
        self.create_dataset()
    
    def update_speed(self, event):
        max_speed = int(self.speed_slider["to"])
        min_speed = int(self.speed_slider["from"])
        slider_value = int(self.speed_slider.get())
        self.speed = max_speed + min_speed - slider_value
    
    def draw_data(self):
        self.canvas.delete("all")
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        bar_width = calculate_bar_width(self.number_of_elements, canvas_width)
        is_mobile = canvas_width <= DEFAULT_CONFIG["MOBILE_BREAKPOINT"]
        
        for i, value in enumerate(self.data):
            x0 = i * bar_width
            y0 = canvas_height - calculate_bar_height(value, is_mobile, canvas_height)
            x1 = x0 + bar_width
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=COLORS["BAR"], outline="black")
        self.root.update()
    
    def start_sorting(self):
        algorithm = self.selected_algorithm.get()
        self.sorting_algorithms[algorithm]()
    
    def bubble_sort(self):
        self.sort_btn.config(state="disabled", bg=COLORS["DISABLED"])
        
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1 - i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_data()
                    sleep(self.speed)
        
        self.sort_btn.config(state="normal", bg=COLORS["SUCCESS"])
    
    def selection_sort(self):
        self.sort_btn.config(state="disabled", bg=COLORS["DISABLED"])
        
        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw_data()
            sleep(self.speed)
        
        self.sort_btn.config(state="normal", bg=COLORS["SUCCESS"])

def main():
    root = tk.Tk()
    root.title("Sorting Visualizer")
    app = SortingVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
