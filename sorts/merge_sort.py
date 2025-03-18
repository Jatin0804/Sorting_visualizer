'''
Merge Sort is a stable sorting algorithm that follows the divide-and-conquer approach. 
It recursively divides the array into smaller subarrays, sorts them, and merges them back together in sorted order.
'''
# Worst case time complexity: O(n log n)
# Best case time complexity: O(n log n)

from .base_sort import BaseSort

class MergeSort(BaseSort):
    complexities = {
        "worst": "O(n log n)",
        "average": "O(n log n)",
        "best": "O(n log n)"
    }
    def run(self):
        self.merge_sort(0, len(self.data) - 1)
        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)  # Final sorted color
        self.draw()

    def merge_sort(self, left, right):
        """Recursively splits and sorts the array."""
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        """Merges two sorted halves."""
        if not self.running:
            return

        left_half = self.data[left:mid + 1]
        right_half = self.data[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_half) and j < len(right_half):
            if not self.running:
                return

            self.highlight_bars([k], "#e74c3c")  # Highlight merge step
            if left_half[i] <= right_half[j]:
                self.data[k] = left_half[i]
                i += 1
            else:
                self.data[k] = right_half[j]
                j += 1

            self.draw()
            self.reset_bars([k])
            k += 1

        while i < len(left_half):
            if not self.running:
                return

            self.highlight_bars([k], "#e74c3c")
            self.data[k] = left_half[i]
            self.draw()
            self.reset_bars([k])
            i += 1
            k += 1

        while j < len(right_half):
            if not self.running:
                return

            self.highlight_bars([k], "#e74c3c")
            self.data[k] = right_half[j]
            self.draw()
            self.reset_bars([k])
            j += 1
            k += 1
