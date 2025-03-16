# Sorting Algorithms Implemented in the Sorting Visualizer

---

## 1. Bubble Sort
### Description
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until the list is completely sorted.

### Implementation & Steps
- Start from the beginning of the list and compare each pair of adjacent elements.
- Swap them if they are in the wrong order.
- Continue this process for multiple passes until no swaps are needed.

### Best Case Use
- When the array is **nearly sorted**, as it can take advantage of its adaptive nature.

### Time Complexity
- **Best Case:** \( O(n) \) (when already sorted)
- **Worst/Average Case:** \( O(n^2) \)

---

## 2. Insertion Sort
### Description
Insertion Sort is a simple and efficient algorithm for small datasets. It works similarly to sorting playing cards by picking one card at a time and inserting it into its correct position.

### Implementation & Steps
- Consider the first element as sorted.
- Pick the next element and compare it with the sorted portion, shifting elements if necessary.
- Insert the picked element into the correct position.
- Repeat for all elements.

### Best Case Use
- When sorting **small or nearly sorted datasets**, as it performs efficiently in such cases.

### Time Complexity
- **Best Case:** \( O(n) \) (when the list is nearly sorted)
- **Worst/Average Case:** \( O(n^2) \)

---

## 3. Selection Sort
### Description
Selection Sort is a simple in-place sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion and moves it to the correct position.

### Implementation & Steps
- Find the smallest element in the unsorted section.
- Swap it with the first unsorted element.
- Move to the next element and repeat.
- Continue until the entire list is sorted.

### Best Case Use
- When **memory swaps are costly**, as it makes a minimal number of swaps.

### Time Complexity
- **Best/Worst/Average Case:** \( O(n^2) \)

---

## 4. Quick Sort
### Description
Quick Sort is a **divide-and-conquer** algorithm that selects a pivot element, partitions the array around the pivot, and recursively sorts the left and right partitions.

### Implementation & Steps
- Select a pivot element.
- Partition the array so that elements smaller than the pivot are on the left and larger elements are on the right.
- Recursively apply Quick Sort to the left and right subarrays.

### Best Case Use
- When **in-place sorting** is required with **randomly distributed elements**.

### Time Complexity
- **Best/Average Case:** \( O(n \log n) \)
- **Worst Case:** \( O(n^2) \) (when the pivot is always the smallest/largest element)

---

## 5. Merge Sort
### Description
Merge Sort is a stable sorting algorithm that follows the **divide-and-conquer** approach. It recursively divides the array into smaller subarrays, sorts them, and merges them back together in sorted order.

### Implementation & Steps
- Recursively divide the array into halves until each half contains a single element.
- Merge the halves back together in sorted order.

### Best Case Use
- When **stability** (maintaining the order of equal elements) is important.

### Time Complexity
- **Best/Worst/Average Case:** \( O(n \log n) \)

---

## 6. Heap Sort
### Description
Heap Sort is a comparison-based sorting algorithm that builds a **binary heap** and repeatedly extracts the maximum element, placing it at the correct position in the sorted array.

### Implementation & Steps
- Convert the array into a **Max Heap**.
- Extract the maximum element (root) and place it at the end.
- Heapify the remaining elements and repeat.

### Best Case Use
- When a **consistent \( O(n \log n) \) sorting algorithm** is required without additional memory allocation.

### Time Complexity
- **Best/Worst/Average Case:** \( O(n \log n) \)

---

## 7. Shell Sort
### Description
Shell Sort is an improved version of **Insertion Sort**, where elements are first sorted at large gaps and then progressively reduced until they are sorted at gap = 1.

### Implementation & Steps
- Start by sorting elements far apart (gap = \( n/2 \)).
- Reduce the gap size gradually and apply Insertion Sort.
- Continue until the gap becomes 1.

### Best Case Use
- When sorting **medium-sized arrays** efficiently without using extra space.

### Time Complexity
- **Best Case:** \( O(n \log n) \)
- **Worst Case:** \( O(n^2) \)

---

## 8. Radix Sort
### Description
Radix Sort is a non-comparative sorting algorithm that sorts numbers digit by digit, starting from the least significant to the most significant digit, using **Counting Sort** as a subroutine.

### Implementation & Steps
- Identify the maximum number to determine the number of digits.
- Sort the numbers digit by digit using Counting Sort.
- Continue the process until all digits are sorted.

### Best Case Use
- When sorting **large numbers with a fixed number of digits**, such as ZIP codes or phone numbers.

### Time Complexity
- **Best/Worst/Average Case:** \( O(d(n + k)) \) (where \( d \) is the number of digits and \( k \) is the range of values)

---

## 9. Counting Sort
### Description
Counting Sort is a non-comparative sorting algorithm that counts the occurrence of each element and places them in their correct positions.

### Implementation & Steps
- Create a frequency array to count occurrences of each value.
- Compute the cumulative count to determine the final positions.
- Place elements in the output array in sorted order.

### Best Case Use
- When sorting integers **within a known and limited range** efficiently.

### Time Complexity
- **Best/Worst/Average Case:** \( O(n + k) \)

---

## 10. Tim Sort
### Description
Tim Sort is a hybrid sorting algorithm that combines **Merge Sort and Insertion Sort** to optimize real-world sorting performance. It is used in Python’s built-in sorting functions.

### Implementation & Steps
- Break the array into **small chunks (runs)**.
- Sort each run using **Insertion Sort**.
- Merge sorted runs using **Merge Sort**.

### Best Case Use
- When sorting **real-world datasets** or when **Python’s built-in sorting** is needed.

### Time Complexity
- **Best Case:** \( O(n) \)
- **Worst/Average Case:** \( O(n \log n) \)

---

## 11. Comb Sort
### Description
Comb Sort is an improved version of **Bubble Sort** that eliminates turtles (small elements near the end of the list that slow down sorting). It compares elements at a decreasing gap.

### Implementation & Steps
- Initialize a gap factor (usually 1.3).
- Compare and swap elements at this gap.
- Reduce the gap until it reaches 1 (then it behaves like Bubble Sort).

### Best Case Use
- When an **efficient alternative to Bubble Sort** is needed for slightly faster sorting.

### Time Complexity
- **Best Case:** \( O(n \log n) \)
- **Worst Case:** \( O(n^2) \)

---

These are the sorting algorithms implemented so far. 
