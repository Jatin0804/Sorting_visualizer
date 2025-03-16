'''
Quick Sort is a divide-and-conquer algorithm that selects a pivot element, 
partitions the array around the pivot, and recursively sorts the left and right partitions.
'''
# Worst case time complexity: O(n^2)
# Best case time complexity: O(n log n)

from .base_sort import BaseSort

class QuickSort(BaseSort):
    def run(self):
        self.quick_sort(0, len(self.data) - 1)
        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)  # Final sorted color
        self.draw()

    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high):
        pivot = self.data[high]  # Choosing last element as pivot
        i = low - 1

        for j in range(low, high):
            if not self.running:
                return low  # Stop sorting if interrupted

            self.highlight_bars([j, high], "#e74c3c")  # Highlight pivot and current element

            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.draw()

            self.reset_bars([j, high])  # Reset highlight

        # Swap pivot to correct position
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.draw()
        
        return i + 1
