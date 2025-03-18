'''
Heap Sort is a comparison-based sorting algorithm that builds a binary heap and 
repeatedly extracts the maximum element, placing it at the correct position in the sorted array.
'''
# Worst case time complexity: O(n log n)
# Best case time complexity: O(n log n)


from .base_sort import BaseSort

class HeapSort(BaseSort):
    complexities = {
        "worst": "O(n log n)",
        "average": "O(n log n)",
        "best": "O(n log n)"
    }
    def run(self):
        n = len(self.data)

        # Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            if not self.running:
                return
            
            # Swap the root (max element) with the last element
            self.highlight_bars([0, i], "#e74c3c")  # Highlight swap
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.draw()
            self.reset_bars([0, i])

            # Heapify the reduced heap
            self.heapify(i, 0)

        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)  # Final sorted color
        self.draw()

    def heapify(self, n, i):
        """Heapifies the subtree rooted at index i."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.data[left] > self.data[largest]:
            largest = left

        if right < n and self.data[right] > self.data[largest]:
            largest = right

        if largest != i:
            if not self.running:
                return
            
            # Swap and continue heapifying
            self.highlight_bars([i, largest], "#e74c3c")  # Highlight comparison
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.draw()
            self.reset_bars([i, largest])

            self.heapify(n, largest)
