'''
Insertion Sort is a simple and efficient algorithm for small datasets. 
It works similarly to sorting playing cards by picking one card at a time and inserting it into its correct position.
'''
# Worst-case performance: O(n^2)
# Best-case performance: O(n)

from .base_sort import BaseSort

class InsertionSort(BaseSort):
    def run(self):

        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1

            while j >= 0 and self.data[j] > key:
                if not self.running:
                    return 
                
                self.highlight_bars([j, j + 1], '#e74c3c')
                self.data[j + 1] = self.data[j]
                self.draw()

                self.reset_bars([j, j + 1])
                j -= 1

            self.data[j + 1] = key
            self.draw()

        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.draw()
