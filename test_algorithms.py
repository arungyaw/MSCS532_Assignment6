# Run selection benchmarks and demonstrate all elementary data structures.

import csv
import random
import time

from data_structures import Array, Matrix, Queue, SinglyLinkedList, Stack
from selection_algorithms import deterministic_select, randomized_select


RESULTS_FILE = "selection_results.csv"


def create_dataset(size, distribution):
    # Create one dataset while keeping duplicate values possible.
    values = [random.randint(0, size // 2) for _ in range(size)]

    if distribution == "sorted":
        return sorted(values)

    if distribution == "reverse_sorted":
        return sorted(values, reverse=True)

    return values


def average_time(function, values, k, repeats=5):
    # Measure the average running time across several trials.
    total_time = 0.0

    for _ in range(repeats):
        start_time = time.perf_counter()
        result = function(values, k)
        total_time += time.perf_counter() - start_time

        # Confirm that each algorithm returned the correct order statistic.
        expected = sorted(values)[k - 1]

        if result != expected:
            raise AssertionError(
                f"{function.__name__} returned {result}, but expected {expected}."
            )

    return total_time / repeats


def test_selection_edge_cases():
    # Check duplicates, negative values, and boundary k values.
    test_values = [7, 2, 7, -3, 5, 2, 10]

    expected_smallest = -3
    expected_largest = 10
    expected_fourth = 5

    assert deterministic_select(test_values, 1) == expected_smallest
    assert randomized_select(test_values, 1) == expected_smallest

    assert deterministic_select(test_values, len(test_values)) == expected_largest
    assert randomized_select(test_values, len(test_values)) == expected_largest

    assert deterministic_select(test_values, 4) == expected_fourth
    assert randomized_select(test_values, 4) == expected_fourth

    print("Selection edge-case tests passed.")


def run_selection_benchmarks():
    # Compare both selection algorithms and save the results to a CSV file.
    input_sizes = [100, 500, 1000, 2500, 5000]
    distributions = ["random", "sorted", "reverse_sorted"]
    rows = []

    print("\nSelection Algorithm Performance")
    print("-" * 79)
    print(
        f"{'Size':>7} {'Distribution':>17} "
        f"{'Deterministic (s)':>20} {'Randomized (s)':>18}"
    )
    print("-" * 79)

    for size in input_sizes:
        for distribution in distributions:
            values = create_dataset(size, distribution)

            # Select the middle order statistic for every dataset.
            k = (size + 1) // 2

            deterministic_time = average_time(
                deterministic_select, values, k
            )
            randomized_time = average_time(
                randomized_select, values, k
            )

            rows.append(
                {
                    "input_size": size,
                    "distribution": distribution,
                    "k": k,
                    "deterministic_time_seconds": deterministic_time,
                    "randomized_time_seconds": randomized_time,
                }
            )

            print(
                f"{size:>7} {distribution:>17} "
                f"{deterministic_time:>20.10f} {randomized_time:>18.10f}"
            )

    with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = [
            "input_size",
            "distribution",
            "k",
            "deterministic_time_seconds",
            "randomized_time_seconds",
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nPerformance results saved to {RESULTS_FILE}.")


def demonstrate_array():
    print("\nArray Demonstration")
    array = Array()
    array.append(10)
    array.append(20)
    array.insert(1, 15)
    print("After insertion:", array.to_list())

    removed_value = array.delete(0)
    print("Deleted value:", removed_value)
    print("After deletion:", array.to_list())

    array.update(0, 99)
    print("Access index 0 after update:", array.access(0))


def demonstrate_matrix():
    print("\nMatrix Demonstration")
    matrix = Matrix([[1, 2], [3, 4]])
    matrix.insert_row(1, [5, 6])
    matrix.insert_column(2, [7, 8, 9])
    print("After row and column insertion:", matrix.to_list())

    removed_row = matrix.delete_row(1)
    removed_column = matrix.delete_column(2)
    print("Deleted row:", removed_row)
    print("Deleted column:", removed_column)

    matrix.update(0, 0, 100)
    print("Value at row 0, column 0:", matrix.access(0, 0))
    print("Final matrix:", matrix.to_list())


def demonstrate_stack():
    print("\nStack Demonstration")
    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    print("Stack after pushes:", stack.to_list())
    print("Top value:", stack.peek())
    print("Popped value:", stack.pop())
    print("Stack after pop:", stack.to_list())


def demonstrate_queue():
    print("\nQueue Demonstration")
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print("Queue after enqueues:", queue.to_list())
    print("Front value:", queue.peek())
    print("Dequeued value:", queue.dequeue())
    print("Queue after dequeue:", queue.to_list())


def demonstrate_linked_list():
    print("\nSingly Linked List Demonstration")
    linked_list = SinglyLinkedList()
    linked_list.insert_front(20)
    linked_list.insert_front(10)
    linked_list.insert_end(40)
    linked_list.insert_at(2, 30)
    print("After insertions:", linked_list.traverse())
    print("Index of 30:", linked_list.search(30))

    linked_list.delete(20)
    print("After deleting 20:", linked_list.traverse())


def run_data_structure_demonstrations():
    # Run basic operations for every required data structure.
    print("\n" + "=" * 45)
    print("ELEMENTARY DATA STRUCTURE TESTS")
    print("=" * 45)

    demonstrate_array()
    demonstrate_matrix()
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_linked_list()


def main():
    # A fixed seed makes the benchmark data reproducible.
    random.seed(42)

    test_selection_edge_cases()
    run_selection_benchmarks()
    run_data_structure_demonstrations()

    print("\nAll tests completed successfully.")


if __name__ == "__main__":
    main()