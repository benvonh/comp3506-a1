"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

from structures.dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._size: int = 0
        self._offset : int = 16
        self._reverse: bool = False
        self._data: DynamicArray = DynamicArray()

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        return 'not done'

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if not 0 <= index < self._size:
            return
        
        if self._reverse:
            bit_index = self._size - 1 + self._offset - index
            elem = self._data[bit_index // self.BITS_PER_ELEMENT]
            bit = elem & (1 << (self.BITS_PER_ELEMENT - 1 - (bit_index % self.BITS_PER_ELEMENT))) # type: ignore
        else:
            bit_index = index + self._offset
            elem = self._data[bit_index // self.BITS_PER_ELEMENT]
            bit = elem & (1 << (bit_index % self.BITS_PER_ELEMENT)) # type: ignore
        
        return 1 if bit else 0

    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if not 0 <= index < self._size:
            return

        if self._reverse:
            bit_index = self._size - 1 + self._offset - index
            elem = self._data[bit_index // self.BITS_PER_ELEMENT]
            mask = elem | (1 << (self.BITS_PER_ELEMENT - 1 - (bit_index % self.BITS_PER_ELEMENT))) # type: ignore
            self._data[bit_index // self.BITS_PER_ELEMENT] = mask
        else:
            bit_index = index + self._offset
            elem = self._data[bit_index // self.BITS_PER_ELEMENT]
            mask = elem | (1 << (bit_index % self.BITS_PER_ELEMENT)) # type: ignore
            self._data[bit_index // self.BITS_PER_ELEMENT] = mask

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if not 0 <= index < self._size:
            return

        if self._reverse:
            bit_index = self._size - 1 + self._offset - index
            elem = self._data[bit_index // self.BITS_PER_ELEMENT]
            mask = elem & ~(1 << (self.BITS_PER_ELEMENT - 1 - (bit_index % self.BITS_PER_ELEMENT))) # type: ignore
            self._data[bit_index // self.BITS_PER_ELEMENT] = mask
        else:
            bit_index = index + self._offset
            elem = self._data[bit_index // self.BITS_PER_ELEMENT]
            mask = elem & ~(1 << (bit_index % self.BITS_PER_ELEMENT)) # type: ignore
            self._data[bit_index // self.BITS_PER_ELEMENT] = mask

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if state:
            self.set_at(index)
        else:
            self.unset_at(index)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        self.__pend(False if not self._reverse else True, state)

    def prepend(self, state: int) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        self.__pend(True if not self._reverse else False, state)

    def __pend(self, front: bool, state: int) -> None:
        if front:
            if self._offset == 0:
                self._offset = self.BITS_PER_ELEMENT - 1
                self._data.prepend(int(state << self._offset))
            else:
                self._offset -= 1
                if state:
                    self.set_at(0)
                else:
                    self.unset_at(0)
        else:
            if (self._offset + self._size) % self.BITS_PER_ELEMENT == 0:
                self._data.append(state)
            else:
                if state:
                    self.set_at(self._offset + self._size)
                else:
                    self.unset_at(self._offset + self._size)

        self._size += 1

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        self._data.reverse()
        self._reverse = not self._reverse
        assert self._reverse is self._data._reverse

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        pass

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._size
