from .base_sort import BaseSort

class BubbleSort(BaseSort):
    def run(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1 - i):
                if not self.running:
                    return
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw()
