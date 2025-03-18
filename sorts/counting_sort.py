'''
Counting Sort is a non-comparative sorting algorithm that counts the occurrence of each element and places them in their correct positions.
'''
# Worst case time complexity: O(n + k)
# Best case time complexity: O(n + k)

from .base_sort import BaseSort

class CountingSort(BaseSort):
    complexities = {
        "worst": "O(n + k)",
        "average": "O(n + k)",
        "best": "O(n + k)"
    }
    def run(self):
        if not self.data:
            return

        max_val = max(self.data)
        count = [0] * (max_val + 1)
        output = [0] * len(self.data)

        # Count occurrences
        for num in self.data:
            count[num] += 1

        # Cumulative count
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Place elements in output array (traverse from right to maintain stability)
        for i in range(len(self.data) - 1, -1, -1):
            if not self.running:
                return
            num = self.data[i]
            output[count[num] - 1] = num
            count[num] -= 1
            self.highlight_bars([i], "#e74c3c")  # Highlight current bar
            self.draw()
            self.reset_bars([i])

        # Copy back sorted elements
        for i in range(len(self.data)):
            self.data[i] = output[i]
            self.draw()

        # Final visualization color
        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.draw()
