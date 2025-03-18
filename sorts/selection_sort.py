'''
Selection Sort is a simple in-place sorting algorithm that repeatedly selects the smallest 
(or largest) element from the unsorted portion and moves it to the correct position.
'''
# Worst-case performance: O(n^2)
# Best-case performance: O(n^2)

from .base_sort import BaseSort

class SelectionSort(BaseSort):
    complexities = {
        "worst": "O(n²)",
        "average": "O(n²)",
        "best": "O(n²)"
    }
    def run(self):
        n = len(self.data)

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                if not self.running:
                    return
                
                self.highlight_bars([i, j], '#e74c3c') # red color for comparison

                if self.data[j] < self.data[min_idx]:
                    min_idx = j

                self.reset_bars([i, j]) # Reset the bars to their original color

            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw()

        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.draw()

# class SelectionSort(BaseSort):
#     
#     def run(self):
#         for i in range(len(self.data)):
#             if not self.running:
#                 return
#             min_idx = i
#             for j in range(i + 1, len(self.data)):
#                 if self.data[j] < self.data[min_idx]:
#                     min_idx = j
#             self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
#             self.draw()