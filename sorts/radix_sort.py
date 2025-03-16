from .base_sort import BaseSort

class RadixSort(BaseSort):
    def run(self):
        if not self.data:
            return

        max_num = max(self.data)
        exp = 1

        while max_num // exp > 0:
            self.counting_sort(exp)
            exp *= 10  # Move to the next digit

        # Final visualization color
        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)
        self.draw()

    def counting_sort(self, exp):
        n = len(self.data)
        output = [0] * n
        count = [0] * 10  # Digits 0-9

        # Count occurrences of each digit at the current exponent place
        for i in range(n):
            index = (self.data[i] // exp) % 10
            count[index] += 1

        # Convert count array to cumulative sum
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build output array (traverse from right to maintain stability)
        for i in range(n - 1, -1, -1):
            index = (self.data[i] // exp) % 10
            output[count[index] - 1] = self.data[i]
            count[index] -= 1

        # Copy output back to data and visualize sorting
        for i in range(n):
            if not self.running:
                return
            self.highlight_bars([i], "#e74c3c")  # Highlight current bar
            self.data[i] = output[i]
            self.draw()
            self.reset_bars([i])
