'''
Comb Sort is an improved version of Bubble Sort that eliminates turtles 
(small elements near the end of the list that slow down sorting). It compares elements at a decreasing gap.
'''
# Worst-case time complexity: O(n²), but typically much faster.
# Best-case time complexity: O(n log n)

from .base_sort import BaseSort


class CombSort(BaseSort):
    complexities = {
        "worst": "O(n²)",
        "average": "O(n log n)",
        "best": "O(n log n)"
    }
    def run(self):
        n = len(self.data)
        gap = n  # Initialize gap size
        shrink_factor = 1.3  # Standard shrink factor for Comb Sort
        sorted = False  # Flag to check if sorting is completed

        while gap > 1 or not sorted:
            gap = max(1, int(gap / shrink_factor))  # Reduce gap size
            sorted = True  # Assume sorted

            for i in range(n - gap):
                if not self.running:
                    return
                
                self.highlight_bars([i, i + gap], "#e74c3c")  # Highlight comparison

                if self.data[i] > self.data[i + gap]:  # Swap if needed
                    self.data[i], self.data[i + gap] = self.data[i + gap], self.data[i]
                    self.draw()
                    sorted = False  # Sorting is not done yet

                self.reset_bars([i, i + gap])  # Reset colors

        # Final visualization color
        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.draw()
