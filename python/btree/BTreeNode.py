# Searching a key on a B-tree in Python


# Create a node
class BTreeNode:
    def __init__(self, leaf=False):
        """
        Initializes a B-tree node.

        Args:
        - leaf (bool): Indicates whether the node is a leaf node (default: False).
        """
        self.leaf = leaf
        self.keys = []  # List to store keys
        self.child = []  # List to store child nodes
