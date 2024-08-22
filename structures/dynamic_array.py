"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any, List


class DynamicArray:
    def __init__(self) -> None:
        self._size: int = 0
        self._offset: int = 16
        self._capacity: int = 64
        self._reverse: bool = False
        self._data: List = [None] * self._capacity

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        return 'not done'

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if not 0 <= index < self._size:
            return
        
        if self._reverse:
            return self._data[self._size - index - 1 + self._offset]
    
        return self._data[index + self._offset]

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if not 0 <= index < self._size:
            return
        
        if self._reverse:
            self._data[self._size - index - 1 + self._offset] = element
        else:
            self._data[index + self._offset] = element

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        self.set_at(index, element)

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        # Explicit condition between 'is reversed' and 'is front'
        self.__pend(False if not self._reverse else True, element)

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        # Explicit condition between 'is reversed' and 'is front'
        self.__pend(True if not self._reverse else False, element)

    def __pend(self, front: bool, element: Any) -> None:
        # Increase capacity left of array
        if self._offset == 0:
            new_offset: int = self._capacity
            self._capacity *= 2
            new_data: List = [None] * self._capacity
            # Copy data to the same position but where the left-side was extended
            for i in range(self._size):
                new_data[i + new_offset] = self._data[i + self._offset]
            # Assign to new offset and buffer
            self._offset = new_offset
            self._data = new_data
        # Increase capacity right of array
        if self._size + self._offset == self._capacity:
            self._capacity *= 2
            new_data: List = [None] * self._capacity
            # Copy data to the same position but where the right-side was extended
            for i in range(self._size):
                new_data[i + self._offset] = self._data[i + self._offset]
            # Assign to new buffer
            self._data = new_data
        
        # Assign element to the front
        if front:
            self._data[self._offset - 1] = element
            self._offset -= 1
        # Assign element to the back
        else:
            self._data[self._size + self._offset] = element
            # self._offset += 1
        
        self._size += 1

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        self._reverse = not self._reverse

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        index = None
        # Loop data from right to left
        if self._reverse:
            for i in range(self._size - 1 - self._offset, self._offset - 1, -1):
                if self._data[i] == element:
                    index = i
                    break
        # Loop data from left to right
        else:
            for i in range(self._offset, self._offset + self._size):
                if self._data[i] == element:
                    index = i
                    break
        # No index if no match
        if index is None:
            return
        # Smart remove that index match
        self.remove_at(index)
                    
    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        if not 0 <= index < self._size:
            return
        # Collapse array on the left of element to the right
        if self._reverse:
            # Save removed data first
            data = self._data[self._size - 1 + index + self._offset]
            # Begin looping to the left of index
            for i in range(self._size - 1 - index + self._offset, self._offset + 1, -1):
                self._data[i] = self._data[i - 1]
            # Clean first element and increment offset
            self._data[self._offset] = None
            self._offset += 1
        # Collapse array on the right of element to the left
        else:
            # Save removed data first
            data = self._data[index + self._offset]
            # Begin looping to the right of index
            for i in range(index + self._offset, self._size - 1 + self._offset):
                self._data[i] = self._data[i + 1]
            # Clean last element
            self._data[self._size - 1] = None
        # Decrement size counter and return removed data
        self._size -= 1
        return data

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        return self._size == 0

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        return self._size == self._capacity

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        Time complexity for full marks: O(NlogN)
        """
        pass
