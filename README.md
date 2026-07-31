# Assignment 6: Medians, Order Statistics, and Elementary Data Structures

## How to Run the Code

Make sure these files are in the same folder:

```text
selection_algorithms.py
data_structures.py
test_algorithms.py
```

Open a terminal in that folder and run:

```bash
python test_algorithms.py
```

On Windows, you can also use:

```bash
py test_algorithms.py
```

The program will test both selection algorithms, demonstrate all required data structures, and create:

```text
selection_results.csv
```

## Summary of Findings

Both the deterministic Median of Medians algorithm and Randomized Quickselect correctly found the kth smallest value for random, sorted, and reverse-sorted datasets.

The deterministic algorithm provides O(n) worst-case time complexity. Randomized Quickselect provides O(n) expected time complexity, but its worst case can be O(n^2).

In the performance tests, Randomized Quickselect was faster in most cases because it has less pivot-selection overhead. The deterministic algorithm was slower in practice, but it provides a stronger worst-case guarantee.

The elementary data structure tests also showed that:

- Arrays provide fast indexed access.
- Stacks follow last-in, first-out order.
- Queues follow first-in, first-out order.
- Circular queues avoid shifting elements during dequeue operations.
- Singly linked lists support insertion and deletion through node references.
