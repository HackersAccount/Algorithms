from typing import List, Optional


class Node:
    """
    Node class representing a node in  a Btree.

    Attributes:
    - keys (List[int]): A list of keys stored in the node.
    - children (List[Node]): A list of child nodes.
    - leaf (bool): A flag  indicating whether the node is a leaf node.
    """

    def __init__(self, leaf: bool = True) -> None:
        """
        Initializes a new Node instance.


        Args:
        - leaf (bool): Indicates whether the node is a leaf node (default: True)
        """
        self.keys: List[int] = []
        self.children: List[Node] = []
        self.leaf: bool = leaf

    def insert(self, key: int):
        """
        Inserts a key into the node  or its child nodes recursively.

        Args:
        - key (int): The key to insert.
        """
        if self.leaf:
            self._insert_leaf(key)
        else:
            index: int = len(self.keys - 1)
            while index >= 0 and key < self.keys[index]:
                index -= 1
            index += 1
            if len(self.children[index].keys) == 3:
                self._split_child(index)
                if key > self.keys[index]:
                    index += 1
            self.children[index].insert(key)

    def _insert_leaf(self, key: int) -> None:
        """
        Inserts a key into the leaf node.

        Args:
        - key (int): The key to insert.
        """
        self.keys.append(key)
        self.keys.sort()

    def _split_child(self, index: int) -> None:
        """
        Splits a child node when it is full.

        Args:
        - index (int): The index of the child node to split.
        """
        new_child = Node(leaf=self.children[index].leaf)
        split_index = len(self.children[index].keys) // 2
        median = self.children[index].keys[split_index]

        new_child.keys = self.children[index].keys[split_index + 1 :]
        self.children[index].keys = self.children[index].keys[:split_index]

        if not self.children[index].leaf:
            new_child.children = self.children[index].children[split_index + 1 :]
            self.children[index].children = self.children[index].children[
                : split_index + 1
            ]

        self.keys.insert(index, median)
        self.children.insert(index + 1, new_child)

    def __str__(self) -> str:
        """
        Returns a string representation of the node.

        Returns:
        - str: A string representation of the node.
        """
        return f"{self.keys}"
