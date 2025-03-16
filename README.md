# Sorting Visualizer

Sorting Visualizer is a graphical application built using **PyQt6** that demonstrates various sorting algorithms with real-time visual feedback. This project helps users understand how different sorting techniques work by showing step-by-step comparisons and swaps.

## Features
- **Multiple Sorting Algorithms**: Implements Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Merge Sort, Heap Sort, Counting Sort, Radix Sort, Shell Sort, Tim Sort, and Comb Sort.
- **Real-time Visualization**: Animates sorting steps with highlighted comparisons.
- **Customizable Speed**: Allows users to adjust sorting speed dynamically.
- **Interactive UI**: Users can start, stop, and reset sorting operations.

## Installation
### Prerequisites
- Python 3.8+
- PyQt6

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Jatin0804/sorting-visualizer.git
   cd sorting-visualizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the application using:
```bash
python main.py
```

## Sorting Algorithms Implemented
Each algorithm is implemented as a class inheriting from `BaseSort`, ensuring modularity and easy expansion.

- **Bubble Sort**: Compares adjacent elements and swaps them if they are in the wrong order.
- **Selection Sort**: Selects the smallest element and places it in the correct position.
- **Insertion Sort**: Builds the sorted array one element at a time.
- **Quick Sort**: Uses partitioning to recursively sort subarrays.
- **Merge Sort**: Splits the array and merges sorted halves.
- **Heap Sort**: Uses a binary heap to extract the largest element repeatedly.
- **Counting Sort**: Counts occurrences and reconstructs the sorted list.
- **Radix Sort**: Sorts numbers digit by digit using Counting Sort.
- **Shell Sort**: Improves Insertion Sort with gap-based sorting.
- **Tim Sort**: Hybrid sorting algorithm combining Merge Sort and Insertion Sort.
- **Comb Sort**: Enhanced Bubble Sort with gap shrinking.

## Contributing
Feel free to contribute by adding new features or optimizing existing ones. Fork the repo, create a branch, and submit a pull request!

## License
This project is licensed under the **MIT License**.
