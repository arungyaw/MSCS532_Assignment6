# Elementary data structure implementations for Assignment 6.


class Array:
    # A small dynamic array with insertion, deletion, and access operations.

    def __init__(self, capacity=4):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1.")

        self._capacity = capacity
        self._size = 0
        self._items = [None] * capacity

    def _resize(self):
        # Double the array capacity when it becomes full.
        self._capacity *= 2
        new_items = [None] * self._capacity

        for index in range(self._size):
            new_items[index] = self._items[index]

        self._items = new_items

    def insert(self, index, value):
        # Insert a value at the requested index.
        if index < 0 or index > self._size:
            raise IndexError("Array index out of range.")

        if self._size == self._capacity:
            self._resize()

        # Shift values to the right to make room for the new value.
        for current in range(self._size, index, -1):
            self._items[current] = self._items[current - 1]

        self._items[index] = value
        self._size += 1

    def append(self, value):
        # Add a value to the end of the array.
        self.insert(self._size, value)

    def delete(self, index):
        # Delete and return the value at the requested index.
        if index < 0 or index >= self._size:
            raise IndexError("Array index out of range.")

        removed_value = self._items[index]

        # Shift remaining values left to close the empty position.
        for current in range(index, self._size - 1):
            self._items[current] = self._items[current + 1]

        self._size -= 1
        self._items[self._size] = None
        return removed_value

    def access(self, index):
        # Return the value stored at an index.
        if index < 0 or index >= self._size:
            raise IndexError("Array index out of range.")

        return self._items[index]

    def update(self, index, value):
        # Replace the value stored at an index.
        if index < 0 or index >= self._size:
            raise IndexError("Array index out of range.")

        self._items[index] = value

    def to_list(self):
        # Return only the active array values.
        return self._items[:self._size]

    def __len__(self):
        return self._size


class Matrix:
    # A matrix that supports access, updates, row changes, and column changes.

    def __init__(self, values):
        if not values or not values[0]:
            raise ValueError("Matrix must contain at least one value.")

        column_count = len(values[0])

        for row in values:
            if len(row) != column_count:
                raise ValueError("All matrix rows must have the same length.")

        # Copy each row so changes do not affect the original input.
        self._values = [list(row) for row in values]

    @property
    def rows(self):
        return len(self._values)

    @property
    def columns(self):
        return len(self._values[0])

    def _check_position(self, row, column):
        if row < 0 or row >= self.rows:
            raise IndexError("Matrix row out of range.")

        if column < 0 or column >= self.columns:
            raise IndexError("Matrix column out of range.")

    def access(self, row, column):
        # Return the value at a row and column.
        self._check_position(row, column)
        return self._values[row][column]

    def update(self, row, column, value):
        # Replace the value at a row and column.
        self._check_position(row, column)
        self._values[row][column] = value

    def insert_row(self, index, row_values):
        # Insert a complete row into the matrix.
        if index < 0 or index > self.rows:
            raise IndexError("Matrix row index out of range.")

        if len(row_values) != self.columns:
            raise ValueError("The new row must match the matrix width.")

        self._values.insert(index, list(row_values))

    def delete_row(self, index):
        # Delete and return one matrix row.
        if self.rows == 1:
            raise ValueError("A matrix must keep at least one row.")

        if index < 0 or index >= self.rows:
            raise IndexError("Matrix row index out of range.")

        return self._values.pop(index)

    def insert_column(self, index, column_values):
        # Insert a complete column into the matrix.
        if index < 0 or index > self.columns:
            raise IndexError("Matrix column index out of range.")

        if len(column_values) != self.rows:
            raise ValueError("The new column must match the matrix height.")

        for row_index in range(self.rows):
            self._values[row_index].insert(index, column_values[row_index])

    def delete_column(self, index):
        # Delete and return one matrix column.
        if self.columns == 1:
            raise ValueError("A matrix must keep at least one column.")

        if index < 0 or index >= self.columns:
            raise IndexError("Matrix column index out of range.")

        removed_column = []

        for row in self._values:
            removed_column.append(row.pop(index))

        return removed_column

    def to_list(self):
        # Return a copy of the matrix values.
        return [row[:] for row in self._values]


class Stack:
    # A last-in, first-out stack implemented with the Array class.

    def __init__(self):
        self._items = Array()

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self._items.delete(len(self._items) - 1)

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")

        return self._items.access(len(self._items) - 1)

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def to_list(self):
        return self._items.to_list()


class Queue:
    # A first-in, first-out queue implemented as a circular array.

    def __init__(self, capacity=4):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1.")

        self._items = [None] * capacity
        self._front = 0
        self._size = 0

    def _resize(self):
        # Double the queue capacity without changing item order.
        new_items = [None] * (len(self._items) * 2)

        for index in range(self._size):
            old_index = (self._front + index) % len(self._items)
            new_items[index] = self._items[old_index]

        self._items = new_items
        self._front = 0

    def enqueue(self, value):
        if self._size == len(self._items):
            self._resize()

        rear_index = (self._front + self._size) % len(self._items)
        self._items[rear_index] = value
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        removed_value = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        return removed_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue.")

        return self._items[self._front]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def to_list(self):
        values = []

        for index in range(self._size):
            item_index = (self._front + index) % len(self._items)
            values.append(self._items[item_index])

        return values


class Node:
    # A single node used by the singly linked list.

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    # A singly linked list with insertion, deletion, search, and traversal.

    def __init__(self):
        self.head = None
        self._size = 0

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self._size += 1
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        self._size += 1

    def insert_at(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Linked-list index out of range.")

        if index == 0:
            self.insert_front(value)
            return

        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def delete(self, value):
        # Delete the first matching value and report whether it was found.
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head

        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True

            current = current.next

        return False

    def search(self, value):
        # Return the zero-based index of a value, or -1 when not found.
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index

            current = current.next
            index += 1

        return -1

    def traverse(self):
        # Return all values in linked-list order.
        values = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def __len__(self):
        return self._size