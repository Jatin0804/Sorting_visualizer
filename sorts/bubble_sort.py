'''
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they are in the wrong order. 
This process continues until the list is completely sorted.
'''
# Worst case time complexity: O(n^2)
# Best case time complexity: O(n)

from .base_sort import BaseSort

class BubbleSort(BaseSort):
    def run(self):
        n = len(self.data)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if not self.running:
                    return
                
                self.highlight_bars([j, j + 1], '#e74c3c') # red color for comparison

                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw()

                self.reset_bars([j, j + 1]) # Reset the bars to their original color

        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.draw()


# class BubbleSort(BaseSort):
#     def run(self):
#         for i in range(len(self.data) - 1):
#             for j in range(len(self.data) - 1 - i):
#                 if not self.running:
#                     return
#                 if self.data[j] > self.data[j + 1]:
#                     self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
#                     self.draw()
