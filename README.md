# Day-1-Bubble-Sort
Here Python Program for Bubble Sort. Day 1 of Day 365.

......Bubble Sort......

- Concept: Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

- Steps:
    1. Start with an unsorted list of elements.
    2. Compare the first two elements:
        - If the first element is greater than the second, swap them.
        - If the first element is smaller or equal, do nothing.
    3. Move to the next pair of adjacent elements and repeat the comparison and swap process.
    4. Continue this process for each pair of adjacent elements in the list.
    5. At the end of the first pass through the list, the largest element will have "bubbled up" to its correct position (end of the list).
    6. Repeat the above steps for the remaining unsorted portion of the list (excluding the last sorted element).
    7. Continue repeating the passes until no swaps are needed, indicating the list is sorted.

- Characteristics:
    - Simple and easy to implement.
    - Inefficient for large lists (time complexity of O(n^2)).
    - Best used for small lists or lists that are nearly sorted.

Here’s example for clarity:
List: [5, 3, 8, 4, 2]

Pass 1:
[3, 5, 8, 4, 2]
[3, 5, 4, 8, 2]
[3, 5, 4, 2, 8]

Pass 2:
[3, 4, 5, 2, 8]
[3, 4, 2, 5, 8]

Pass 3:
[3, 2, 4, 5, 8]

Pass 4:
[2, 3, 4, 5, 8]
