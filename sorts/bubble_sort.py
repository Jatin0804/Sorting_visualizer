from .base_sort import BaseSort

# The BubbleSort class implements the bubble sort algorithm to sort a list of data.
# class BubbleSort(BaseSort):
#     def run(self):
#         for i in range(len(self.data) - 1):
#             for j in range(len(self.data) - 1 - i):
#                 if not self.running:
#                     return
#                 if self.data[j] > self.data[j + 1]:
#                     self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
#                     self.draw()

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
                    self.update_signal.emit()

                self.reset_bars([j, j + 1]) # Reset the bars to their original color

        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.update_signal.emit()
