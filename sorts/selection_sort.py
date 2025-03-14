from .base_sort import BaseSort

class SelectionSort(BaseSort):
    """
    The `SelectionSort` class implements the selection sort algorithm to sort a list of elements in
    ascending order.
    :return: In the provided code snippet, the `run` method of a class named `SelectionSort` is being
    executed. Within this method, a selection sort algorithm is implemented to sort the data stored in
    the object. The method iterates over the data and finds the minimum element in the unsorted portion
    of the list, then swaps it with the element at the current index.
    """
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
