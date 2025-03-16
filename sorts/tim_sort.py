'''
Tim Sort is a hybrid sorting algorithm that combines Merge Sort and Insertion Sort to optimize real-world sorting performance. It is used in Python’s built-in sorting functions.
'''
# Worst case time complexity: O(n log n)
# Best case time complexity: O(n)

from .base_sort import BaseSort

class TimSort(BaseSort):
    RUN = 32  # Standard RUN size used in Tim Sort

    def run(self):
        n = len(self.data)

        # Step 1: Sort small chunks using Insertion Sort
        for i in range(0, n, self.RUN):
            self.insertion_sort(i, min(i + self.RUN - 1, n - 1))

        # Step 2: Merge chunks using Merge Sort
        size = self.RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))

                if mid < right:
                    self.merge(left, mid, right)

            size *= 2  # Increase merge size

        # Final visualization color
        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.draw()

    def insertion_sort(self, left, right):
        """Sorts a small subarray using Insertion Sort."""
        for i in range(left + 1, right + 1):
            key = self.data[i]
            j = i - 1

            while j >= left and self.data[j] > key:
                if not self.running:
                    return
                self.highlight_bars([j, j + 1], "#e74c3c")  # Highlight comparison
                self.data[j + 1] = self.data[j]
                self.draw()
                self.reset_bars([j, j + 1])
                j -= 1

            self.data[j + 1] = key
            self.draw()

    def merge(self, left, mid, right):
        """Merges two sorted subarrays."""
        left_part = self.data[left: mid + 1]
        right_part = self.data[mid + 1: right + 1]

        i, j, k = 0, 0, left

        while i < len(left_part) and j < len(right_part):
            if not self.running:
                return
            if left_part[i] <= right_part[j]:
                self.data[k] = left_part[i]
                i += 1
            else:
                self.data[k] = right_part[j]
                j += 1

            self.highlight_bars([k], "#e74c3c")  # Highlight merging process
            self.draw()
            self.reset_bars([k])
            k += 1

        while i < len(left_part):
            if not self.running:
                return
            self.data[k] = left_part[i]
            self.highlight_bars([k], "#e74c3c")
            self.draw()
            self.reset_bars([k])
            i += 1
            k += 1

        while j < len(right_part):
            if not self.running:
                return
            self.data[k] = right_part[j]
            self.highlight_bars([k], "#e74c3c")
            self.draw()
            self.reset_bars([k])
            j += 1
            k += 1
