"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

# so we can hint Node get_next
from __future__ import annotations

from typing import Any


class Node:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next Node
        self._prev = None  # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_next(self) -> Node | None:
        return self._next

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def get_prev(self) -> Node | None:
        return self._prev


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    Note that any time you see `Any` in the type annotations,
    this refers to the "data" stored inside a Node.

    [V3: Note that this API was changed in the V3 spec] 
    """

    def __init__(self) -> None:
        self._size: int = 0
        self._head: Any = None
        self._tail: Any = None
        self._reverse: bool = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        msg: str = '[ '
        counter: int = 0
        node = self._head

        while counter < self._size:
            msg += node.get_data()
            node = node.get_next()
            counter += 1
        
        msg += ' ]'
        return msg

    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_head(self) -> Any | None:
        """
        Return the data of the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return

        if self._reverse:
            return self._tail.get_data()

        return self._head.get_data()

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return
        
        if self._reverse:
            self._tail.set_data(data)
        else:
            self._head.set_data(data)

    def get_tail(self) -> Any | None:
        """
        Return the data of the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return
        
        if self._reverse:
            return self._head.get_data()
        
        return self._tail.get_data()

    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return
        
        if self._reverse:
            self._head.set_data(data)
        else:
            self._tail.set_data(data)

    """
    More interesting functionality now.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert the given data to the front of the list.
        Hint: You will need to create a Node type containing
        the given data.
        Time complexity for full marks: O(1)
        """
        # Explicit condition between 'is reversed' and 'is front'
        self.__insert(True if not self._reverse else False, data)

    def insert_to_back(self, data: Any) -> None:
        """
        Insert the given data (in a node) to the back of the list
        Time complexity for full marks: O(1)
        """
        # Explicit condition between 'is reversed' and 'is front'
        self.__insert(False if not self._reverse else True, data)

    def __insert(self, front: bool, data: Any) -> None:
        # Create node and loop to itself
        if self._size == 0:
            self._head = Node(data)
            self._head.set_next(self._head)
            self._head.set_prev(self._head)
            self._tail = self._head
        # Insert node at real front and redo link
        elif front:
            tmp = self._head
            self._head = Node(data)
            self._head.set_next(tmp)
            tmp.set_prev(self._head)
        # Insert node at real back and redo link
        else:
            tmp = self._tail
            self._tail = Node(data)
            self._tail.set_prev(tmp)
            tmp.set_next(self._tail)
        # Increment size counter
        self._size += 1

    def remove_from_front(self) -> Any | None:
        """
        Remove the front node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        # Explicit condition between 'is reversed' and 'is front'
        return self.__remove(True if not self._reverse else False)

    def remove_from_back(self) -> Any | None:
        """
        Remove the back node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        # Explicit condition between 'is reversed' and 'is front'
        return self.__remove(False if not self._reverse else True)

    def __remove(self, front: bool) -> Any | None:
        # Do nothing for empty list
        if self._size == 0:
            return
        # Get data and remove head+tail
        if self._size == 1:
            data = self._head.get_data()
            self._head = None
            self._tail = None
        # Get data and remove node at real front
        elif front:
            data = self._head.get_data()
            self._head = self._head.get_next()
            self._head.set_prev(None)
        # Get data and remove node at real back
        else:
            data = self._tail.get_data()
            self._tail = self._tail.get_prev()
            self._tail.set_next(None)
        # Decrement size counter and return data
        self._size -= 1
        return data

    def find_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        return self.__find_node(elem) is not None

    def find_and_remove_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list; if a match is
        found, this node is removed from the linked list, and True is returned.
        False is returned if no match is found.
        Time complexity for full marks: O(N)
        """
        node = self.__find_node(elem)
        # Do nothing for no match
        if node is None:
            return False
        # Check pointer and remove head
        if node is self._head:
            self.remove_from_front()
        # Check pointer and remove tail
        elif node is self._tail:
            self.remove_from_back()
        # Must be in the middle (>3)
        # Link left and right nodes together
        else:
            left = node.get_prev()
            right = node.get_next()
            left.set_next(right) # type: ignore
            right.set_prev(left) # type: ignore
        # Node was removed
        return True

    def __find_node(self, elem: Any) -> Node | None:
        counter: int = 0
        # Find elem in reverse
        if self._reverse:
            node = self._tail
            # Loop for size many times
            while counter < self._size:
                if node.get_data() == elem:
                    return node
                # Get previous node
                counter += 1
                node = node.get_prev()
        # Find elem in forward
        else:
            node = self._head
            # Loop for size many times
            while counter < self._size:
                if node.get_data() == elem:
                    return node
                # Get next node
                counter += 1
                node = node.get_next()

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        self._reverse = not self._reverse
