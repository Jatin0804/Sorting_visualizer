from .base_sort import BaseSort

# The BubbleSort class implements the bubble sort algorithm to sort a list of data.
class BubbleSort(BaseSort):
    def run(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1 - i):
                if not self.running:
                    return
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw()
