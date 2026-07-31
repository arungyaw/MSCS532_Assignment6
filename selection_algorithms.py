# Selection algorithms for Assignment 6.

# Both public functions use a 1-based value for k.
# For example, k=1 returns the smallest value.


import random


def _validate_input(values, k):
    # Check that the array and k value are valid.
    if not values:
        raise ValueError("The array cannot be empty.")

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if k < 1 or k > len(values):
        raise ValueError("k must be between 1 and the array length.")


def _median_of_medians(values):
    # Choose a reliable pivot by using groups of five.
    if len(values) <= 5:
        ordered_values = sorted(values)
        return ordered_values[len(ordered_values) // 2]

    medians = []

    # Divide the values into groups of five and find each group median.
    for start in range(0, len(values), 5):
        group = sorted(values[start:start + 5])
        medians.append(group[len(group) // 2])

    # Recursively find the median of the group medians.
    return _median_of_medians(medians)


def _deterministic_select(values, target_index):
    # Return the value at target_index using Median of Medians.
    if len(values) <= 5:
        return sorted(values)[target_index]

    pivot = _median_of_medians(values)

    # Three-way partitioning correctly handles duplicate values.
    smaller = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    larger = [value for value in values if value > pivot]

    if target_index < len(smaller):
        return _deterministic_select(smaller, target_index)

    if target_index < len(smaller) + len(equal):
        return pivot

    new_index = target_index - len(smaller) - len(equal)
    return _deterministic_select(larger, new_index)


def deterministic_select(values, k):
    # Return the kth smallest value using worst-case linear-time selection.
    _validate_input(values, k)

    # Copy the input so the original array is not changed.
    copied_values = list(values)
    return _deterministic_select(copied_values, k - 1)


def randomized_select(values, k):
    # Return the kth smallest value using Randomized Quickselect.
    _validate_input(values, k)

    # Work with a copy so the original array remains unchanged.
    remaining = list(values)
    target_index = k - 1

    while True:
        if len(remaining) <= 5:
            return sorted(remaining)[target_index]

        pivot = random.choice(remaining)

        # Three-way partitioning avoids problems when duplicates are present.
        smaller = [value for value in remaining if value < pivot]
        equal = [value for value in remaining if value == pivot]
        larger = [value for value in remaining if value > pivot]

        if target_index < len(smaller):
            remaining = smaller
        elif target_index < len(smaller) + len(equal):
            return pivot
        else:
            target_index -= len(smaller) + len(equal)
            remaining = larger