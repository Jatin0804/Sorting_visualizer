from .base_sort import BaseSort
import random

class BogoSort(BaseSort):
    complexities = {
        "worst": "O(∞)",
        "average": "O((n+1)!)",
        "best": "O(n)"
    }

    def run(self):
        while not self.is_sorted():
            if not self.running:
                return
            self.shuffle()
            self.draw()
        
        # Final visualization color
        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.draw()
    
    def is_sorted(self):
        """Check if the data is sorted."""
        for i in range(len(self.data) - 1):
            if self.data[i] > self.data[i + 1]:
                return False
        return True
    
    def shuffle(self):
        """Randomly shuffle the data."""
        random.shuffle(self.data)
        self.highlight_bars(range(len(self.data)), "#e74c3c")  # Highlight all bars while shuffling
        self.draw()
