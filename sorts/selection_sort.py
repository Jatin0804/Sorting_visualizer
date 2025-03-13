from .base_sort import BaseSort

class SelectionSort(BaseSort):
    def run(self):
        for i in range(len(self.data)):
            if not self.running:
                return
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw()
