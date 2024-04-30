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
